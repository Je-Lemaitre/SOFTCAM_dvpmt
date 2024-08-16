import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")

from domain.services.calculsloiscame import CalculRampe, CalculRaccord
import domain.services.calculsdynamique as cdyn
from domain.entities.loiscame import LoisPhaseRampe, LoisPhaseAccel, LoisPhaseRaccord, LoisPhaseDecel, LoisPhaseDecelV2, DemiLois, LoisCame
from domain.entities.assemblage import Assemblage, AssemblageLinguet, AssemblageDirecte
from application.interfaces.controller_interface import ControllerInterface
from geomdl import NURBS
import numpy as np
import scipy.integrate as scitg
import scipy.interpolate as scitp
import scipy.optimize as sco
import matplotlib.pyplot as plt
import domain.services.unitees as unit

class OptimiseLoisRampe():
    def __init__(self, vitesse_squel, levee_squel):
        self.duree_rampe = vitesse_squel[-1, 0] - vitesse_squel[0, 0]
        self.duree_vitesse_constante = vitesse_squel[-1, 0] - vitesse_squel[-2, 0]
        self.vitesse_rampe = vitesse_squel[-1, 1]
        self.levee_rampe = levee_squel[1, 1]

    def __call__(self):
        calcul_rampe = CalculRampe(
            duree_rampe = self.duree_rampe,
            duree_vitesse_constante = self.duree_vitesse_constante,
            vitesse_rampe = self.vitesse_rampe,
            levee_rampe = self.levee_rampe
        )

        return LoisPhaseRampe(
            duree_rampe = self.duree_rampe,
            a_rampe = calcul_rampe.a,
            v_rampe = calcul_rampe.v,
            l_rampe = calcul_rampe.l,
            j_rampe = calcul_rampe.j
        )

class OptimiseLoisAccel():
    def __init__(self, accel_squel, vitesse_squel, levee_squel):
        self.duree_accel = accel_squel[-1,0]
        self.vitesse_rampe = vitesse_squel[-1, 1]
        self.levee_rampe = levee_squel[1, 1]
        self.accel_squel = accel_squel
        pass

    def __call__(self, accelmax) -> LoisPhaseAccel:
        
        ctrlpts, weights = self.compute_ctrlpts(accelmax)
        a_spl = self.compute_a_spl(ctrlpts, weights, degree=3)
        
        return LoisPhaseAccel(
            duree_accel = self.duree_accel,
            vitesse_rampe = self.vitesse_rampe,
            levee_rampe = self.levee_rampe,
            a_spl = a_spl
        )
       
    def compute_a_spl(self, ctrlpts, poids, degree = 3, delta = 1e-4) -> scitp.BSpline:
        
        curve = NURBS.Curve()
        # Set degree of splines
        curve.degree = degree
        curve.ctrlpts = ctrlpts
        curve.knotvector = np.array([0,0,0,0,1,2,3,4,4,4,4])
        curve.delta = delta
        curve.weights = poids

        evalangles, evalaccels = np.array(curve.evalpts).T

        knot_vector, coefficients, degree = scitp.splrep(evalangles, evalaccels, k=degree)

        return scitp.BSpline(knot_vector, coefficients, degree, extrapolate=True)
    
    def compute_ctrlpts(self, accelmax : float = None) :
        if accelmax is None :
            accelmax = (self.accel_squel[2, 1] + self.accel_squel[-2, 1])/2 
        
        jf = -accelmax/(self.accel_squel[-1, 0] - self.accel_squel[-2, 0])

        ctrlpts = np.array([
            [self.accel_squel[0, 0], self.accel_squel[0, 1]],
            [self.accel_squel[1, 0], self.accel_squel[1, 1]],
            [self.accel_squel[2, 0], accelmax],
            [(self.accel_squel[2, 0] + self.accel_squel[-2, 0])/2, accelmax], 
            [self.accel_squel[-2, 0], accelmax],
            [self.accel_squel[-1, 0] - 3*np.pi/180/np.sqrt(1+jf**2), -3*np.pi/180*jf/np.sqrt(1+jf**2)], 
            [self.accel_squel[-1, 0], self.accel_squel[-1, 1]]]
            )
        
        weights = np.array([self.accel_squel[0, 2], self.accel_squel[1, 2], self.accel_squel[2, 2], 1, self.accel_squel[-2, 2], 1, self.accel_squel[-1, 2]])
        
        return ctrlpts, weights 
        
