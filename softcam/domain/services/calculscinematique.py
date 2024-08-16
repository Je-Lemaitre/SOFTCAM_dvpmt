import sys
from abc import ABC, abstractmethod

import numpy as np
import numpy.linalg as npl
import scipy.optimize as sco

from domain.entities.assemblage import Assemblage, AssemblageLinguet, AssemblageDirecte
from domain.entities.loiscame import LoisCame

class CalculsCinematique(ABC):
    def __init__(self, assemblage : Assemblage, loiscame : LoisCame):
        self.__x = np.array([1, 0, 0])
        self.__y1 = np.array([0, 1, 0])
        self.__z1 = np.array([0, 0, 1])

        self.__lbd = loiscame.l
        self.__lbd_doac = loiscame.v
        self.__lbd_ddoac = loiscame.a

        self.__sensrot = assemblage.sens_rotation_came
        self.__rb = assemblage.came.rayon_base
    
    @property
    def x(self) -> np.ndarray:
        return self.__x
    @property
    def y1(self) -> np.ndarray:
        return self.__y1
    @property
    def z1(self) -> np.ndarray:
        return self.__z1
    @property
    def lbd(self):
        return self.__lbd
    @property
    def lbd_doac(self):
        return self.__lbd_doac
    @property
    def lbd_ddoac(self):
        return self.__lbd_ddoac
    
    @property
    def sensrot(self):
        return self.__sensrot
    @property
    def rb(self):
        return self.__rb

    @abstractmethod
    def y2(self,ac):
        pass
    @abstractmethod
    def z2(self,ac):
        pass
    @abstractmethod
    def vitesse_glissement(self, ac, contact=None):
        pass
    @abstractmethod
    def position_contact(self, ac, contact=None):
        pass
    @abstractmethod
    def ci_came(self, ac):
        pass
    @abstractmethod
    def di_soup(self, ac):
        pass

    @classmethod
    def matrot(cls, angle):
        cos_beta = np.cos(angle)
        sin_beta = np.sin(angle)

        matrices =  np.zeros((angle.shape[0], 3, 3))
        matrices[:, 0, 0] = 1
        matrices[:, 1, 1] = cos_beta
        matrices[:, 2, 2] = cos_beta
        matrices[:, 1, 2] = -sin_beta
        matrices[:, 2, 1] = sin_beta

        return matrices

