import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")
from abc import ABC, abstractmethod

import numpy as np
import numpy.linalg as npl
import scipy.interpolate as scitp

from domain.entities.assemblage import Assemblage, AssemblageLinguet, AssemblageDirecte
from domain.entities.loiscame import LoisCame
from domain.services.calculscinematique import CalculsCinematique, CalculsCinematiqueLevier, CalculsCinematiqueDirecte

class CalculsProfilCame(ABC):
    """Classe abstraite pour le calcul du profil de la came et des grandeurs associées.

    Cette classe constitue un utilitaire pour le calcul du profil de la came en coordonnées cartésiennes et polaires. Permet également le calcul de grandeurs associées à ce profil comme le rayon de courbure.

    Args:
        assemblage (Assemblage): Assemblage étudié.
        loiscame (LoisCame): Lois créée.
        calccinematique (CalculsCinematique): Utilitaire de calcul cinématique.
        ac_evalpts (np.ndarray): Angles de rotation de la came pour lesquels seront évalués le profil.

    Attributes:
        lbd (callable): Loi de levée.
        lbd_doac (callable): Vitesse de la loi de levée.
        ccin (CalculsCinematique): Utilitaire de réalisation des calculs cinématiques.
        sensrot (str): Sens de rotation de la came. Positif dans le sens trigonométrique et négatif dans l'autre.
        angle_polaire_itp (BSpline, optional): Interpolation de l'angle polaire en fonction de l'angle de rotation de la came.
        profil_polaire_itp (BSpline, optional): Interpolation du profil de la came en fonction de l'angle polaire.

    Methods:
        rayon_courbure(eps) : Calcule le rayon de courbure pour un angle polaire.
        profil_polaire(eps): Calcule le profil polaire pour un angle polaire.
        interpolate_deplacement_roller(ac, rayon_roller): Crée un spline interpolant le déplacement du roller.
        interpolate_profil_polaire(ac): Crée une spline interpolant le profil polaire de la came.
        interpolate_angle_polaire(ac): Crée une spline interpolant l'angle polaire en fonction de l'angle de rotation de la came.
        plan_tangent(ac): Méthode abstraite pour la représentation du profil par plan tangent (voir B. Geoffroy).
        position_polaire_roller(ac, rayon_roller): Méthode abstraite pour le calcul du déplacement du roller en fonction de l'angle de rotation de la came.
        angle_polaire(ac): Méthode abstraite pour le calcul de l'angle polaire en fonction de l'angle de rotation de la came.
        profil_cartesien(ac): Méthode abstraite pour le calcul du profil de la came en coordonnées cartésiennes.
    """
    def __init__(self, assemblage: Assemblage, loiscame: LoisCame, calccinematique: CalculsCinematique, ac_evalpts: np.ndarray):
        self.lbd = loiscame.l
        self.lbd_doac = loiscame.v
        self.ccin = calccinematique
        self.sensrot = assemblage.sens_rotation_came
        self.angle_polaire_itp = None
        self.profil_polaire_itp = None
    
    def rayon_courbure(self, eps: float) -> float:
        """Calcule le rayon de courbure de la came à un angle polaire spécifié.

        Cette méthode calcule le rayon de courbure de la came pour l'angle polaire, epsilon, indiqué. Par angle polaire, il est entendu l'angle des coordonnées cylindriques. En effet, cet angle est différent de l'angle de rotation de la came. Pour faire ce calcul, le profil polaire rho = f(epsilon) est interpolé par une spline.

        Args:
            eps (float): Angle polaire.

        Returns:
            float: Le rayon de courbure à l'angle indiqué.
        """
        rho = self.profil_polaire(eps)
        rho_doeps = self.profil_polaire_itp.derivative(nu=1)(eps)
        rho_ddoeps = self.profil_polaire_itp.derivative(nu=2)(eps)
        return (rho**2 + rho_doeps**2)**(3/2)/(rho**2 + 2*rho_doeps**2 - rho*rho_ddoeps)
    
    def profil_polaire(self, eps: float) -> float:
        """Calcule le rayon polaire à un angle polaire spécifié.

        Cette méthode utilise directement profil polaire interpolé, rho = f(epsilon).

        Args:
            eps (float): Angle polaire.

        Returns:
            float: Rayon polaire.
        """
        return self.profil_polaire_itp(eps)
    
    def interpolate_deplacement_roller(self, ac: np.ndarray, rayon_roller: float = 8.5e-3) -> scitp.BSpline:
        """Interpole le déplacement du roller en coordonnées polaires.

        Cette méthode interpole la position du roller exprimée en coordonnées polaires. Pour ce faire, on calcule la distance entre le centre de la came et le centre du roller ainsi que l'angle entre le vecteur y3 lié à la came et le vecteur reliant le centre de rotation de la came au centre du roller. Ce calcul est réalisé pour l'ensemble des angles de rotation de came indiqués. La distance est ensuite interpolée en fonction de l'angle.  

        Args:
            ac (np.ndarray): Angles rotations de la came pour lesquels seront évalués la position du roller.

        Returns:
            scitp.BSpline: B-spline repérant le roller en coordonnées polaires par rapport au référentiel lié à la came.
        """
        eps3_evalpts, rho3_evalpts = self.position_polaire_roller(ac, rayon_roller) 
        knot_vector,coefficients,degree = scitp.splrep(eps3_evalpts, rho3_evalpts, k=3)
        return scitp.BSpline(knot_vector, coefficients, degree, extrapolate=True)
    
    def interpolate_profil_polaire(self, ac: np.ndarray) -> scitp.BSpline:
        """Interpole le profil de la came exprimé en coordonnées polaires.

        Cette méthode interpole le profil de came exprimé en coordonnées polaires, rho=f(epsilon). Pour ce faire, le rayon polaire est d'abord calculé pour un ensemble d'angles de rotation de la came. L'angle polaire, epsilon, est ensuite calculé pour ces mêmes angles de rotation de la came. Enfin, le profil polaire est interpolé.

        Args:
            ac (np.ndarray): Angles rotations de la came pour lesquels seront évalués le rayon et l'angle polaire.

        Returns:
            scitp.BSpline: B-spline représentant le profil en coordonnées polaires.
        """
        rho_evalpts = npl.norm(self.profil_cartesien(ac), axis =1)
        eps_evalpts = self.angle_polaire(ac)
        knot_vector, coefficients,degree = scitp.splrep(eps_evalpts, rho_evalpts, k=5)
        return scitp.BSpline(knot_vector, coefficients, degree, extrapolate=True)
    
    def interpolate_angle_polaire(self, ac: np.ndarray) -> scitp.BSpline:
        """Interpole l'angle polaire, epsilon, en fonction de l'angle de la came.

        Cette méthode interpole la valeur de l'angle polaire, epsilon, en fonction de l'angle de rotation de la came. Pour cela, l'angle polaire est d'abord calculé pour un ensemble d'angles de rotation de la came définis.

        Args:
            ac (np.ndarray): Angles rotations de la came pour lesquels seront évalués la position du roller.

        Returns:
            scitp.BSpline: B-spline donnant l'angle polaire en fonction de l'angle de rotation de la came.
        """
        eps_evalpts = self.angle_polaire(ac)
        knot_vector,coefficients,degree = scitp.splrep(ac, eps_evalpts, k=5)
        return scitp.BSpline(knot_vector, coefficients, degree, extrapolate=True)
    
    @abstractmethod
    def plan_tangent(self, ac: float) -> tuple[float, float]:
        pass
    @abstractmethod
    def position_polaire_roller(self, ac: float, rayon_roller: float =8.5e-3) -> tuple[float, float]:
        pass
    @abstractmethod
    def angle_polaire(self, ac: float) -> float:
        pass
    @abstractmethod
    def profil_cartesien(self, ac : np.ndarray) -> np.ndarray :
        pass
            