class OptimiseLoisDecel():
    def __init__(self, assemblage : AssemblageLinguet, levee_squel, raccord_angle, pas_angulaire_itg = 0.1*unit.DEGREE_TO_RADIAN):
        self.m1 = assemblage.soupape.masse_coupelle + assemblage.soupape.masse_soupape + assemblage.ressort.masse/3
        self.j2 = assemblage.levier.inertie
        self.k = assemblage.ressort.raideur
        self.dr = assemblage.ressort.precharge/assemblage.ressort.raideur
        self.mu_ps = assemblage.frottement_patinsoupape
        self.l_ling = assemblage.levier.longueur  
        self.r_ps = assemblage.levier.patin_soupape.rayon_courbure
        self.z_l = assemblage.coords_levier[2]

        self.leveemax = levee_squel[-1, 1]
        self.duree_decel = levee_squel[-1, 0] - raccord_angle
        self.ac_evalpts = np.arange(0.0, 1.01*self.duree_decel, pas_angulaire_itg)

        self.betamax = cdyn.beta(
            lbd = self.leveemax,
            l_ling = self.l_ling, 
            z_l = self.z_l, 
            r_ps = self.r_ps)
        
    def __call__(self, regime_affolement) -> LoisPhaseDecel:
        
        decel_evalpts = self.compute_decel(regime_affolement)

        a_spl = self.compute_a_spl(-np.flip(self.ac_evalpts), np.flip(decel_evalpts), degree=3)
        
        return LoisPhaseDecel(
            duree_decel = self.duree_decel,
            leveemax = self.leveemax, 
            a_spl = a_spl
        )
    
    def compute_a_spl(self, acs, decels, degree = 3):
        knot_vector, coefficients, degree = scitp.splrep(acs, decels, k=degree)
        return scitp.BSpline(knot_vector, coefficients, degree, extrapolate=True)

    def compute_decel(self, regime_affolement):
        tps_evalpts = -self.ac_evalpts/regime_affolement
        sol = scitg.odeint(
            cdyn.dynamique_mvmt_affolement,
            np.array([self.betamax, 0]),
            tps_evalpts,
            args = (self.m1, self.j2, self.k, self.dr, self.l_ling, self.r_ps, self.z_l, self.mu_ps)
            )
        beta = sol[:,0]
        beta_dot = sol[:,1]
        beta_ddot = cdyn.dynamique_mvmt_affolement(sol.T, None, self.m1, self.j2, self.k, self.dr, self.l_ling, self.r_ps, self.z_l, self.mu_ps)[1]
        lbd_ddot = cdyn.lbd_ddot(beta, beta_dot, beta_ddot, self.l_ling)
        lbd_ddoac = lbd_ddot/(regime_affolement/2)**2
        return lbd_ddoac