class CalculsCinematiqueLevier(CalculsCinematique):
    def __init__(self, assemblage : AssemblageLinguet, loiscame : LoisCame) -> None: 
        super().__init__(assemblage, loiscame)
        
        self.__ol = assemblage.coords_levier
        self.__cl = assemblage.coords_levier - assemblage.coords_came

        self.__l_ling = assemblage.levier.longueur
        self.__rps = assemblage.levier.patin_soupape.rayon_courbure
        self.__rpc = assemblage.levier.patin_came.rayon_courbure
        
        self.__gamma0 = assemblage.angle_leviercame_init
        self.__cb0 = self.compute_cb0()
    
    @property
    def ol(self):
        return self.__ol
    @property
    def cl(self):
        return self.__cl
    @property
    def l_ling(self):
        return self.__l_ling
    @property
    def rps(self):
        return self.__rps
    @property
    def rpc(self):
        return self.__rpc
    @property
    def gamma0(self):
        return self.__gamma0
    @property
    def cb0(self):
        return self.__cb0

    @classmethod
    def rot21(cls, beta):
        angle = np.atleast_1d(beta)
        return cls.matrot(angle)
    @classmethod
    def rot31(cls, ac, gamma0):
        angle = np.atleast_1d(ac + gamma0)
        return cls.matrot(angle)
    def t23(self, ac):
        eta = self.eta(ac)
        phi = self.phi(ac)
        angle_y3_n23 = eta + phi - self.sensrot*ac
        return self.rot31(self.sensrot*ac, self.gamma0)@self.matrot(angle_y3_n23)@np.array([0, 0, -1]) 
    def n23(self, ac):
        eta = self.eta(ac)
        phi = self.phi(ac)
        angle_y3_n23 = eta + phi - self.sensrot*ac
        return self.rot31(self.sensrot*ac, self.gamma0)@self.matrot(angle_y3_n23)@np.array([0, 1, 0])
    def y23(self, ac):
        angle = self.eta(ac) + self.gamma0
        return self.matrot(angle)@np.array([0, 1, 0])
    def z23(self, ac):
        angle = self.eta(ac) + self.gamma0
        return self.matrot(angle)@np.array([0, 0, 1])
    def y3(self, ac):
        return self.rot31(self.sensrot*ac, self.gamma0)@np.array([0,1,0])
    def z3(self, ac):
        return self.rot31(self.sensrot*ac, self.gamma0)@np.array([0,0,1])
    def y2(self, ac):
        return self.rot21(self.beta(ac))@np.array([0,1,0])
    def z2(self, ac):
        return self.rot21(self.beta(ac))@np.array([0,0,1])

    def glissement_specifique(self, ac, contact=None):
        if contact == "Came/Patin" :
            vg = self.vg23(ac)
            gs2 = -vg/self.v2_ic(ac)
            gs3 = vg/self.v3_ic(ac)
            return np.array([gs2, gs3])
        elif contact == "Soupape/Patin":
            vg = self.vg12(ac)
            gs1 = (self.lbd(ac) + self.ol[2])/(self.ol[2] + self.lbd(ac) - self.rps)
            gs2 = (self.lbd(ac) + self.ol[2])/self.rps
            return np.array([gs1, gs2])
        else :
            return np.array([
                self.glissement_specifique(ac, "Came/Patin"),
                self.glissement_specifique(ac, "Soupape/Patin")
            ])

    def vitesse_glissement(self, ac, contact=None):
        if contact == "Came/Patin" :
            return self.vg23(ac)
        elif contact == "Soupape/Patin":
            return self.vg12(ac)
        else :
            return np.array([
                self.vitesse_glissement(ac, "Came/Patin"),
                self.vitesse_glissement(ac, "Soupape/Patin")
            ])
    
    def position_contact(self, ac, contact=None):
        if contact == "Came/Patin" :
            return self.angle_y23init_n23(ac)
        elif contact == "Soupape/Patin":
            return self.di_soup(ac)
        else :
            return np.array([
                self.position_contact(ac, "Came/Patin"),
                self.position_contact(ac, "Soupape/Patin")
            ])
 
    def vg23(self, ac):
        n23 = self.n23(ac)
        lb = self.lb(ac)
        cb = self.cb(ac)
        beta_doac = self.beta_doac(ac)
        return np.einsum(
            "ij, ij -> i",
            cb - np.einsum("i, ij -> ij", beta_doac, lb),
            n23
            ) + self.rpc*(1 - beta_doac)
    
    def vg23_v2(self, ac):
        beta_doac = self.beta_doac(ac)
        ci_came = self.ci_came(ac)
        li_came = self.li_came(ac)
        vg = np.einsum("i, ij -> ij", beta_doac, li_came) - ci_came
        return npl.norm(np.cross(self.x, vg), axis = 1)

    def vg12(self, ac):
        return self.beta_doac(ac) *(self.l_ling*np.sin(self.beta(ac)) + self.rps)
    
    def v3_ic(self, ac):
        t23 = self.t23(ac)
        n23 = self.n23(ac)
        cb = self.cb(ac)
        cb_doac = self.cb_doac(ac)
        return np.einsum("ij , ij -> i", cb_doac, t23) + np.einsum("ij , ij -> i", cb, n23) - self.rpc*(self.phi_doac(ac) + self.eta_doac(ac) - 1)
    
    def v2_ic(self, ac):
        return -self.rpc*(self.phi_doac(ac) + self.eta_doac(ac) - self.beta_doac(ac))

    def v2_is(self, ac):
        return - self.beta_doac(ac) *self.rps

    def v1_is(self, ac):
        return self.beta_doac(ac) *self.l_ling*np.sin(self.beta(ac))

    def angle_y23init_n23(self, ac):
        cos_y23init_n23 = np.atleast_1d(self.cos_y23init_n23(ac))
        cos_y23init_n23_defined = (-1 < cos_y23init_n23) & (cos_y23init_n23 < 1)
        cos_y23init_n23_sup = 1 <= cos_y23init_n23
        cos_y23init_n23_inf = cos_y23init_n23 <= -1
        
        abs_y23init_n23 = np.zeros(len(cos_y23init_n23))
        abs_y23init_n23[cos_y23init_n23_inf] = np.pi
        abs_y23init_n23[cos_y23init_n23_defined] = np.arccos(cos_y23init_n23[cos_y23init_n23_defined])
        abs_y23init_n23[cos_y23init_n23_sup] = 0
        
        return self.sgn_y23init_n23(ac)*abs_y23init_n23
    
    def cos_y23init_n23(self, ac):
        y23_init_base2 = (self.rot21(-self.beta(0))@self.y23(0)[0]).squeeze() 
        y23_init_update = self.rot21(self.beta(ac))@y23_init_base2
        return np.einsum("ij, ij -> i", y23_init_update, self.n23(ac))
    
    def sgn_y23init_n23(self, ac):
        x = np.array([1, 0, 0])
        y23_init_base2 = (self.rot21(-self.beta(0))@self.y23(0)[0]).squeeze() 
        y23_init_update = self.rot21(self.beta(ac))@y23_init_base2
        return np.sign(np.dot(np.cross(y23_init_update, self.n23(ac)), x))

    def ci_came(self, ac):
        return self.cb(ac) + self.rpc*self.n23(ac)
    
    def li_came(self, ac):
        return self.lb(ac) + self.rpc*self.n23(ac)

    def li(self, ac):
        return -self.rps*self.z1 -self.l_ling*self.y2(ac)

    def phi_doac(self, ac, pas = 0.0005):
        return (self.phi(ac+pas) - self.phi(ac-pas))/2/pas    
    
    def phi(self, ac):
        cb = self.cb(ac)
        cb_doac = self.cb_doac(ac)
        eta_doac = self.eta_doac(ac)
        tan_phi = np.einsum("ij, ij -> i", cb, cb_doac)/npl.norm(cb, axis=1)**2/(1-eta_doac)
        return np.arctan(tan_phi)

    def eta_doac(self, ac):
        cos_eta = np.atleast_1d(self.cos_eta(ac))
        cb = self.cb(ac)
        cb_doac = self.cb_doac(ac)

        cos_eta_masked = np.atleast_1d(np.ma.array(np.asarray(cos_eta), mask = (cos_eta**2>=1)))
        factor1 = -self.sgn_eta(ac)/npl.norm(self.cb0)/npl.norm(cb, axis=1)/np.sqrt(1 - cos_eta_masked**2)
        factor1[cos_eta_masked.mask] = 0
        factor2 = np.einsum("ij, j -> i", cb_doac, self.cb0) - np.einsum("ij, ij -> i", cb, cb_doac)*np.einsum("ij, j -> i", cb, self.cb0)/npl.norm(cb, axis=1)**2
        return factor1 *factor2
    
    def cb_doac(self, ac):
        ac = np.atleast_1d(ac)
        x = np.array([1, 0, 0])
        return self.beta_doac(ac)[:, np.newaxis]*np.cross(x, self.lb(ac))
    
    def eta(self, ac):
        cos_eta = np.atleast_1d(self.cos_eta(ac))
        cos_eta_defined = (-1 < cos_eta) & (cos_eta < 1)
        cos_eta_sup = 1 <= cos_eta
        cos_eta_inf = cos_eta <= -1
        
        abs_eta = np.zeros(len(cos_eta))
        abs_eta[cos_eta_inf] = np.pi
        abs_eta[cos_eta_defined] = np.arccos(cos_eta[cos_eta_defined])
        abs_eta[cos_eta_sup] = 0
        
        return self.sgn_eta(ac)*abs_eta

    def cos_eta(self, ac):
        cb = self.cb(ac)
        return np.einsum("ij, j -> i", cb, self.cb0)/npl.norm(self.cb0)/npl.norm(cb, axis=1)
    
    def sgn_eta(self, ac):
        x = np.array([1, 0, 0])
        return np.sign(np.dot(np.cross(self.cb0, self.cb(ac)), x))
    
    def cb(self, ac):
        return self.cl + self.lb(ac)

    def lb(self, ac):
        lb_base2 = (self.rot21(-self.beta(0))@(self.cb0 - self.cl)).squeeze()
        rot21 = self.rot21(self.beta(ac))
        return rot21@lb_base2
    
    def compute_cb0(self) :
        y23_init = np.array([0, np.cos(self.gamma0), np.sin(self.gamma0)])
        return -(self.rb + self.rpc)*y23_init

    def di_soup(self, ac):
        return self.ol[1] - self.l_ling*np.cos(self.beta(ac))
    
    def beta_ddoac(self, ac):
        ac_degree = ac
        beta = self.beta(ac)
        return self.lbd_ddoac(ac_degree)/self.l_ling/np.cos(beta) + self.beta_doac(ac)**2*np.tan(beta)

    def beta_doac(self, ac):
        ac_degree = ac
        beta = self.beta(ac)
        lbd_doac = self.lbd_doac(ac_degree)
        return self.sensrot*lbd_doac/np.cos(beta)/self.l_ling

    def beta(self, ac):
        ac_degree = ac
        lbd = self.lbd(ac_degree)
        num = (lbd + self.ol[2] - self.rps)
        return np.arcsin((lbd + self.ol[2] - self.rps)/self.l_ling)

