import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from geomdl import NURBS
import numpy as np
import scipy.integrate as scitg
import scipy.interpolate as scitp
import scipy.optimize as sco

import domain.services.unitees as unit
import domain.services.calculsdynamique as cdyn
from domain.services.calculsloiscame import CalculRampe, CalculRaccord
from domain.entities.loiscame import LoisPhaseRampe, LoisPhaseAccel, LoisPhaseRaccord, LoisPhaseDecel, LoisPhaseDecelV2, DemiLois, LoisCame
from domain.entities.assemblage import Assemblage, AssemblageLinguet, AssemblageDirecte
from application.interfaces.controller_interface import ControllerInterface

class OptimiseLoisRampe():
    """Crée une instance de LoisPhaseRampe, qui représente la phase de rampe, en fonction des squelettes renseignés.

    Dans les faits, aucun ajustement n'est réalisé sur la phase de rampe. Le nom de cette classe est donc mal choisi.

    Attributes:
        duree_rampe (float): Durée totale de la rampe.
        duree_vitesse_constante (float): Durée de la phase à vitesse constante.
        vitesse_rampe (float): Vitesse durant la phase à vitesse constante.
        levee_rampe (float): Levée en fin de rampe.

    Args:
        vitesse_squel (np.ndarray): Squelette de vitesse.
        levee_squel (np.ndarray): Squelette de levée.

    Methods:
        __call__() -> LoisPhaseRampe:
            Crée une instance de LoisPhaseRampe correspondant aux squelettes renseignés.

    Returns:
        LoisPhaseRampe: Une instance de LoisPhaseRampe représentant les lois de distributions pour la phase de rampe.
    """
    def __init__(self, vitesse_squel, levee_squel):
        self.duree_rampe = vitesse_squel[-1, 0] - vitesse_squel[0, 0]
        self.duree_vitesse_constante = vitesse_squel[-1, 0] - vitesse_squel[-2, 0]
        self.vitesse_rampe = vitesse_squel[-1, 1]
        self.levee_rampe = levee_squel[1, 1]

    def __call__(self) -> LoisPhaseRampe:
        """Crée une instance de LoisPhaseRampe pour les squelettes renseignés.
        
        Cette méthode utilise les squelettes de vitesse et d'acélération pour créer d'abord une instance de CalculRampe puis une instance de LoisPhaseRampe. La rampe est plutôt simple à modéliser, une phase définie par un polynôme de degré 7 et une phase à vitesse constante. Cette rampe est fixe et ne subit pas d'optimisation.

        Returns:
            LoisPhaseRampe: Une instance de LoisPhaseRampe représentant la phase de rampe.
        """
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
    """Utilitaire permettant de créer la loi d'accélération positive en fonction de l'accélération maximale et du squelette.
    
    Cette classe est un utilitaire qui permet de créer la phase d'accélération positive en fonction de l'accélération maximale. Son nom est sûrement mal choisi car aucune "optimisation" n'est réalisée dans cette classe. Néanmoins, elle fut appelée ainsi car elle est utilisée par la classe CreeDemiLois pour réaliser l'ajustement des demi-lois.

    Args:
        accel_squel (np.ndarray): Squelette d'accélération.
        vitesse_squel (np.ndarray): Squelette de vitesse.
        levee_squel (np.ndarray): Squelette de levée.

    Attributes:
        duree_accel (float): Durée de la phase d'accélération positive.
        vitesse_rampe (float): Vitesse en fin de rampe.
        levee_rampe (float): Levée en fin de rampe.
        accel_squel (np.ndarray): Squelette d'accélération.

    Methods:
        __call__(accelmax: float) -> LoisPhaseAccel:
            Crée une instance de LoisPhaseAccel correspondant à l'accélération maximale renseignée.
        compute_a_spl(ctrlpts: np.ndarray, poids: np.ndarray, degree: int=3, delta: float=1e-4) -> scitp.BSpline:
            Interpole l'accélération de la phase d'accélération positive par une B-Spline.
        compute_ctrlpts(accelmax: float=None) -> tuple[np.ndarray, np.ndarray]:
            Calcule les points de contrôle.

    Returns:
        LoisPhaseAccel: Une instance de LoisPhaseAccel répsentant la phase d'accélération positive.
    """
    def __init__(self, accel_squel, vitesse_squel, levee_squel):
        self.duree_accel = accel_squel[-1,0]
        self.vitesse_rampe = vitesse_squel[-1, 1]
        self.levee_rampe = levee_squel[1, 1]
        self.accel_squel = accel_squel

    def __call__(self, accelmax: float) -> LoisPhaseAccel:
        """Crée une instance de LoisPhaseAccel qui corresponde à l'accélération maximale renseignée. 
    
        Cette méthode crée d'abord des points de contrôle avec des poids associés. Ces points de contrôle sont ensuite interpolés par un spline de type NURBS.

        Args:
            accelmax (float): Accélération maximale pour laquelle est calculée la phase d'accélération positive.

        Returns:
            LoisPhaseAccel: Instance de LoisPhaseAccel représentant la phase d'accélération positive.
        """
        ctrlpts, weights = self.compute_ctrlpts(accelmax)
        a_spl = self.compute_a_spl(ctrlpts, weights, degree=3)
        
        return LoisPhaseAccel(
            duree_accel = self.duree_accel,
            vitesse_rampe = self.vitesse_rampe,
            levee_rampe = self.levee_rampe,
            a_spl = a_spl
        )
    
    def compute_a_spl(self, ctrlpts: np.ndarray, poids: np.ndarray, degree: int= 3, delta: float= 1e-4) -> scitp.BSpline:
        """Crée la spline représentant l'accélération de la phase d'accélération positive.

        Cette méthode passe par l'utilisation de NURBS qui sont un type spécifique de splines permettant de définir un poids. Un module spécifique a été utilisé pour calculer ces NURBS. Afin de se ramener à une spline du module scipy.interpolate, la spline de type NURBS est ensuite interpolé par une B-Spline. En effet, d'une part les scitp.BSpline sont plus simples à utilisées et, d'autre part, cela permet de créer une certaine cohérence dans le logiciel.

        Args:
            ctrlpts (np.ndarray): Points de contrôle de la spline de type NURBS.
            poids (np.ndarray): Poids associés aux points de contrôle.
            degree (int): Degré de la spline (3 par défaut).
            delta (float): Précision sur la spline (1e-4 par défaut). Attention si la précision est trop grande (i.e. delta trop petit) le temps de calcul deviendra très long.

        Returns:
            scitp.BSpline: Accélération pour la phase d'accélération positive. Cette accélération est interpolée par une B-Spline.
        """
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
    
    def compute_ctrlpts(self, accelmax: float= None) -> tuple[np.ndarray, np.ndarray]:
        """Calcule les points de contrôle qui seront interpolés par la NURBS.

        Cette méthode calcule les points de contrôle de la spline et les poids associés pour pourvoir utiliser un spline de type NURBS. Les points de contrôle sont principalement ceux définis par le squelette d'accélération. Les deux point d'acclération non nulle du squelette sont ajustés pour correspondre à l'accélération maximale. Des points de contrôle sont ajoutés contrôler la valeur de la dérivée de la lois au point de levée maximale et en fin de phase d'accélération positive. La dérivée en fin de phase d'accélération positive est la pente de la dernière branche du squelette d'accélération pour cette phase.

        Args:
            accelmax (float, optional): L'accélération maximale. 
                                        Si aucune accélération n'est renseignée, celle-ci est calculée suivant le squelette initial.

        Returns:
            tuple[np.ndarray, np.ndarray]: A tuple containing:
                - ctrlpts (np.ndarray): Array contenant les points de contrôle.
                - weights (np.ndarray): Poids associés au points de contrôle.
        """
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
    """Utilitaire permettant de créer la loi de décélération à la limite de l'affolement en fonction du régime d'affolement.

    Cette classe est un utilitaire qui permet de créer la phase de décélération à la limite de l'affolement en fonction du régime d'affolement. Son nom est sûrement mal choisi car aucune "optimisation" n'est réalisée dans cette classe. Néanmoins elle fut appelée ainsi car elle est utilisée par la classe CreeDemiLois pour réaliser l'ajustement des demi-lois.

    Args:
        assemblage (AssemblageLinguet): L'assemblage étudié.
        levee_squel (np.ndarray): Squelette de levée.
        raccord_angle (float): Angle de rotation de la came pour lequel le raccord rejoint la décélération à la limite de l'affolement.
        pas_angulaire_itg (float): Pas angulaire d'intégration de l'équation différentielle (Par défault ce pas est de 0.1 degrées). Ce pas est exprimé en radians.

    Attributes:
        m1 (float): Masse de l'ensemble cinématique lié à la soupape.
        j2 (float): Inertie du levier.
        k (float): Raideur du ressort.
        dr (float): Précharge / Raideur du ressort = Différence entre la longueur à vide et la longueur à levée et jeu nul.
        mu_ps (float): Coefficient de frottement dynamique entre la soupape et son patin.
        l_ling (float): Longueur du levier. De son centre de rotation au centre de rotation du patin côté soupape.
        r_ps (float): Rayon de courbure du patin côté soupape.
        z_l (float): Coordonnée selon z1 du centre de rotation du linguet dans le repère (O, x, y1, z1).
        leveemax (float): Levée maximale souhaitée pour un jeu nul.
        duree_decel (float): Durée de la phase de décélération à la limite de l'affolement.
        ac_evalpts (np.ndarray): Angles de rotation de la came pour lesquels sont calculés la décélération.
        betamax (float): Angle d'inclinaison du linguet à la levée maximale.

    Methods:
        __call__(regime_affolement: float) -> LoisPhaseDecel:
            Crée la loi de décélération pour le regime d'affolement renseigné.
        compute_a_spl(acs: np.ndarray, decels: np.ndarray, degree=3) -> scipy.interpolate.BSpline:
            Interpole la phase de décélération à la limite de l'affolement par une B-Spline.
        compute_decel(regime_affolement: float) -> np.ndarray:
            Calcule la décélération à la limite de l'affolement pour les angles de rotation de la came définis en attributs.

    Returns:
        LoisPhaseDecel: Une instance de LoisPhaseDecel représentant la décélération à la limite de l'affolement.
    """
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
        
    def __call__(self, regime_affolement: float) -> LoisPhaseDecel:
        """Crée une instance de LoisPhaseDecel pour le régime d'affolement renseigné.

        Cette méthode calcule d'abord les décélérations aux angles de rotation de la came définis comme attributs. Ces angles de rotation dépendent du pas angulaire choisi. Les décélérations sont calculées en résolvant l'équation du mouvement à l'affolement avec pour conditions initiales la levée maximale et une vitesse nulle. La fonction odeint de scipy.integrate est utilisée pour intégrer l'équation du mouvement. Cette fonction utilise une méthode d'Adams-BDF pour la résolution de l'équation différentielle.

        Args:
            regime_affolement (float): Régime d'affolement pour lequel est caculé la décélération.

        Returns:
            LoisPhaseDecel: Une instance de LoisPhaseDecel représentant la décélération à la limite de l'affolement.
        """
        decel_evalpts = self.compute_decel(regime_affolement)

        a_spl = self.compute_a_spl(-np.flip(self.ac_evalpts), np.flip(decel_evalpts), degree=3)
        
        return LoisPhaseDecel(
            duree_decel = self.duree_decel,
            leveemax = self.leveemax, 
            a_spl = a_spl
        )
    
    def compute_a_spl(self, acs: np.ndarray, decels: np.ndarray, degree:int =3) -> scitp.BSpline:
        """Interpole la phase de décélération par une B-Spline.

        Cette méthode utilise les résultats issus de la résolution de l'équation du mouvement du système à l'affolement.

        Args:
            acs (np.ndarray): Angles de rotation de came des points à interpoler.
            decels (np.ndarray): Décélération correspondantes aux angles des points à interpoler.
            degree (int): Degré de la BSplien (3 par défaut, spline cubique).

        Returns:
            scitp.BSpline: A B-spline object representing the acceleration profile.

        Raises:
            None: This method does not raise exceptions but relies on the input arrays to be valid.
        """
        knot_vector, coefficients, degree = scitp.splrep(acs, decels, k=degree)
        return scitp.BSpline(knot_vector, coefficients, degree, extrapolate=True)


    def compute_decel(self, regime_affolement: float) -> np.ndarray:
        """Calcule la décélération pour les angles définis en attributs.
        
        Cette méthode calcule la décélération pour les angles définis en attributs, ac_evalpts. Pour cela l'équation du mouvement est résolue avec le point de levée maximale comme condition initiale (levée maximale, vitesse nulle).

        Args:
            regime_affolement (float): Le régime d'affolement pour lequel est calculé la décélération.

        Returns:
            np.ndarray: Un vecteur contenant les décélérations pour chacun des angles ac_evalpts.
        """
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
    """Cette classe a pour objectif de proposer une autre stratégie l'ajustement de la phase de décélération. Une stratégie qui ne soit pas basée sur le régime d'affolement. Cette classe n'a pas été implémentée par faute de temps. On pourrait imaginer une stratégie faisant varier l'ouverture."""
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
    """Classe représentant le cas d'usage "Création des demis-lois de distribution". 

    Args:
        assemblage (Assemblage): L'assemblage étudié et précédemment défini.
        ouverture (bool): Indique si la demi-loi créée est une demi-loi d'ouverture ou de fermeture. True = Ouverture, False = Fermeture.

    Attributes:
        asmb (Assemblage): L'assemblage étudié et précédemment défini.
        ouverture (bool): Indique si la demi-loi créée est une demi-loi d'ouverture ou de fermeture. True = Ouverture, False = Fermeture.

    Methods:
        __call__(symetrie: bool, regime_affolement_init: float, accel_squelbrut: np.ndarray, vitesse_squelbrut: np.ndarray, levee_squelbrut: np.ndarray, raccord_anglebrut: float) -> LoisCame: 
            Crée une demi-loi à partir des squelettes bruts.
        optimise(accelmax_init: float, regime_affolement_init: float, opt_la: OptimiseLoisAccel, opt_ld: OptimiseLoisDecel, duree_raccord: float) -> np.ndarray: 
            Ajuste les paramètres de la demi-loi pour assurer la continuité en levée et en vitesse.
        opt_func(accelmax_waff: np.ndarray, opt_la : OptimiseLoisAccel, opt_ld : OptimiseLoisDecel, duree_raccord : float) -> np.ndarray: 
            La fonction à optimiser.
        compute_raccord(duree_raccord : float, loisaccel : LoisPhaseAccel, loisdecel : LoisPhaseDecel) -> LoisPhaseRaccord:
            Crée une instance de LoisPhaseRaccord qui relie les instance de LoisPhaseAccel et LoisPhaseDecel renseignées.
        traite_squelettes(accel_squelbrut: np.ndarray, vitesse_squelbrut: np.ndarray, levee_squelbrut: np.ndarray, raccord_anglebrut: float, ouverture: bool= True) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
            Traite les squelettes bruts pour les rendre exploitables par les fonctions d'optimisation. 
        
    Returns:
        DemiLois: Une instance de DemiLois.
    """
    def __init__(self, assemblage : Assemblage, ouverture = True):
        self.asmb = assemblage
        self.ouverture = ouverture
    
    def __call__(self, 
                regime_affolement_init: float,
                accel_squelbrut: np.ndarray,
                vitesse_squelbrut: np.ndarray,
                levee_squelbrut: np.ndarray,
                raccord_anglebrut: float
                ) -> DemiLois:
        """Crée une instance de DemiLois à partir des squelettes bruts. 

        Cette méthode applique d'abord un traitement aux squelettes bruts pour les rendre exploitables. Ensuite des utilitaires de création des phases de rampe, d'accélération positive et de décélération à la limite de l'affolement sont créée. Grâce à ces derniers, un raccord est créé et les paramètres des différentes phases sont ajustés afin d'assurer la continuité en vitesse et en levée. Enfin la demi-loi finale est créée.

        Args:
            regime_affolement_init (float): Régime d'affolement pour l'initialisation de l'optimisation.
            accel_squelbrut (np.ndarray): Squelette d'accélération "brut".
            vitesse_squelbrut (np.ndarray): Squelette de vitesse "brut".
            levee_squelbrut (np.ndarray): Squelette de levée "brut".
            raccord_anglebrut (float): Angle de rotation de la came pour lequel le raccord rejoint la décélération à la limite de l'affolement.

        Returns:
            DemiLois: Une instance de DemiLois correspondant au squelette renseigné.

        Raises:
            Exception: Génère une erreur si l'optimisation n'a pas aboutie.
        """
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
    
    def optimise(self, accelmax_init: float, regime_affolement_init: float, opt_la: OptimiseLoisAccel, opt_ld: OptimiseLoisDecel, duree_raccord: float) -> np.ndarray:
        """Ajuste l'accélération maximale et le régime d'affolement pour qu'il y ait continuité en vitesse et en levée.

        Pour réaliser cette optimisation, on utilise la fonction root de scipy.optimize. Cette fonction permet de trouver les racines d'une fonction vectorielle. La fonction vectorielle dont nous cherchons les racines est celle qui retourne la valeur de la discontinuité en vitesse et la valeur de la discontinuité en levée.

        Args:
            accelmax_init (float): Accélération maximale pour l'initialisation de l'ajustement.
            regime_affolement_init (float): Régime d'affolement pour l'initialisation de l'ajustement.
            opt_la (OptimiseLoisAccel): Une instance de OptimiseLoisAccel qui permet de calculer l'accélération positive en fonction de l'accélération maximale.
            opt_ld (OptimiseLoisDecel): Une instance de OptimiseLoisAccel qui permet de calculer la décélération à la limite de l'affolement en fonction du régime d'affolement.
            duree_raccord (float): Durée de la phase de raccord.

        Returns:
            np.ndarray: Un vecteur contenant l'accélération et le régime d'affolement permettant de respecter les continuités.

        Raises:
            Exception: Retourne une erreur si l'algorithme d'optimisation ne converge pas.
        """
        sol = sco.root(
            self.opt_func, 
            method="hybr", 
            x0=np.array([accelmax_init, regime_affolement_init]),
            args=(opt_la, opt_ld, duree_raccord))

        if not sol.success :
            raise Exception("L'optimisation n'a pas abouti.")

        return sol.x
    
    def opt_func(self, accelmax_waff: np.ndarray, opt_la : OptimiseLoisAccel, opt_ld : OptimiseLoisDecel, duree_raccord : float) -> np.ndarray:
        """Calcule les discontinuités en vitesse et levée à partir de l'accélération maximale et du régime d'affolement.

        Cette fonction évalue les discontinuités en vitesse et levée à partir de l'accélération maximale et du régime d'affolement. C'est la fonction dont on cherche les racines pour réaliser l'ajustement.

        Args:
            accelmax_waff (np.ndarray): Un vecteur contenant l'accélération maximale et le régime d'affolement.
            opt_la (OptimiseLoisAccel): Une instance de OptimiseLoisAccel qui permet de calculer l'accélération positive en fonction de l'accélération maximale.
            opt_ld (OptimiseLoisDecel): opt_ld (OptimiseLoisDecel): Une instance de OptimiseLoisAccel qui permet de calculer la décélération à la limite de l'affolement en fonction du régime d'affolement.
            duree_raccord (float): Durée de la phase de raccord.

        Returns:
            np.ndarray: Vecteur contenant les discontinuités en vitesse et en levée.
        """
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
        """Crée le raccord qui permet de relier les phases d'accélération positive et de décélération à la limite de l'affolement.

        Cette fonction utilise l'utilitaire de calcul du raccord implémenté dans domain.services.calculsloiscame.

        Args:
            duree_raccord (float): Durée de la phase de raccord.
            loisaccel (LoisPhaseAccel): Instance de LoisPhaseAccel représentant la phase d'accélération positive.
            loisdecel (LoisPhaseDecel): Instance de LoisPhaseDecel représentant la phase de décélération à la limite de l'affolement.

        Returns:
            LoisPhaseRaccord: Une instance de LoisPhaseRaccord représentant le raccord.
        """
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
        accel_squelbrut: np.ndarray,
        vitesse_squelbrut: np.ndarray,
        levee_squelbrut: np.ndarray,
        raccord_anglebrut: float,
        ouverture: bool= True
        ) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
        """Traite les squelettes bruts pour les rendres exploitables par les fonction d'ajustement et de création des phases.

        Cette méthode de classe traite les squelettes bruts pour les rendre exploitable ensuite. Ce traitement consiste à diviser les squelettes suivant les phases qu'ils représentent, à les translater les squelettes pour qu'ils commencent à un angle nul et à calculer la durée du raccord. Si les squelettes renseignés sont des squelettes de fermeture, alors ces derniers sont également symétrisés. 

        Args:
            accel_squelbrut (np.ndarray): Squelette d'accélération "brut".
            vitesse_squelbrut (np.ndarray): Squelette de vitesse "brut".
            levee_squelbrut (np.ndarray): Squelette de levée "brut".
            raccord_anglebrut (float): Angle de rotation de la came pour lequel le raccord rejoint la décélération à la limite de l'affolement.
            ouverture (bool): Indique si les squelettes bruts renseignés sont des squelettes d'ouverture. True= Ouverture, False= Fermeture (default is True).

        Returns:
            tuple[np.ndarray, np.ndarray, np.ndarray, float]: Un tuple contenant les squelettes ajustés de l'accélération, de la vitesse et de la levée ainsi que l'angle de raccord et la durée du raccord.

        """

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
    """Classe représentant le cas d'usage "Création des lois de distribution". 

    Args:
        assemblage (Assemblage): L'assemblage étudié et précédemment défini.

    Methods:
        __call__(symetrie: bool, regime_affolement_init: float, 
                accel_squelbrut_ouverture: np.ndarray, 
                accel_squelbrut_fermeture: np.ndarray, 
                vitesse_squelbrut_ouverture: np.ndarray, 
                vitesse_squelbrut_fermeture: np.ndarray, 
                levee_squelbrut_ouverture: np.ndarray, 
                levee_squelbrut_fermeture: np.ndarray, 
                raccord_anglebrut_ouverture: float, 
                raccord_anglebrut_fermeture: float) -> LoisCame:
            Crée les lois de distribution à partir des squelettes.

    Returns:
        LoisCame: Une instance de LoisCame.
    """
    def __init__(self, assemblage : Assemblage):
        self.asmb = assemblage   
    
    def __call__(self, symetrie: bool, regime_affolement_init: float,
            accel_squelbrut_ouverture: np.ndarray, accel_squelbrut_fermeture: np.ndarray,
            vitesse_squelbrut_ouverture: np.ndarray, vitesse_squelbrut_fermeture: np.ndarray, 
            levee_squelbrut_ouverture: np.ndarray, levee_squelbrut_fermeture: np.ndarray,
            raccord_anglebrut_ouverture: float, raccord_anglebrut_fermeture: float
        ) -> LoisCame :
        """Crée une instance de l'objet LoisCame à partir des squelette renseignés par l'utilisateur. 
        
        Pour créer une instance de LoisCame, la méthode crée d'abord deux instances de DemiLois, une pour l'ouverture et une pour la fermeture. Ces DemiLois sont ensuite assemblée pour former la lois finale. Si la loi est symétrique, une seule instance de DemiLois est créée, celle associée aux squelettes d'ouverture. Les squelettes sont qualifiés de "brut". En effet ce sont ceux renseignés par l'utilisateur dans l'interface graphique. Ils subiront ensuite un petit traitement pour pouvoir isoler les différentes phases (rampe, accélération positive, ...).

        Args:
            symetrie (bool): Indique si la loi est symétrique ou non. True = Loi symétrique, False = Loi asymétrique.
            regime_affolement_init (float): Régime d'affolement pour l'initialisation de l'optimisation.
            accel_squelbrut_ouverture (np.ndarray): Squelette d'accélération "brut" pour l'ouverture.
            accel_squelbrut_fermeture (np.ndarray): Squelette d'accélération "brut" pour la fermeture.
            vitesse_squelbrut_ouverture (np.ndarray): Squelette de vitesse "brut" pour l'ouverture.
            vitesse_squelbrut_fermeture (np.ndarray): Squelette de vitesse "brut" pour la fermeture.
            levee_squelbrut_ouverture (np.ndarray): Squelette de levée "brut" pour l'ouverture.
            levee_squelbrut_fermeture (np.ndarray): Squelette de levée "brut" pour la fermeture.
            raccord_anglebrut_ouverture (float): Angle de rotation de la came où a lieu le raccord avec la phase de décélération à la limite de l'affolement, pour l'ouverture.
            raccord_anglebrut_fermeture (float): Angle de rotation de la came où a lieu le raccord avec la phase de décélération à la limite de l'affolement, pour la fermeture.

        Returns:
            LoisCame: Une instance de LoisCame correspondant au squelette renseigné.
        """
        
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
    """Classe représentant le cas d'usage "Calcul des lois réelles pour le jeu indiqué".

    Cette classe permet également le calcul de l'ouverture de la lois.

    Args:
        controller (ControllerInterface): Contrôleur de l'application.

    Attributes:
        laws (object): Les lois chargées dans le logiciel. Ces lois sont celles sur lesquelle on travaille.

    Methods:
        __call__(angles: np.ndarray, jeu: float = 0.0) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
            Calcule les lois réelles pour un ensemble d'angles donné et pour un jeu particulier.
        calcul_angles_attaque(jeu: float = 0.0) -> tuple[float, float]:
            Calcule les angles d'attaque pour l'ouverture et la fermeture.
        calcul_ouverture(jeu: float = 0.0) -> float:
            Calcule l'ouverture pour un jeu donné.
        levee_reelle(angles: np.ndarray, jeu: float) -> np.ndarray:
            Calcule la levée réelle pour le jeu renseigné et pour un ensemble d'angles donnés.
    """
    def __init__(self, controller : ControllerInterface):
        self.laws = controller.current_laws

    def __call__(self, angles : np.ndarray, jeu : float = 0.0) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Calcule les lois réelles pour un ensemble d'angles et pour un jeu donnés.

        Cette méthode calcule les lois réelles pour un ensemble d'angles et pour un jeu donnés. Tout d'abord, la fonction restreint le calcul aux angles se trouvant entre les angles d'attaque. Ensuite les nouvelles lois sont calculées.

        Args:
            angles (np.ndarray): Angles de rotation de la came pour lesquels on souhaite connaitre les lois réelles.
            jeu (float, optional): Jeu choisi dans le système.

        Returns:
            tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: Angles se trouvant entre les angles d'attaque, accélération pour ces angles, vitesse pour ces angles et levée réelle pour ces angles. 
            and the real lift values.
        """
        angles_1d = np.atleast_1d(angles)

        angles_attaque = self.calcul_angles_attaque(jeu)
        partieactive = np.where((angles_attaque[0] < angles_1d) & (angles_1d < angles_attaque[1]))

        angles_actif = angles_1d[partieactive]

        return angles_actif, self.laws.a(angles_actif), self.laws.v(angles_actif), self.levee_reelle(angles_actif, jeu)
    
    def calcul_ouverture(self, jeu : float = 0.0) -> float:
        """Calcule l'ouverture de la loi de levée en fonction du jeu.

        Cette ouverture est définie comme la durée angulaire pendant laquelle la loi de levée théorique à jeu nul est supérieure au jeu. Pour calculer cette durée, les angles pour lesquels la levée à jeu nul est égale au jeu sont calculés. On obtient alors deux angles. Ces deux angles sont ensuite soustraits pour obtenir l'ouverture.

        Args:
            jeu (float, optional): Jeu théorique dans le système.

        Returns:
            float: L'ouverture pour le jeu indiqué.
        """
        angle_attaque_ouverture, angle_attaque_fermeture = self.calcul_angles_attaque(jeu)

        return angle_attaque_fermeture - angle_attaque_ouverture
    
    def calcul_angles_attaque(self, jeu : float = 0.0) -> tuple[float, float]:
        """Calcule les angles d'attaque à l'ouverture et à la fermeture.

        Ces angles sont définis tels que la loi théorique à jeu nul soit égale au jeu pour ces angles.

        Args:
            jeu (float, optional): Jeu choisi pour le système.

        Returns:
            tuple[float, float]: Angle d'attaque à l'ouverture et angle d'attaque (ou de fuite plutôt) à la fermeture.
        """
        angle_rampe_ouverture = self.laws.demilois_ouverture.ac_fin_rampe
        levee_rampe_ouverture = self.laws.demilois_ouverture.lois_accel.levee_rampe
        vitesse_rampe_ouverture = self.laws.demilois_ouverture.lois_accel.vitesse_rampe

        angle_rampe_fermeture = self.laws.dac_leveemax_ouverture + self.laws.dac_leveemax_ouverture - self.laws.demilois_fermeture.ac_fin_rampe
        levee_rampe_fermeture = self.laws.demilois_fermeture.lois_accel.levee_rampe
        vitesse_rampe_fermeture = -self.laws.demilois_fermeture.lois_accel.vitesse_rampe

        angle_attaque_ouverture = (jeu - levee_rampe_ouverture) / vitesse_rampe_ouverture + angle_rampe_ouverture
        angle_attaque_fermeture = (jeu - levee_rampe_fermeture) / vitesse_rampe_fermeture + angle_rampe_fermeture

        return angle_attaque_ouverture, angle_attaque_fermeture
    
    def levee_reelle(self, angles: np.ndarray, jeu: float) -> np.ndarray:
        """Calcule la levée réelle avec prise en considération du jeu.

        Cette méthode soustrait le jeu à la levée réelle.

        Args:
            angles (array-like): Les angles pour lesquels la loi réelle est évaluée.
            jeu (float): Le jeu théorique dans le système. Attention le jeu ne doit pas être supérieur à la levée en fin de rampe.

        Returns:
            array-like: La levée réelle.
        """
        return self.laws.l(angles) - jeu

class CalculEfficacite():
    """Classe représentant le cas d'usage "Calcul de l'efficacité de la loi".

    Cette classe implémente des méthodes pour le calcul de l'efficacité de la loi réelle.

    Args:
        controller (ControllerInterface): Contrôleur de l'application.

    Attributes:
        laws (object): Lois chargées par le contrôleur.
        calcloisrelles (CalculLoisReelles): Instance de l'utilitaire de calcul des lois réelles, CalculLoisRelles.

    Methods:
        __call__(jeu: float = 0.0) -> float:
            Calcule l'efficacité de la loi réelle.
        calcul_aire_reelle(jeu: float) -> float:
            Calcule l'aire sous la courbe de la loi réelle.
    """
    def __init__(self, controller : ControllerInterface):
        self.laws = controller.current_laws
        self.calcloisrelles = CalculLoisReelles(controller)

    def __call__(self, jeu : float = 0.0):
        """Calcule l'efficacité de la loi pour le jeu renseigné.

        Cette fonction calcule l'efficacité, c'est à dire le rapport entre l'aire de la loi réelle et l'aire de la loi idéale.

        Args:
            jeu (float, optional): Jeu théorique choisi pour le système.

        Returns:
            float: Efficacité de la loi.
        """
        ac_attaque_ouverture, ac_attaque_fermeture = self.calcloisrelles.calcul_angles_attaque(jeu)
        
        aire_ideale = (ac_attaque_fermeture - ac_attaque_ouverture)*(self.laws.demilois_ouverture.squelette_levee[-1, 1] - jeu)

        aire_reelle, err = scitg.quad(self.calcloisrelles.levee_reelle, ac_attaque_ouverture, ac_attaque_fermeture, args=(jeu,))
        
        return aire_reelle /aire_ideale
    
    def calcul_aire_reelle(self, jeu: float) -> float:
        """Calcule l'aire de la loi de levée réelle, avec prise en compte du jeu.

        Cette méthode tire profit du module integrate de scipy et plus particulière de la fonction quad qui permet d'intégrer une fonction entre deux bornes. Ici les bornes sont l'angle d'attaque à l'ouverture et l'angle d'attaque à la fermeture.

        Args:
            jeu (float): Jeu choisi pour le système.

        Returns:
            float: Aire sous la courbe de levée de la loi réelle.
        """
        ac_attaque_ouverture, ac_attaque_fermeture = self.calcloisrelles.calcul_angles_attaque(jeu)

        return scitg.quad(self.calcloisrelles.levee_reelle, ac_attaque_ouverture, ac_attaque_fermeture, args=(jeu,))[0]
    