class OptimiseLoisDecelV2():
    def __init__(self, assemblage : AssemblageLinguet, levee_squel, pas_angulaire_itg = 0.1*unit.DEGREE_TO_RADIAN):
        self.m1 = assemblage.soupape.masse_coupelle + assemblage.soupape.masse_soupape + assemblage.ressort.masse/3
        self.j2 = assemblage.levier.inertie
        self.k = assemblage.ressort.raideur
        self.dr = assemblage.ressort.precharge/assemblage.ressort.raideur
        self.mu_ps = assemblage.frottement_patinsoupape
        self.l_ling = assemblage.levier.longueur  
        self.r_ps = assemblage.levier.patin_soupape.rayon_courbure
        self.z_l = assemblage.coords_levier[2]

        self.pas_itg = pas_angulaire_itg
        self.leveemax = levee_squel[-1, 1]
        

        self.betamax = cdyn.beta(
            lbd = self.leveemax,
            l_ling = self.l_ling, 
            z_l = self.z_l, 
            r_ps = self.r_ps)
        
    def __call__(self, duree_decel, levee_init, vitesse_init, regime_affolement) -> LoisPhaseDecel:
        ac_evalpts = np.arange(0.0, 1.01*duree_decel, self.pas_itg)
        beta_init = cdyn.beta(
            levee_init,
            self.l_ling,
            self.z_l,
            self.r_ps
        )
        beta_dot_init = cdyn.beta_dot(
            vitesse_init*regime_affolement/2,
            beta_init,
            self.l_ling
        )
        decel_evalpts = self.compute_decel(ac_evalpts, beta_init, beta_dot_init, regime_affolement)

        a_spl = self.compute_a_spl(ac_evalpts, np.flip(decel_evalpts), degree=3)
        
        return LoisPhaseDecelV2(
            duree_decel = duree_decel,
            l_init = levee_init,
            v_init=vitesse_init, 
            a_spl = a_spl
        )
    
    def compute_a_spl(self, acs, decels, degree = 3):
        knot_vector, coefficients, degree = scitp.splrep(acs, decels, k=degree)
        return scitp.BSpline(knot_vector, coefficients, degree, extrapolate=True)

    def compute_decel(self, ac_evalpts, beta_init, beta_dot_init, regime_affolement):
        tps_evalpts = ac_evalpts/regime_affolement
        sol = scitg.odeint(
            cdyn.dynamique_mvmt_affolement,
            np.array([beta_init, beta_dot_init]),
            tps_evalpts,
            args = (self.m1, self.j2, self.k, self.dr, self.l_ling, self.r_ps, self.z_l, self.mu_ps)
            )
        beta = sol[:,0]
        beta_dot = sol[:,1]
        beta_ddot = cdyn.dynamique_mvmt_affolement(sol.T, None, self.m1, self.j2, self.k, self.dr, self.l_ling, self.r_ps, self.z_l, self.mu_ps)[1]
        lbd_ddot = cdyn.lbd_ddot(beta, beta_dot, beta_ddot, self.l_ling)
        lbd_ddoac = lbd_ddot/(regime_affolement/2)**2
        return lbd_ddoac