class CalculsCinematiqueDirecte(CalculsCinematique):
    def __init__(self, assemblage : AssemblageDirecte, loiscame : LoisCame) -> None:
        super().__init__(assemblage, loiscame)
    
    @classmethod
    def rot31(cls, ac, gamma0):
        angle = np.atleast_1d(ac + gamma0)
        return cls.matrot(angle)
    
    def vitesse_glissement(self, ac, contact=None):
        pass
    
    def position_contact(self, ac, contact=None):
        pass




class CalculsCinematiqueFromCame():
    def __init__(self, assemblage : AssemblageLinguet):
        self.__x = np.array([1, 0, 0])
        self.__yc = np.array([0, 1, 0])
        self.__zc = np.array([0, 0, 1])

        self.__oc = assemblage.coords_came
        self.__ol = assemblage.coords_levier

        self.__sensrot = assemblage.sens_rotation_came
        self.__rb = assemblage.came.rayon_base
        self.__rpc = assemblage.levier.patin_came.rayon_courbure
        self.__rps = assemblage.levier.patin_soupape.rayon_courbure
        self.__l_ling = assemblage.levier.longueur
        self.__gamma0 = assemblage.angle_leviercame_init

        self.__rho = assemblage.came.profil
        self.__rho_doeps = assemblage.came.profil.derivative(nu = 1)
        self.__rho_ddoeps = assemblage.came.profil.derivative(nu = 2)

        self.__beta0 = self.compute_beta0()
        self.__lc = self.oc - self.ol
        self.__norm_lc = npl.norm(self.lc)
        self.__lb = self.compute_lb()
        self.__norm_lb = npl.norm(self.lb)

        pass

    @property
    def x(self):
        return self.__x
    @property
    def yc(self):
        return self.__yc
    @property
    def zc(self):
        return self.__zc
    @property
    def oc(self):
        return self.__oc
    @property
    def ol(self):
        return self.__ol
    @property
    def sensrot(self):
        return self.__sensrot
    @property
    def rb(self):
        return self.__rb
    @property
    def rpc(self):
        return self.__rpc
    @property
    def rps(self):
        return self.__rps
    @property
    def l_ling(self):
        return self.__l_ling
    @property
    def gamma0(self):
        return self.__gamma0
    @property
    def rho(self):
        return self.__rho
    @property
    def rho_doeps(self):
        return self.__rho_doeps
    @property
    def rho_ddoeps(self):
        return self.__rho_ddoeps
    @property
    def beta0(self):
        return self.__beta0
    @property
    def lc(self):
        return self.__lc
    @property
    def norm_lc(self):
        return self.__norm_lc
    @property
    def lb(self):
        return self.__lb
    @property
    def norm_lb(self):
        return self.__norm_lb

    @classmethod
    def matrot(cls, angle):
        angle = np.atleast_1d(angle)
        cos_angle = np.cos(angle)
        sin_angle = np.sin(angle)

        matrices =  np.zeros((angle.shape[0], 3, 3))
        matrices[:, 0, 0] = 1
        matrices[:, 1, 1] = cos_angle
        matrices[:, 2, 2] = cos_angle
        matrices[:, 1, 2] = -sin_angle
        matrices[:, 2, 1] = sin_angle

        return matrices

    def u(self, eps):
        eps = np.atleast_1d(eps)
        return self.matrot(eps)@np.array([0,1,0])
    def v(self, eps):
        eps = np.atleast_1d(eps)
        return self.matrot(eps)@np.array([0,0,1])
    def t23(self, eps):
        eps = np.atleast_1d(eps)
        rho = self.rho(eps)
        rho_doeps = self.rho_doeps(eps)
        norm_spd = np.sqrt(self.rho_doeps(eps)**2 + self.rho(eps)**2)
        return - np.einsum("i, ij -> ij", rho_doeps/norm_spd, self.u(eps)) - np.einsum("i, ij -> ij", rho/norm_spd, self.v(eps))
    def n23(self, eps):
        eps = np.atleast_1d(eps)
        return np.cross(self.x, self.t23(eps))
    def y1(self, ac):
        return self.matrot(-ac - self.gamma0)@np.array([0, 1, 0])
    def z1(self, ac):
        return np.cross(self.x, self.y1(ac))
    def y2(self, ac, beta):
        rot21 = self.matrot(beta)
        y1 = self.y1(ac)
        return np.einsum("ijk, ik -> ij", rot21, y1)
    
    def lbd(self, ac):
        eps = self.solve_fermeture_geom(ac)
        beta = self.beta(ac, eps)
        oi_soup_base3 = self.oc_base3(ac) + self.ci_soup_base3(ac, beta)
        return -np.einsum("ij, ij -> i", oi_soup_base3, self.z1(ac))

    def ci_soup_base3(self, ac, beta):
        cl_base3 = - self.matrot(-ac-self.gamma0)@self.lc
        la_base3 = - self.l_ling*self.y2(ac, beta)
        ai_base3 = - self.rps*self.z1(ac) 
        return cl_base3 + la_base3 + ai_base3

    def oc_base3(self, ac):
        return self.matrot(-ac-self.gamma0)@self.oc

    def beta(self, ac, eps):
        term_eps = self.eq1_fermeture_geom(eps, ac)
        term_eps_doac = np.zeros(len(ac))
        term_eps_doac[1:-1] = (term_eps[2:] - term_eps[:-2])/(ac[2:] - ac[:-2])
        term_eps_doac[0] = (term_eps[1] - term_eps[0])/(ac[1] - ac[0])
        term_eps_doac[-1] = (term_eps[-1] - term_eps[-2])/(ac[-1] - ac[-2])

        term_eps_doac_neg = (term_eps_doac <= 0)
        term_eps_doac_pos = (term_eps_doac > 0)

        discriminant = self.norm_lb**2 - term_eps**2

        tan = np.zeros(len(ac))
        tan[term_eps_doac_neg] = (-self.lb[2] + np.sqrt(discriminant[term_eps_doac_neg]))/(term_eps[term_eps_doac_neg] - self.lb[1])
        tan[term_eps_doac_pos] = (-self.lb[2] - np.sqrt(discriminant[term_eps_doac_pos]))/(term_eps[term_eps_doac_pos] - self.lb[1])

        beta = ac + self.gamma0 - 2*np.arctan(tan)
        
        return np.mod(beta + np.pi, 2*np.pi) - np.pi

    def solve_fermeture_geom(self, acs):
        sols = []
        for ac in acs:
            sol = sco.root_scalar(self.equation_fermeture_geom, x0 = abs(ac)+0.1, args=(ac,), method="secant")
            sols.append(sol.root[0])
        return np.array(sols)
    
    def equation_fermeture_geom(self, eps, ac):
        term1 = self.eq1_fermeture_geom(eps, ac)**2 
        term2 = self.eq2_fermeture_geom(eps, ac)**2
        return term1 + term2 - self.norm_lb**2
    
    def eq1_fermeture_geom(self, eps, ac):
        rho = self.rho(eps)
        delta = self.delta(eps)
        return -self.lc[1]*np.cos(ac + self.gamma0) - self.lc[2]*np.sin(ac + self.gamma0) + self.rpc*np.cos(eps + delta) + rho*np.cos(eps)
    
    def eq2_fermeture_geom(self, eps, ac):
        rho = self.rho(eps)
        delta = self.delta(eps)
        return self.lc[1]*np.sin(ac + self.gamma0) - self.lc[2]*np.cos(ac + self.gamma0) + self.rpc*np.sin(eps + delta) + rho*np.sin(eps)

    def delta(self, eps):
        cos_delta = np.atleast_1d(self.cos_delta(eps))
        cos_delta_defined = (-1 <= cos_delta) & (cos_delta <= 1)
        cos_delta_sup = 1 < cos_delta
        cos_delta_inf = cos_delta < -1
        
        abs_delta = np.zeros(len(cos_delta))
        abs_delta[cos_delta_inf] = np.pi
        abs_delta[cos_delta_defined] = np.arccos(cos_delta[cos_delta_defined])
        abs_delta[cos_delta_sup] = 0
        
        return self.sgn_delta(eps)*abs_delta
    
    def cos_delta(self, eps):
        u = self.u(eps)
        n23 = self.n23(eps)
        return np.einsum("ij, ij -> i", u , n23)
    
    def sgn_delta(self, eps):
        return np.sign(np.dot(np.cross(self.u(eps), self.n23(eps)), self.x))
    
    def compute_lb(self):
        y23_init = np.array([0, np.cos(self.gamma0), np.sin(self.gamma0)])
        lb0 = self.lc - (self.rb + self.rpc)*y23_init
        rot12 = self.matrot(-self.beta0)[0]
        return rot12@lb0 

    def compute_beta0(self):
        return np.arcsin((self.ol[2] - self.rps)/self.l_ling)    

