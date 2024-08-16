import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")
from abc import ABC, abstractmethod
from typing import Tuple, Union

import numpy as np
import numpy.linalg as npl
import numpy.typing as npt
import scipy.interpolate as scitp

import domain.services.unitees as unit
from domain.entities.assemblage import Assemblage, AssemblageLinguet, AssemblageDirecte
from domain.entities.loiscame import LoisCame
from domain.services.calculscinematique import CalculsCinematique, CalculsCinematiqueLevier, CalculsCinematiqueDirecte

class CalculsProfilCame(ABC):
    def __init__(self, assemblage : Assemblage, loiscame : LoisCame, calccinematique : CalculsCinematique, ac_evalpts : np.ndarray):
        self.lbd = loiscame.l
        self.lbd_doac = loiscame.v
        self.ccin = calccinematique
        self.sensrot = assemblage.sens_rotation_came

        self.angle_polaire_itp = None
        self.profil_polaire_itp = None
    
    def rayon_courbure(self, eps : np.ndarray) -> np.ndarray :
        rho = self.profil_polaire(eps)
        rho_doeps = self.profil_polaire_itp.derivative(nu=1)(eps)
        rho_ddoeps = self.profil_polaire_itp.derivative(nu=2)(eps)
        
        return (rho**2 + rho_doeps**2)**(3/2)/(rho**2 + 2*rho_doeps**2 - rho*rho_ddoeps)
    
    def profil_polaire(self, eps : np.ndarray) -> np.ndarray :
        return self.profil_polaire_itp(eps)
    
    def interpolate_deplacement_roller(self, ac, rayon_roller = 8.5e-3):
        eps3_evalpts, rho3_evalpts = self.position_polaire_roller(ac, rayon_roller) 
        
        knot_vector,coefficients,degree = scitp.splrep(eps3_evalpts, rho3_evalpts, k=3)
        return scitp.BSpline(knot_vector, coefficients, degree, extrapolate=True)
    
    def interpolate_profil_polaire(self, ac : np.ndarray) -> scitp.BSpline :
        rho_evalpts = npl.norm(self.profil_cartesien(ac), axis =1)
        eps_evalpts = self.angle_polaire(ac)
        
        knot_vector, coefficients,degree = scitp.splrep(eps_evalpts, rho_evalpts, k=5)
        return scitp.BSpline(knot_vector, coefficients, degree, extrapolate=True)
    
    def interpolate_angle_polaire(self, ac : np.ndarray) -> scitp.BSpline :
        eps_evalpts = self.angle_polaire(ac)

        knot_vector,coefficients,degree = scitp.splrep(ac, eps_evalpts, k=5)
        return scitp.BSpline(knot_vector, coefficients, degree, extrapolate=True)
    
    @abstractmethod
    def plan_tangent(self, ac):
        pass
    @abstractmethod
    def position_polaire_roller(self, ac, rayon_roller = 8.5e-3):
        pass
    @abstractmethod
    def angle_polaire(self, ac):
        pass
    @abstractmethod
    def profil_cartesien(self, ac : np.ndarray) -> np.ndarray :
        pass
            
class CalculsProfilCameLevier(CalculsProfilCame):
    """Les différentes notations développées dans cette classe ne peuvent être comprise qu'avec l'aide de la documentation.
    """
    def __init__(self, assemblage : AssemblageLinguet, loiscame : LoisCame, calccinematique : CalculsCinematiqueLevier, ac_evalpts : np.ndarray) -> None:
        super().__init__(assemblage, loiscame, calccinematique, ac_evalpts)
        
        self.__oc = assemblage.coords_came
        self.__ol = assemblage.coords_levier
        self.__cl = assemblage.coords_levier - assemblage.coords_came
        

        self.__l_ling = assemblage.levier.longueur
        self.__rps = assemblage.levier.patin_soupape.rayon_courbure
        self.__rpc = assemblage.levier.patin_came.rayon_courbure
        self.__rb = assemblage.came.rayon_base
        self.__gamma0 = assemblage.angle_leviercame_init

        self.angle_polaire_itp = self.interpolate_angle_polaire(ac_evalpts)
        self.profil_polaire_itp = self.interpolate_profil_polaire(ac_evalpts)
        
    @property
    def oc(self):
        return self.__oc
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
    def rb(self):
        return self.__rb
    @property
    def gamma0(self):
        return self.__gamma0
    
    def plan_tangent(self, ac):
        phi = self.ccin.phi(ac)
        rho2 = npl.norm(self.ccin.cb(ac), axis=1)
        hc = rho2*np.cos(phi) - self.rpc - self.rb
        delta = self.sensrot*ac  - self.ccin.eta(ac) - phi
        
        return hc, delta
    
    def position_polaire_roller(self, ac, rayon_roller = 8.5e-3):
        rho2 = npl.norm(self.ccin.cb(ac), axis=1)
        phi = self.ccin.phi(ac)
        eta = self.ccin.eta(ac)
        
        rho3 = np.sqrt(rho2**2 + (rayon_roller - self.rpc)**2 -2*(rayon_roller - self.rpc)*rho2*np.cos(np.pi - phi))
        eps3 = abs(self.sensrot*ac  - eta - np.arcsin((rayon_roller - self.rpc)*np.sin(phi)/rho3))

        return eps3, rho3
    
    def angle_polaire(self, ac):
        ac_vec = np.atleast_1d(ac)
        rot31 = self.ccin.rot31(-self.sensrot*ac_vec, -self.gamma0)
        cb = np.einsum("ijk, ik -> ij", rot31, self.ccin.cb(ac_vec))
        ci = self.profil_cartesien(ac)
        
        cos_eps = np.einsum("ij, ij -> i", cb, ci)/npl.norm(cb, axis=1)/npl.norm(ci, axis=1)
        cos_eps_defined = (-1 < cos_eps) & (cos_eps < 1)
        cos_eps_sup = 1 <= cos_eps
        cos_eps_inf = cos_eps <= -1
        
        abs_eps = np.zeros(len(cos_eps))
        abs_eps[cos_eps_inf] = np.pi
        abs_eps[cos_eps_defined] = np.arccos(cos_eps[cos_eps_defined])
        abs_eps[cos_eps_sup] = 0
        
        sgn_eps = np.sign(np.dot(np.cross(cb, ci), np.array([1, 0, 0])))
        
        return -self.sensrot*ac + self.ccin.eta(ac) + sgn_eps*abs_eps
    
    def profil_cartesien(self, ac):
        return np.einsum("ijk, ik -> ij", self.ccin.rot31(-self.sensrot*ac, -self.gamma0), self.ccin.ci_came(ac))

class CalculsProfilCameDirecte(CalculsProfilCame):
    def __init__(self, assemblage : AssemblageDirecte, loiscame : LoisCame, calccinematique : CalculsCinematiqueDirecte, ac_evalpts : np.ndarray):
        super().__init__(assemblage, loiscame, calccinematique, ac_evalpts)
    
    def plan_tangent(self, ac):
        pass
            
    def position_polaire_roller(self, ac, rayon_roller = 8.5e-3):
        pass
    
    def angle_polaire(self, ac):
        pass
    
    def profil_cartesien(self, ac):
        pass