class CreeDemiLois():
    def __init__(self, assemblage : Assemblage, ouverture = True):
        self.asmb = assemblage
        self.ouverture = ouverture
    
    def __call__(self, 
                regime_affolement_init,
                accel_squelbrut,
                vitesse_squelbrut,
                levee_squelbrut,
                raccord_anglebrut
                ):

        accel_squel, vitesse_squel, levee_squel, raccord_angle, duree_raccord = self.traite_squelettes(
            accel_squelbrut,
            vitesse_squelbrut,
            levee_squelbrut,
            raccord_anglebrut,
            self.ouverture
            )
        
        opt_rampe = OptimiseLoisRampe(
            vitesse_squel = vitesse_squel,
            levee_squel = levee_squel
        )
        opt_accel = OptimiseLoisAccel(
            accel_squel = accel_squel,
            vitesse_squel = vitesse_squel,
            levee_squel = levee_squel
        )
        opt_decel = OptimiseLoisDecel(
            assemblage = self.asmb,
            levee_squel = levee_squel,
            raccord_angle = raccord_angle,
            pas_angulaire_itg = 0.1*unit.DEGREE_TO_RADIAN
            )
        
        loisrampe = opt_rampe()

        amax_opt, wmot_aff_opt = self.optimise(
            accelmax_init = (accel_squel[2, 1] + accel_squel[-2, 1])/2, 
            regime_affolement_init = regime_affolement_init, 
            opt_la = opt_accel, 
            opt_ld = opt_decel, 
            duree_raccord = duree_raccord
        )
        
        loisaccel = opt_accel(accelmax = amax_opt)

        loisdecel = opt_decel(regime_affolement = wmot_aff_opt)

        loisraccord = self.compute_raccord(duree_raccord = duree_raccord, loisaccel = loisaccel, loisdecel = loisdecel)
        
        return DemiLois(
            squelette_acceleration = accel_squel,
            squelette_vitesse = vitesse_squel,
            squelette_levee = levee_squel,
            ac_fin_rampe = vitesse_squelbrut[-1, 0],
            ac_fin_accel = accel_squelbrut[-1, 0],
            ac_leveemax = levee_squelbrut[-1, 0],
            lois_rampe = loisrampe,
            lois_accel = loisaccel,
            lois_raccord = loisraccord,
            lois_decel = loisdecel,
            accelmax_opt = amax_opt,
            regime_affolement_opt = wmot_aff_opt
        )
    
    def optimise(self, accelmax_init, regime_affolement_init, opt_la, opt_ld, duree_raccord):
        sol = sco.root(
            self.opt_func, 
            method="hybr", 
            x0=np.array([accelmax_init, regime_affolement_init]),
            args=(opt_la, opt_ld, duree_raccord))

        if not sol.success :
            raise Exception("L'optimisation n'a pas abouti.")

        return sol.x
    
    def opt_func(self, accelmax_waff, opt_la : OptimiseLoisAccel, opt_ld : OptimiseLoisDecel, duree_raccord : float):
        
        amax, wmot_aff = accelmax_waff
        loisaccel = opt_la(amax)
        loisdecel = opt_ld(wmot_aff)

        loisraccord = self.compute_raccord(duree_raccord=duree_raccord, loisaccel=loisaccel, loisdecel=loisdecel)

        levee_fin_apos = loisaccel.l(loisaccel.duree_accel)
        vitesse_fin_apos = loisaccel.v(loisaccel.duree_accel)

        levee_debut_decel = (
            loisraccord.l_spl(-duree_raccord) 
            - (loisraccord.vitesse_init - loisraccord.v_spl(0))*duree_raccord 
            + loisraccord.levee_init - loisraccord.l_spl(0)
            )
        vitesse_debut_decel = (
            loisraccord.v_spl(-duree_raccord) 
            + loisraccord.vitesse_init 
            - loisraccord.v_spl(0)
            )
        
        discontinuite_vitesse = vitesse_fin_apos - vitesse_debut_decel
        discontinuite_levee = levee_debut_decel - levee_fin_apos

        return np.array([discontinuite_vitesse, discontinuite_levee])
        
    def compute_raccord(self, duree_raccord : float, loisaccel : LoisPhaseAccel, loisdecel : LoisPhaseDecel) -> LoisPhaseRaccord:
        ai = loisdecel.a_spl(-loisdecel.duree_decel)
        ji = loisdecel.j_spl(-loisdecel.duree_decel)
        jf = loisaccel.j_spl(loisaccel.duree_accel)

        calculraccord = CalculRaccord(
            duree_raccord=duree_raccord,
            accel_init=ai,
            jerk_init=ji,
            accel_final=0,
            jerk_final=jf
        )
        return LoisPhaseRaccord(
            duree_raccord=duree_raccord,
            levee_init=loisdecel.l(-loisdecel.duree_decel),
            vitesse_init=loisdecel.v(-loisdecel.duree_decel),
            a_spl = calculraccord.a_spl
        )

    @classmethod
    def traite_squelettes(cls, 
        accel_squelbrut,
        vitesse_squelbrut,
        levee_squelbrut,
        raccord_anglebrut,
        ouverture = True
        ):
        

        if ouverture :
            accel_squel = accel_squelbrut - np.meshgrid(np.array([vitesse_squelbrut[-1, 0], 0, 0]), np.ones(len(accel_squelbrut)))[0]
            vitesse_squel = vitesse_squelbrut
            levee_squel = levee_squelbrut
            raccord_angle = raccord_anglebrut
            duree_raccord = raccord_anglebrut - accel_squelbrut[-1, 0]
        
        else :
            accel_squel_decale = np.column_stack((-accel_squelbrut[:,0] + vitesse_squelbrut[0,0], accel_squelbrut[:,1:]))
            accel_squel = np.flip(accel_squel_decale, axis = 0) 

            vitesse_squel_decale = np.column_stack((-vitesse_squelbrut[:,0] + levee_squelbrut[-1,0], -vitesse_squelbrut[:,1]))
            vitesse_squel = np.flip(vitesse_squel_decale, axis = 0)

            levee_squel_decale = np.column_stack((-levee_squelbrut[:,0] + levee_squelbrut[-1,0], levee_squelbrut[:,1]))
            levee_squel = np.flip(levee_squel_decale, axis = 0)

            raccord_angle = levee_squelbrut[-1, 0] - raccord_anglebrut
            duree_raccord = - raccord_anglebrut + accel_squelbrut[0, 0]
        
        return accel_squel, vitesse_squel, levee_squel, raccord_angle, duree_raccord
    