class CalculsCinematiqueFromCameV1():
    def __init__(self, assemblage : AssemblageLinguet):
        self.__x = np.array([1, 0, 0])
        self.__yc = np.array([0, 1, 0])
        self.__zc = np.array([0, 0, 1])

        self.__oc = assemblage.coords_came
        self.__ol = assemblage.coords_levier

        self.__sensrot = assemblage.sens_rotation_came
        self.__rb = assemblage.came.rayon_base
        self.__rpc = assemblage.levier.patin_came.rayon_courbure
        self.__rps = assemblage.levier.patin_soupape.rayon_courbure
        self.__l_ling = assemblage.levier.longueur
        self.__gamma0 = assemblage.angle_leviercame_init

        self.__rho = assemblage.came.profil
        self.__rho_doeps = assemblage.came.profil.derivative(nu = 1)
        self.__rho_ddoeps = assemblage.came.profil.derivative(nu = 2)

        self.__beta0 = self.compute_beta0()
        self.__lc = self.oc - self.ol
        self.__norm_lc = npl.norm(self.lc)
        self.__lb = self.compute_lb()
        self.__norm_lb = npl.norm(self.lb)

        pass

    @property
    def x(self):
        return self.__x
    @property
    def yc(self):
        return self.__yc
    @property
    def zc(self):
        return self.__zc
    @property
    def oc(self):
        return self.__oc
    @property
    def ol(self):
        return self.__ol
    @property
    def sensrot(self):
        return self.__sensrot
    @property
    def rb(self):
        return self.__rb
    @property
    def rpc(self):
        return self.__rpc
    @property
    def rps(self):
        return self.__rps
    @property
    def l_ling(self):
        return self.__l_ling
    @property
    def gamma0(self):
        return self.__gamma0
    @property
    def rho(self):
        return self.__rho
    @property
    def rho_doeps(self):
        return self.__rho_doeps
    @property
    def rho_ddoeps(self):
        return self.__rho_ddoeps
    @property
    def beta0(self):
        return self.__beta0
    @property
    def lc(self):
        return self.__lc
    @property
    def norm_lc(self):
        return self.__norm_lc
    @property
    def lb(self):
        return self.__lb
    @property
    def norm_lb(self):
        return self.__norm_lb

    @classmethod
    def matrot(cls, angle):
        angle = np.atleast_1d(angle)
        cos_beta = np.cos(angle)
        sin_beta = np.sin(angle)

        matrices =  np.zeros((angle.shape[0], 3, 3))
        matrices[:, 0, 0] = 1
        matrices[:, 1, 1] = cos_beta
        matrices[:, 2, 2] = cos_beta
        matrices[:, 1, 2] = -sin_beta
        matrices[:, 2, 1] = sin_beta

        return matrices

    def u(self, eps):
        eps = np.atleast_1d(eps)
        return self.matrot(eps)@np.array([0,-1,0])
    def v(self, eps):
        eps = np.atleast_1d(eps)
        return self.matrot(eps)@np.array([0,0,-1])
    
    def t23(self, eps):
        eps = np.atleast_1d(eps)
        rho = self.rho(eps)
        rho_doeps = self.rho_doeps(eps)
        norm_spd = np.sqrt(self.rho_doeps(eps)**2 + self.rho(eps)**2)
        return np.einsum("i, ij -> ij", rho_doeps/norm_spd, self.u(eps)) + np.einsum("i, ij -> ij", rho/norm_spd, self.v(eps))
    def n23(self, eps):
        eps = np.atleast_1d(eps)
        return np.cross(self.x, self.t23(eps))
    def y1(self, ac):
        return self.matrot(-ac - self.gamma0)@np.array([0, 1, 0])
    def z1(self, ac):
        return np.cross(self.x, self.y1(ac))
    def y2(self, ac, beta):
        rot21 = self.matrot(beta)
        y1 = self.y1(ac)
        return np.einsum("ijk, ik -> ij", rot21, y1)
    
    def lbd(self, ac, beta):
        oi_soup_base3 = self.oc_base3(ac) + self.ci_soup_base3(ac, beta)
        return -np.einsum("ij, ij -> i", oi_soup_base3, self.z1(ac))

    def ci_soup_base3(self, ac, beta):
        cl_base3 = - self.matrot(-ac-self.gamma0)@self.lc
        la_base3 = - self.l_ling*self.y2(ac, beta)
        ai_base3 = - self.rps*self.z1(ac) 
        return cl_base3 + la_base3 + ai_base3

    def oc_base3(self, ac):
        return self.matrot(-ac-self.gamma0)@self.oc

    def solve_fermeture_geom(self, eps):
        cbs = self.cb(eps)
        sols = []
        for cb in cbs:
            sol = sco.root(self.equation_fermeture_geom, x0 = np.array([0,-0.341]), args=(cb,))
            sols.append(sol.x)
        return np.array(sols)
    
    def equation_fermeture_geom(self, angles, cb):
        rot13 = self.matrot(-(angles[0] + self.gamma0))[0]
        rot21 = self.matrot(angles[1])[0]
        mateq = cb - rot13@rot21@self.lb + rot13@self.lc
        return mateq[1:]
    
    def compute_lb(self):
        y23_init = np.array([0, np.cos(self.gamma0), np.sin(self.gamma0)])
        lb0 = self.oc - self.ol - (self.rb + self.rpc)*y23_init
        rot12 = self.matrot(-self.beta0)[0]
        return rot12@lb0

    def cb(self, eps):
        return self.ci_came(eps) - self.rpc*self.n23(eps)
    
    def ci_came(self, eps):
        eps = np.atleast_1d(eps)
        return np.einsum("i, ij -> ij", self.rho(eps), self.u(eps)) 
    
    def compute_beta0(self):
        return np.arcsin((self.ol[2] - self.rps)/self.l_ling)
    
    if __name__=="__main__":
        pass