class CalculsProfilCameLevier(CalculsProfilCame):
    """Implémentation de la classe abstraite "CalculsProfilCame" pour les système à "levier".

    Args:
        assemblage (AssemblageLinguet): L'assemblage étudié. Il doit être constitué d'un "levier".
        loiscame (LoisCame): Lois de distribution étudiées.
        calccinematique (CalculsCinematiqueLevier): Utilitaire de calcul cinématique les système à "levier".
        ac_evalpts (np.ndarray): Angles de rotation de la came pour lesquels seront interpolés les profils.

    Attributes:
        oc (np.ndarray): Coordonnées du centre de la came.
        ol (np.ndarray): Coordonnées du levier.
        cl (np.ndarray): Vecteur CL. Voir définition dans le rapport.
        l_ling (float): Longueur du linguet. De son centre de rotation au centre du patin en contact avec la soupape.
        rps (float): Rayon de courbure du patin côté soupape.
        rpc (float): Rayon de courbure du patin côté came.
        rb (float): Rayon de base de la came.
        gamma0 (float): Angle entre le vecteur y1 et le vecteur BC à levée nulle.
    
    Methods : 
        plan_tangent(ac): Calcule la représentation du profil par plan tangent (voir B. Geoffroy).
        position_polaire_roller(ac, rayon_roller): Calcule le déplacement du roller en fonction de l'angle de rotation de la came.
        angle_polaire(ac): Calcule l'angle polaire en fonction de l'angle de rotation de la came.
        profil_cartesien(ac): Calcule le profil de la came en coordonnées cartésiennes.
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
    
    def plan_tangent(self, ac: float) -> tuple[float, float]:
        """Calcule la position du plan tangent pour un angle de rotation de la came donné.

        Cette méthode calcule la hauteur et l'angle permettant de repérer le plan tangent à la came. Voir l'étude de B. Geoffroy pour plus de détails. 

        Args:
            ac: L'angle de rotation de la came.

        Returns:
            tuple[float, float]: La heuteur et l'angle permettant de positionner le plan tangent.
        """
        phi = self.ccin.phi(ac)
        rho2 = npl.norm(self.ccin.cb(ac), axis=1)
        hc = rho2*np.cos(phi) - self.rpc - self.rb
        delta = self.sensrot*ac  - self.ccin.eta(ac) - phi
        
        return hc, delta
    
    def position_polaire_roller(self, ac: float, rayon_roller: float = 8.5e-3) -> tuple[float, float]:
        """Calcule la postion du centre du roller en coordonnées polaires dans le référentiel de la came.

        Cette méthode calcule la position du roller, rayon et angle, en coordonnées polaires dans le référentiel de la came.

        Args:
            ac(float): Angle de rotation de la came.
            rayon_roller (float, optional): Rayon du roller.

        Returns:
            tuple[float, float]: rayon et angle polaire permettant de positionner le centre du roller.
        """
        rho2 = npl.norm(self.ccin.cb(ac), axis=1)
        phi = self.ccin.phi(ac)
        eta = self.ccin.eta(ac)
        rho3 = np.sqrt(rho2**2 + (rayon_roller - self.rpc)**2 -2*(rayon_roller - self.rpc)*rho2*np.cos(np.pi - phi))
        eps3 = abs(self.sensrot*ac  - eta - np.arcsin((rayon_roller - self.rpc)*np.sin(phi)/rho3))
        return eps3, rho3
    
    def angle_polaire(self, ac: float) -> float:
        """Calcule l'angle polaire, espsilon.

        Calcule l'angle polaire espilon pour un angle de rotation de came donné.

        Args:
            ac(float): Angle de rotation de la came.

        Returns:
            float: L'angle polaire associé à l'angle de rotation de la came.
        """
        ac_vec = np.atleast_1d(ac)
        rot31 = self.ccin.matrot(-(self.sensrot*ac_vec + self.gamma0))
        cb = np.einsum("ijk, ik -> ij", rot31, self.ccin.cb(ac_vec))
        ci = self.profil_cartesien(ac)

        cos_eps = np.einsum("ij, ij -> i", cb, ci)/npl.norm(cb, axis=1)/npl.norm(ci, axis=1)
        cos_eps_defined = (cos_eps > -1) & (cos_eps < 1)
        cos_eps_sup = cos_eps >= 1
        cos_eps_inf = cos_eps <= -1

        abs_eps = np.zeros(len(cos_eps))
        abs_eps[cos_eps_inf] = np.pi
        abs_eps[cos_eps_defined] = np.arccos(cos_eps[cos_eps_defined])
        abs_eps[cos_eps_sup] = 0

        sgn_eps = np.sign(np.dot(np.cross(cb, ci), np.array([1, 0, 0])))

        return -self.sensrot*ac + self.ccin.eta(ac) + sgn_eps*abs_eps
    
    def profil_cartesien(self, ac: float) -> np.ndarray:
        """Calule la position du point de contact dans le référentiel lié à la came.

        Cette méthode calcule la position du point de contact entre la came et son patin, en coordonnées cartésiennes, dans le référentiel lié à la came. Pour cela, le vecteur CI_c, calculé par l'utilitaire de cinématique dans la base liée à la soupape, subit une simple rotation d'un angle ac + gamma0. Cette rotation est ici écrite sous forme matricielle. En renseignant des angles allant de 0 à 360 degrées, on peut représenter le profil de la came.

        Args:
            ac: Angle de rotation de la came.

        Returns:
            np.ndarray: Position du point de contact en coordonnées cartésiennes dans le référentiel lié à la came.
        """
        return np.einsum("ijk, ik -> ij", self.ccin.matrot(-(self.sensrot*ac + self.gamma0)), self.ccin.ci_c(ac))

class CalculsProfilCameDirecte(CalculsProfilCame):
    """Implémentation de la classe abstraite "CalculsProfilCame" pour les système à attaque directe.

    Args:
        assemblage (AssemblageLinguet): L'assemblage étudié. Il doit être constitué à attaque directe et constitué d'un poussoir.
        loiscame (LoisCame): Lois de distribution étudiées.
        calccinematique (CalculsCinematiqueLevier): Utilitaire de calcul cinématique les système à attaque directe.
        ac_evalpts (np.ndarray): Angles de rotation de la came pour lesquels seront interpolés les profils.

    Attributes:
        oc (np.ndarray): Coordonnées du centre de la came.
        rb (float): Rayon de base de la came.

    Methods : 
        plan_tangent(ac): Calcule la représentation du profil par plan tangent (voir B. Geoffroy).
        position_polaire_roller(ac, rayon_roller): Calcule le déplacement du roller en fonction de l'angle de rotation de la came.
        angle_polaire(ac): Calcule l'angle polaire en fonction de l'angle de rotation de la came.
        profil_cartesien(ac): Calcule le profil de la came en coordonnées cartésiennes.
    """
    def __init__(self, assemblage : AssemblageDirecte, loiscame : LoisCame, calccinematique : CalculsCinematiqueDirecte, ac_evalpts : np.ndarray):
        super().__init__(assemblage, loiscame, calccinematique, ac_evalpts)
    
    def plan_tangent(self, ac: float) -> tuple[float, float]:
        pass
            
    def position_polaire_roller(self, ac: float, rayon_roller: float= 8.5e-3) -> tuple[float, float]:
        pass
    
    def angle_polaire(self, ac: float) -> float:
        pass
    
    def profil_cartesien(self, ac: float) -> np.ndarray:
        pass