class CreeLois():
    def __init__(self, assemblage : Assemblage):
        self.asmb = assemblage   
    
    def __call__(self, symetrie : bool, regime_affolement_init,
            accel_squelbrut_ouverture, accel_squelbrut_fermeture,
            vitesse_squelbrut_ouverture, vitesse_squelbrut_fermeture, 
            levee_squelbrut_ouverture, levee_squelbrut_fermeture,
            raccord_anglebrut_ouverture, raccord_anglebrut_fermeture
        ) -> LoisCame :
        
        dac_leveemax_ouverture = levee_squelbrut_ouverture[-1,0] - levee_squelbrut_ouverture[0,0]
        dac_leveemax_fermeture = levee_squelbrut_fermeture[-1,0] - levee_squelbrut_fermeture[0,0]

        cdl_ouverture = CreeDemiLois(self.asmb, ouverture = True)

        demilois_ouverture = cdl_ouverture(
            regime_affolement_init = regime_affolement_init, 
            accel_squelbrut = accel_squelbrut_ouverture,
            vitesse_squelbrut = vitesse_squelbrut_ouverture,
            levee_squelbrut = levee_squelbrut_ouverture,
            raccord_anglebrut = raccord_anglebrut_ouverture
            )
        
        if symetrie :
            demilois_fermeture = demilois_ouverture
        else :
            cdl_fermeture = CreeDemiLois(self.asmb, ouverture = False)
            demilois_fermeture = cdl_fermeture(
                regime_affolement_init = regime_affolement_init,
                accel_squelbrut = accel_squelbrut_fermeture,
                vitesse_squelbrut = vitesse_squelbrut_fermeture,
                levee_squelbrut = levee_squelbrut_fermeture,
                raccord_anglebrut = raccord_anglebrut_fermeture
                )

        return LoisCame(
            symetrie = symetrie,
            demilois_ouverture = demilois_ouverture,
            demilois_fermeture = demilois_fermeture,
            dac_leveemax_ouverture = dac_leveemax_ouverture,
            dac_leveemax_fermeture = dac_leveemax_fermeture
        )

class CalculLoisReelles():
    def __init__(self, controller : ControllerInterface):
        self.laws = controller.current_laws
    
    def calcul_angles_attaque(self, jeu : float = 0.0):
        angle_rampe_ouverture = self.laws.demilois_ouverture.ac_fin_rampe
        levee_rampe_ouverture = self.laws.demilois_ouverture.lois_accel.levee_rampe
        vitesse_rampe_ouverture = self.laws.demilois_ouverture.lois_accel.vitesse_rampe

        angle_rampe_fermeture = self.laws.dac_leveemax_ouverture + self.laws.dac_leveemax_ouverture - self.laws.demilois_fermeture.ac_fin_rampe
        levee_rampe_fermeture = self.laws.demilois_fermeture.lois_accel.levee_rampe
        vitesse_rampe_fermeture = -self.laws.demilois_fermeture.lois_accel.vitesse_rampe

        angle_attaque_ouverture = (jeu - levee_rampe_ouverture) / vitesse_rampe_ouverture + angle_rampe_ouverture
        angle_attaque_fermeture = (jeu - levee_rampe_fermeture) / vitesse_rampe_fermeture + angle_rampe_fermeture

        return angle_attaque_ouverture, angle_attaque_fermeture
    
    def calcul_ouverture(self, jeu : float = 0.0):
        angle_attaque_ouverture, angle_attaque_fermeture = self.calcul_angles_attaque(jeu)

        return angle_attaque_fermeture - angle_attaque_ouverture

    def levee_reelle(self, angles, jeu):
        return self.laws.l(angles) - jeu

    def __call__(self, angles : np.ndarray, jeu : float = 0.0):
    
        angles_1d = np.atleast_1d(angles)

        angles_attaque = self.calcul_angles_attaque(jeu)
        partieactive = np.where((angles_attaque[0] < angles_1d) & (angles_1d < angles_attaque[1]))

        angles_actif = angles_1d[partieactive]

        return angles_actif, self.laws.a(angles_actif), self.laws.v(angles_actif), self.levee_reelle(angles_actif, jeu)
    
class CalculEfficacite():
    def __init__(self, controller : ControllerInterface):
        self.laws = controller.current_laws
        self.calcloisrelles = CalculLoisReelles(controller)

    def calcul_aire_reelle(self, jeu):
        ac_attaque_ouverture, ac_attaque_fermeture = self.calcloisrelles.calcul_angles_attaque(jeu)
        
        return scitg.quad(self.calcloisrelles.levee_reelle, ac_attaque_ouverture, ac_attaque_fermeture, args=(jeu,))[0]
    
    def __call__(self, jeu : float = 0.0):

        ac_attaque_ouverture, ac_attaque_fermeture = self.calcloisrelles.calcul_angles_attaque(jeu)
        
        aire_ideale = (ac_attaque_fermeture - ac_attaque_ouverture)*(self.laws.demilois_ouverture.squelette_levee[-1, 1] - jeu)

        aire_reelle, err = scitg.quad(self.calcloisrelles.levee_reelle, ac_attaque_ouverture, ac_attaque_fermeture, args=(jeu,))
        
        return aire_reelle /aire_ideale

class CalculLoisReellesV2():
    def __init__(self, lois : LoisCame):
        self.laws = lois
    
    def calcul_angles_attaque(self, jeu : float = 0.0):
        angle_rampe_ouverture = self.laws.demilois_ouverture.ac_fin_rampe
        levee_rampe_ouverture = self.laws.demilois_ouverture.lois_accel.levee_rampe
        vitesse_rampe_ouverture = self.laws.demilois_ouverture.lois_accel.vitesse_rampe

        angle_rampe_fermeture = self.laws.dac_leveemax_ouverture + self.laws.dac_leveemax_ouverture - self.laws.demilois_fermeture.ac_fin_rampe
        levee_rampe_fermeture = self.laws.demilois_fermeture.lois_accel.levee_rampe
        vitesse_rampe_fermeture = -self.laws.demilois_fermeture.lois_accel.vitesse_rampe

        angle_attaque_ouverture = (jeu - levee_rampe_ouverture) / vitesse_rampe_ouverture + angle_rampe_ouverture
        angle_attaque_fermeture = (jeu - levee_rampe_fermeture) / vitesse_rampe_fermeture + angle_rampe_fermeture

        return angle_attaque_ouverture, angle_attaque_fermeture

    def calcul_ouverture(self, jeu : float = 0.0):
        angle_attaque_ouverture, angle_attaque_fermeture = self.calcul_angles_attaque(jeu)

        return angle_attaque_fermeture - angle_attaque_ouverture

    def levee_reelle(self, angles, jeu):
        return self.laws.l(angles) - jeu

    def __call__(self, angles : np.ndarray, jeu : float = 0.0):
    
        angles_1d = np.atleast_1d(angles)

        angles_attaque = self.calcul_angles_attaque(jeu)
        partieactive = np.where((angles_attaque[0] < angles_1d) & (angles_1d < angles_attaque[1]))

        angles_actif = angles_1d[partieactive]

        return angles_actif, self.laws.a(angles_actif), self.laws.v(angles_actif), self.levee_reelle(angles_actif, jeu)

class CalculEfficaciteV2():
    def __init__(self, lois : LoisCame, calculloisrelle : CalculLoisReellesV2):
        self.laws = lois
        self.calcloisrelles = calculloisrelle

    def calcul_aire_reelle(self, jeu):
        ac_attaque_ouverture, ac_attaque_fermeture = self.calcloisrelles.calcul_angles_attaque(jeu)
        
        return scitg.quad(self.calcloisrelles.levee_reelle, ac_attaque_ouverture, ac_attaque_fermeture, args=(jeu,))[0]
    
    def __call__(self, jeu : float = 0.0):

        ac_attaque_ouverture, ac_attaque_fermeture = self.calcloisrelles.calcul_angles_attaque(jeu)
        
        aire_ideale = (ac_attaque_fermeture - ac_attaque_ouverture)*(self.laws.demilois_ouverture.squelette_levee[-1, 1] - jeu)

        aire_reelle, err = scitg.quad(self.calcloisrelles.levee_reelle, ac_attaque_ouverture, ac_attaque_fermeture, args=(jeu,))
        
        return aire_reelle /aire_ideale

if __name__=="__main__":  
    pass