import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from abc import ABC, abstractmethod

import numpy as np
import numpy.linalg as npl
import scipy.optimize as sco

from domain.entities.assemblage import Assemblage, AssemblageLinguet, AssemblageDirecte
from domain.entities.loiscame import LoisCame

class CalculsCinematique(ABC):
    """
        Classe abstraite pour la réalisation des calculs cinématiques relitfs aux systèmes.

        Cette class initialise les paramètres principaux communs à tous les systèmes de distribution et fournit des "properties" pour accéder à ces paramètres. Des méthodes abstraites à implémenter obligatoirement dans les classes enfants sont également définie. Ces méthodes permet le calcul de grandeurs communes à tous les systèmes de distribution.
        
        Les variables définies ici correspondent au paramétrage utilisé dans le rapport associé.

        Args:
            assemblage (Assemblage): L'assemblage étudié, qui stocke les grandeurs caractéristiques de l'assemblage.
            loiscame (LoisCame): Les lois de distribution, qui serve de loi entrée-sortie.

        Attributes:
            x (np.ndarray): Vecteur unitaire suivant la direction x.
            y1 (np.ndarray): Vecteur unitaire suivant la direction y1.
            z1 (np.ndarray): Vecteur unitaire suivant la direction z1.
            lbd (scipy.BSpline): Loi de levée .
            lbd_doac (scipy.BSpline): Loi de vitesse (dérivée première de la levée par rapport à l'angle de la came).
            lbd_ddoac (scipy.BSpline): Loi d'accélération.
            sensrot (int): Sens de rotation de la came (sens trigonométrique = 1, sens horaire = -1).
            rb (float): Rayon de base de la came.

        Methods:
            y2(ac): Méthode abstraite, calcule le vecteur unitaire y2 en fonction de l'angle de roation de la came.
            z2(ac): Méthode abstraite, calcule le vecteur unitaire z2 en fonction de l'angle de roation de la came.
            vitesse_glissement(ac, contact=None): Méthode abstraite, calcule la vitesse de glissement (en m/rad) en fonction de l'angle de rotation de la came contact considéré.
            position_contact(ac, contact=None): Méthode abstraite, détermine la position du point de contact en fonction de l'angle de rotation de la came et du contact considéré.
            ci_c(ac): Méthode abstraite, détermine l'expression du vecteur reliant le centre de la came au point de contact avec la pièce en vis-à-vis en fonction de l'angle de rotation de la came.
            matrot(angle): Méthode de classe, définit la matrice de rotation de l'angle renseigné.
    """

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
    def ci_c(self, ac):
        pass

    @classmethod
    def matrot(cls, angle : np.ndarray):
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

class CalculsCinematiqueLevier(CalculsCinematique):
    """Classe permettant de réalisé les calculs cinématique spécifiques aux systèmes avec levier (Linguet ou Basculeur).

    Cette classe hérite de la classe CalculsCinematique et implémente des méthodes spécifique au sytèmes à levier.

    Args:
        assemblage (AssemblageLinguet): Un assemblage à levier.
        loiscame (LoisCame): Les lois de distribution.

    Attributes:
        ol (np.ndarray): Coordonnées du centre de rotation du levier.
        cl (np.ndarray): Coordonnées du vecteur CL.
        l_ling (float): Longueur du levier, norme du vecteur AL.
        rps (float): Rayon de courbure du patin côté soupape.
        rpc (float): Rayon de courbure du patin côté came.
        gamma0 (float): Angle entre le vecteur y1 et le vecteur BC à levée nulle.
        cb0 (np.ndarray): Vecteur CB à levée nulle.

    Methods:
        t23(ac): Calcule le vecteur tangent au contact Came/Patin.
        n23(ac): Calcule le vecteur normal au contact Came/Patin.
        y23(ac): Calcule le vecteur y23 dans le référentiel lié à la soupape.
        z23(ac): Calcule le vecteur z23 dans le référentiel lié à la soupape.
        y3(ac): Calcule le vecteur y3 dans le référentiel lié à la soupape.
        z3(ac): Calcule le vecteur z3 dans le référentiel lié à la soupape.
        y2(ac): Calcule le vecteur y2 dans le référentiel lié à la soupape.
        z2(ac): Calcule le vecteur z2 dans le référentiel lié à la soupape.
        glissement_specifique(ac, contact=None): Calcule les glissements spécifiques au contact renseigné en fonction de l'angle de rotation de la came.
        vitesse_glissement(ac, contact=None): Calcule la vitesse de glissement en fonction de l'angle de rotation de la came au contact renseigné.
        position_contact(ac, contact=None): Détermine la position du point de contact en fonction de l'angle de rotation de la came.
        vg23(ac): Calcule la vitesse de glissement pour le contact Came/Patin .
        vg12(ac): Calcule la vitesse de glissement pour le contact Came/Soupape.
        v3_ic(ac): Calcule la vitesse du point de contact Came/Patin dans le référentiel lié à la came.
        v2_ic(ac): Calcule la vitesse du point de contact Came/Patin dans le référentiel lié au levier.
        v2_is(ac): Calcule la vitesse du point de contact Soupape/Patin dans le référentiel lié au levier.
        v1_is(ac): Calcule la vitesse du point de contact Soupape/Patin dans le référentiel lié à la soupape.
        angle_y23init_n23(ac): Calcule l'angle entre le vecteur B0C et le vecteur normal en fonction de l'angle de rotation de la came.
        cos_y23init_n23(ac): Calcule le cosinus de l'angle entre le vecteur B0C et le vecteur normal en fonction de l'angle de rotation de la came.
        sgn_y23init_n23(ac): Calcule  le signe de l'angle entre le vecteur B0C et le vecteur normal en fonction de l'angle de rotation de la came.
        ci_c(ac): Détermine l'expression du vecteur reliant le centre de la came au point de contact en fonction de l'angle de rotation de la came.
        li_c(ac): Détermine l'expression du vecteur reliant le centre de rotation du linguet au point de contact avec la came en fonction de l'angle de rotation de la came.
        li_s(ac): Détermine l'expression du vecteur reliant le centre de rotation du linguet au point de contact avec la soupape en fonction de l'angle de rotation de la came.
        phi_doac(ac, pas=0.0005): Calcule la dérivée de l'angle phi par rapport à l'angle de rotation de la came et avec un pas donné.
        phi(ac): Calcule l'angle phi en fonction de l'angle de  rotation de la came.
        eta_doac(ac): Calcule la dérivée de l'angle eta par rapport à l'angle de rotation de la came.
        cb_doac(ac): Calcule la dérivée du vecteur CB par rapport à l'angle de rotation de la came et dans le référentiel lié à la soupape.
        eta(ac): Calcule l'angle eta.
        abs_angle_from_cos(cos_angle): Fonction utilitaire permet de calculer la valeur absolue dans angle à partir de son cosinus.
        cos_eta(ac): Calcule le cosinus de l'angle eta en fonction de l'angle de rotation de la came.
        sgn_eta(ac): Calcule le signe de l'angle eta en fonction de l'angle de rotation de la came.
        cb(ac): Calcule le vecteur CB en fonction de l'angle de rotation de la came.
        lb(ac): Calcule le vecteur LB en fonction de l'angle de rotation de la came.
        compute_cb0(): Calcule le vecteur CB0.
        di_soup(ac): Calcule la position du point de contact entre la soupape et son pation.
        beta_ddoac(ac): Calcule la dérivée seconde de l'angle beta par rapport à l'angle de rotation de la came.
        beta_doac(ac): Calcule la dérivée de l'angle beta par rapport à l'angle de rotation de la came.
        beta(ac): Calcule l'angle beta en fonction de l'angle de rotation de la came.
    """

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
    
    def t23(self, ac: float) -> np.ndarray:
        """
        Calcule le vecteur unitaire t23, tangent au contact entre la came et le patin en fonction de l'angle de rotation de la came. L'utilisation du produit scalaire repose sur le fait que t23 appartient à la base orthonormale directe (x, t23, n23).

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray: Vecteur t23 dans la base liée à la soupape.
        """

        return np.cross(self.n23(ac), self.x)
        
    def n23(self, ac: float) -> np.ndarray :
        """Calcule le vecteur unitaire n23, normal au contact entre la came et le patin en fonction de l'angle de rotation de la came.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray: Vecteur n23 dans la base liée à la soupape.
        """
        angle_y3_n23 = self.eta(ac) + self.phi(ac) - self.sensrot * ac
        return self.matrot(self.sensrot*ac + self.gamma0)@self.matrot(angle_y3_n23)@np.array([0, 1, 0])
    
    def y23(self, ac: float) -> np.ndarray :
        """
        Calcule le vecteur unitaire y23, colinéaire à la droite reliant le centre du patin au centre de la came et allant de B vers C.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray: Vecteur y23 dans la base liée à la soupape.
        """
        return self.matrot(self.eta(ac) + self.gamma0)@np.array([0, 1, 0])
    
    def z23(self, ac: float) -> np.ndarray :
        """
        Calcule le vecteur unitaire z23, normal à la droite reliant le centre du patin au centre de la came.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray: Vecteur z23 dans la base liée à la soupape.
        """
        return self.matrot(self.eta(ac) + self.gamma0)@np.array([0, 0, 1])
    
    def y3(self, ac: float) -> np.ndarray :
        """Calcule le vecteur unitaire y3 lié à la came.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray: Vecteur y3 dans la base liée à la soupape.
        """
        return self.matrot(self.sensrot*ac + self.gamma0)@np.array([0,1,0])
    
    def z3(self, ac: float) -> np.ndarray :
        """Calcule le vecteur unitaire z3 lié à la came.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray: Vecteur z3 dans la base liée à la soupape.
        """
        return self.matrot(self.sensrot*ac + self.gamma0)@np.array([0,0,1])
    
    def y2(self, ac: float) -> np.ndarray :
        """Calcule le vecteur unitaire y2 lié au linguet. y2 est colinéaire à la droite reliant le centre du patin côté soupape, A, au centre de rotation du linguet, L, et dans le sens A vers L.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray: Vecteur y2 dans la base liée à la soupape.
        """
        return self.matrot(self.beta(ac))@np.array([0,1,0])
    
    def z2(self, ac: float) -> np.ndarray :
        """Calcule le vecteur unitaire z2 lié au linguet. y2 est normal à la droite reliant A et L.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray: Vecteur z2 dans la base liée à la soupape.
        """
        return self.matrot(self.beta(ac))@np.array([0,0,1])

    def glissement_specifique(self, ac: float, contact: str= None ) -> np.ndarray:
        """
        Calcule les glissements spécifiques pour un angle rotation de came donné et un contact donné. Si aucun contact n'est renseigné, le glissement spécifique est calculé pour tous les contacts.
    
        Args:
            ac (float): L'angle de rotation de la came pour lequel doit être calculé le glissement spécifique.
            contact (str, optional): Le contact pour lequel doit être calculé le glissement spécifique. Ce contact est soit "Came/Patin", soit "Soupape/Patin". 

        Returns:
            np.array : Les glissements spécifiques.
        """

        if contact == "Came/Patin" :
            vg = self.vg23(ac)
            gs2 = -vg / self.v2_ic(ac)
            gs3 = vg / self.v3_ic(ac)
            return np.array([gs2, gs3])
        elif contact == "Soupape/Patin":
            gs1 = (self.lbd(ac) + self.ol[2])/(self.ol[2] + self.lbd(ac) - self.rps)
            gs2 = (self.lbd(ac) + self.ol[2])/self.rps
            return np.array([gs1, gs2])
        else :
            return np.array([
                self.glissement_specifique(ac, "Came/Patin"),
                self.glissement_specifique(ac, "Soupape/Patin")
            ])

    def vitesse_glissement(self, ac: float, contact: str= None) -> float:
        """
        Calcule la vitesse de glissement pour un angle rotation de came donné et un contact donné. Si aucun contact n'est renseigné, le vitesse de glissement est calculée pour tous les contacts.
    
        Args:
            ac (float): L'angle de rotation de la came.
            contact (str, optional): Le contact parmi "Came/Patin" et "Soupape/Patin". 

        Returns:
            float : La vitesse de glissement.
        """
        if contact == "Came/Patin" :
            return self.vg23(ac)
        elif contact == "Soupape/Patin":
            return self.vg12(ac)
        else :
            return np.array([
                self.vitesse_glissement(ac, "Came/Patin"),
                self.vitesse_glissement(ac, "Soupape/Patin")
            ])
    
    def position_contact(self, ac: float, contact: str=None) -> float:
        """
        Calule la position du point de contact au contact renseigné. Suivant le type de contact, cylindre/cylindre ou cylindre/plan, la position du point de contact peut être repérée par un angle ou par une distance à un axe (voir rapport et paramétrage des systèmes). 
    
        Args:
            ac (float): L'angle de rotation de la came.
            contact (str, optional): Le contact parmi "Came/Patin" et "Soupape/Patin". 

        Returns:
            float : ¨Position du contact. Angle CBI_c dans le cas du contact "Came/Patin". Distance SI_s dans le cas du contact "Soupape/Patin".
        """
        if contact == "Came/Patin" :
            return self.angle_y23init_n23(ac)
        elif contact == "Soupape/Patin":
            return self.di_soup(ac)
        else :
            return np.array([
                self.position_contact(ac, "Came/Patin"),
                self.position_contact(ac, "Soupape/Patin")
            ])
 
    def vg23(self, ac: float) -> float:
        """Calcule la vitesse de glissement du patin par rapport à la came.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float: Vitesse de glissement.
        """
        n23 = self.n23(ac)
        cb = self.cb(ac)
        beta_doac = self.beta_doac(ac)
        return np.einsum(
            "ij, ij -> i",
            cb - np.einsum("i, ij -> ij", beta_doac, self.lb(ac)),
            n23
            ) + self.rpc*(1 - beta_doac)

    def vg12(self, ac: float) -> float:
        """Calcule la vitesse de glissement de la soupape par rapport au patin.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float: Vitesse de glissement.
        """
        return self.beta_doac(ac) *(self.l_ling*np.sin(self.beta(ac)) + self.rps)
    
    def v3_ic(self, ac: float) -> float:
        """Calcule la vitesse du point de contact "Came/Patin" dans la base liée à la came.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float: Vitesse du point de contact "Came/Patin" dans la base liée à la came .
        """
        t23 = self.t23(ac)
        n23 = self.n23(ac)
        cb = self.cb(ac)
        cb_doac = self.cb_doac(ac)
        return np.einsum("ij , ij -> i", cb_doac, t23) + np.einsum("ij , ij -> i", cb, n23) - self.rpc*(self.phi_doac(ac) + self.eta_doac(ac) - 1)
    
    def v2_ic(self, ac: float) -> float:
        """Calcule la vitesse du point de contact "Came/Patin" dans la base liée au linguet.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float: Vitesse du point de contact "Came/Patin" dans la base liée au linguet.
        """
        return -self.rpc*(self.phi_doac(ac) + self.eta_doac(ac) - self.beta_doac(ac))

    def v2_is(self, ac: float) -> float:
        """Calcule la vitesse du point de contact "Soupape/Patin" dans la base liée au linget.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float: Vitesse du point de contact "Soupape/Patin" dans la base liée au linguet .
        """
        return - self.beta_doac(ac) *self.rps

    def v1_is(self, ac: float) -> float:
        """Calcule la vitesse du point de contact "Soupape/Patin" dans la base liée à la soupape.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float: Vitesse du point de contact "Soupape/Patin" dans la base liée à la soupape.
        """
        return self.beta_doac(ac) *self.l_ling*np.sin(self.beta(ac))

    def angle_y23init_n23(self, ac: float) -> float:
        """Calcule l'angle entre la droite (BC) et la normale au contact Came/Patin à partir du cosinus de l'angle et du signe de l'angle.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float: Angle (y23, n23).
        """
        cos_y23init_n23 = np.atleast_1d(self.cos_y23init_n23(ac))
        abs_y23init_n23 = self.abs_angle_from_cos(cos_y23init_n23)
        return self.sgn_y23init_n23(ac)*abs_y23init_n23
    
    def cos_y23init_n23(self, ac: float) -> float:
        """Calcule le cosinus de l'angle entre la droite (BC) et la normale au contact Came/Patin.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float: Cosinus de l'angle (y23, n23).
        """
        y23_init_base2 = (self.matrot(-self.beta(0))@self.y23(0)[0]).squeeze() 
        y23_init_update = self.matrot(self.beta(ac))@y23_init_base2
        return np.einsum("ij, ij -> i", y23_init_update, self.n23(ac))
    
    def sgn_y23init_n23(self, ac: float) -> int:
        """Calcule le signe de l'angle entre la droite (BC) et la normale au contact Came/Patin. Cette fonction retourne -1 si le signe est strictement négatif, 1 si le signe est strictement positif et zéro sinon.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            int : Signe de l'angle (y23, n23).
        """
        x = np.array([1, 0, 0])
        y23_init_base2 = (self.matrot(-self.beta(0))@self.y23(0)[0]).squeeze() 
        y23_init_update = self.matrot(self.beta(ac))@y23_init_base2
        return np.sign(np.dot(np.cross(y23_init_update, self.n23(ac)), x))

    def ci_c(self, ac: float) -> np.ndarray:
        """Calcule l'expression du vecteur reliant le centre de rotation de la came au point de contact Came/Patin. Cette expression est donnée dans la base liée à la soupape.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray : Vecteur CI_c dans la base liée à la soupape.
        """
        return self.cb(ac) + self.rpc*self.n23(ac)
    
    def li_c(self, ac: float) -> np.ndarray:
        """Calcule l'expression du vecteur reliant le centre de rotation du linguet au point de contact Came/Patin. Cette expression est donnée dans la base liée à la soupape.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray : Vecteur LI_c dans la base liée à la soupape.
        """
        return self.lb(ac) + self.rpc*self.n23(ac)

    def li_s(self, ac: float) -> np.ndarray:
        """Calcule l'expression du vecteur reliant le centre de rotation de la came au point de contact Soupape/Patin. Cette expression est donnée dans la base liée à la soupape.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray : Vecteur LI_s dans la base liée à la soupape.
        """
        return -self.rps*self.z1 -self.l_ling*self.y2(ac)

    def phi_doac(self, ac: float , pas: float= 0.0005) -> float:
        """Calcule une approxiamtion par différences finies de la dérivée de l'angle phi (voir la définition de l'angle dans le rapport) par rapport à l'angle de rotation de la came.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float : Dérivée de l'angle phi.
        """
        return (self.phi(ac+pas) - self.phi(ac-pas))/2/pas    
    
    def phi(self, ac: float) -> float:
        """Calcule l'angle phi (voir la définition de l'angle dans le rapport) en fonction de l'angle de rotation de la came. Pour la démonstration de la formule, voir le rapport associé. Cet angle permet de repérer la position du point de contct Came/Patin.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float : Angle phi.
        """
        cb = self.cb(ac)
        cb_doac = self.cb_doac(ac)
        eta_doac = self.eta_doac(ac)
        tan_phi = np.einsum("ij, ij -> i", cb, cb_doac)/npl.norm(cb, axis=1)**2/(1-eta_doac)
        return np.arctan(tan_phi)

    def eta_doac(self, ac: float) -> float:
        """Calcule la dérivée de l'angle eta (voir la définition de l'angle dans le rapport) par rapport l'angle de rotation de la came. Pour la démonstration de l'équation, voir le rapport associé.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float : Dérivée de eta par rapport à l'angle de roation de la came.
        """
        cos_eta = np.atleast_1d(self.cos_eta(ac))
        cb = self.cb(ac)
        cb_doac = self.cb_doac(ac)

        cos_eta_masked = np.atleast_1d(np.ma.array(np.asarray(cos_eta), mask = (cos_eta**2>=1)))
        factor1 = -self.sgn_eta(ac)/npl.norm(self.cb0)/npl.norm(cb, axis=1)/np.sqrt(1 - cos_eta_masked**2)
        factor1[cos_eta_masked.mask] = 0
        factor2 = np.einsum("ij, j -> i", cb_doac, self.cb0) - np.einsum("ij, ij -> i", cb, cb_doac)*np.einsum("ij, j -> i", cb, self.cb0)/npl.norm(cb, axis=1)**2
        return factor1 *factor2
    
    def cb_doac(self, ac: float) -> np.ndarray:
        """Calcule la dérivée du vecteur CB, par rapport à l'angle de rotation de la came dans le repère lié à la soupape.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray : Dérivée de CB par rapport à l'angle de roation de la came dans le repère lié à la soupape.
        """
        ac = np.atleast_1d(ac)
        x = np.array([1, 0, 0])
        return self.beta_doac(ac)[:, np.newaxis]*np.cross(x, self.lb(ac))
    
    def eta(self, ac: float) -> float:
        """Calcule l'angle eta en fonction de l'angle de rotation de la came.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float : Angle eta.
        """
        cos_eta = np.atleast_1d(self.cos_eta(ac))
        abs_eta = self.abs_angle_from_cos(cos_eta)
        return self.sgn_eta(ac)*abs_eta

    def abs_angle_from_cos(self, cos_angle: float) -> float:
        """Fonction utilitaire qui calcule la valeur absolue d'un angle en fonction de son cosinus.

        Args:
            cos_angle (float): Cosinus de l'angle.

        Returns:
            float : Valeur absolue de l'angle.
        """
        angle_defined = (cos_angle > -1) & (cos_angle < 1)
        angle_sup = cos_angle >= 1
        angle_inf = cos_angle <= -1
        result = np.zeros(len(cos_angle))
        result[angle_inf] = np.pi
        result[angle_defined] = np.arccos(cos_angle[angle_defined])
        result[angle_sup] = 0
        return result

    def cos_eta(self, ac: float) -> float:
        """Calcule le cosinus de l'angle eta, angle entre les vecteur y230 et y23 (voir définition dans le rapport). Ce calcule est basé sur le produit scalaire.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float: Cosinus de l'angle eta.
        """
        cb = self.cb(ac)
        return np.einsum("ij, j -> i", cb, self.cb0)/npl.norm(self.cb0)/npl.norm(cb, axis=1)
    
    def sgn_eta(self, ac: float) -> int:
        """Calcule le signe de l'angle eta, angle entre les vecteur y230 et y23 (voir définition dans le rapport). Ce calcule est basé sur le produit vectoriel.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float: Cosinus de l'angle eta.
        """
        x = np.array([1, 0, 0])
        return np.sign(np.dot(np.cross(self.cb0, self.cb(ac)), x))
    
    def cb(self, ac: float) -> np.ndarray:
        """Calcule le vecteur CB entre le centre de rotation de la came et le centre du patin en contact avec la came. L'expression finale est donnée dans la base liée à la soupape.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray : Vecteur CB dans la base liée à la soupape.
        """
        return self.cl + self.lb(ac)

    def lb(self, ac: float) -> np.ndarray:
        """Calcule le vecteur LB entre le centre de rotation du linguet et le centre du patin en contact avec la came. L'expression finale est donnée dans la base liée à la soupape. La méthode utilisée est la suivante. Connaissant le vecteur LB0 pour une levée nulle dans la base liée à la soupape, on l'exprime dans la base liée au linguet par rotation. En effet LB est constant dans cette base. On repasse ensuite dans la base liée à la soupape en faisant une rotation inverse.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray : Vecteur LB dans la base liée à la soupape.
        """
        lb_base2 = (self.matrot(-self.beta(0))@(self.cb0 - self.cl)).squeeze() 
        return self.matrot(self.beta(ac))@lb_base2
    
    def compute_cb0(self) -> np.ndarray :
        """
        Calcule le vecteur CB0. CB0 relie le centre de rotation de la came au le centre du patin à levée nulle. L'expression finale est donnée dans la base liée à la soupape.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            np.ndarray : Vecteur CB0 dans la base liée à la soupape.
        """
        y23_init = np.array([0, np.cos(self.gamma0), np.sin(self.gamma0)])
        return -(self.rb + self.rpc)*y23_init

    def di_soup(self, ac: float) -> float:
        """
        Calcule la position du point de contact en la soupape et son patin. Cette position est repérée par une distance à l'axe de révolution de la soupape. Cette distance est signée afin de repérer de quel côté de l'axe on se trouve.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float : Distance d_i_s, signée.
        """
        return self.ol[1] - self.l_ling*np.cos(self.beta(ac))
    
    def beta_ddoac(self, ac: float) -> float:
        """
        Calcule la dérivée seconde de l'angle beta d'inclinaison du linguet par rapport à l'angle de rotation de la came.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float : Dérivée seconde de l'angle beta par rapport à l'angle de rotation de la came.
        """
        beta = self.beta(ac)
        return self.lbd_ddoac(ac)/self.l_ling/np.cos(beta) + self.beta_doac(ac)**2*np.tan(beta)

    def beta_doac(self, ac: float) -> float:
        """
        Calcule la dérivée première de l'angle beta d'inclinaison du linguet par rapport à l'angle de rotation de la came. _doac signifie "derivative of angle came".

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float : Dérivée première de l'angle beta par rapport à l'angle de rotation de la came.
        """
        beta = self.beta(ac)
        lbd_doac = self.lbd_doac(ac)
        return self.sensrot*lbd_doac/np.cos(beta)/self.l_ling

    def beta(self, ac: float) -> float :
        """
        Calcule l'angle beta d'inclinaison du linguet.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float : Inclinaison du linguet.
        """
        return np.arcsin((self.lbd(ac) + self.ol[2] - self.rps)/self.l_ling)

class CalculsCinematiqueDirecte(CalculsCinematique):
    """Implémentation de CalculsCinematique pour les systèmes à attaque directe.

    Calcule un ensemble de grandeurs cinématiques pour les systèmes à attaque directe.

    Args:
        assemblage (AssemblageDirecte): Un assemblage à levier.
        loiscame (LoisCame): Les lois de distribution.

    Attributes:
        cb0 (np.ndarray): Vecteur CB à levée nulle.

    Methods:
        t12(ac): Calcule le vecteur tangent au contact Poussoir/Came.
        n12(ac): Calcule le vecteur normal au contact Poussoir/Came.
        y12(ac): Calcule le vecteur y12 dans le référentiel lié à la soupape.
        z12(ac): Calcule le vecteur z12 dans le référentiel lié à la soupape.
        y2(ac): Calcule le vecteur y2 dans le référentiel lié à la soupape.
        z2(ac): Calcule le vecteur z2 dans le référentiel lié à la soupape.
        glissement_specifique(ac, contact=None): Calcule les glissements spécifiques au contact renseigné en fonction de l'angle de rotation de la came.
        vitesse_glissement(ac, contact=None): Calcule la vitesse de glissement en fonction de l'angle de rotation de la came au contact renseigné.
        position_contact(ac, contact=None): Détermine la position du point de contact en fonction de l'angle de rotation de la came.
    """
    def __init__(self, assemblage : AssemblageDirecte, loiscame : LoisCame) -> None:
        super().__init__(assemblage, loiscame)
    
    def vitesse_glissement(self, ac, contact=None):
        pass
    
    def position_contact(self, ac, contact=None):
        pass


class CalculsCinematiqueFromCame():
    """Class permettant de calculer la cinématique du système connaissant le profil de la came.

    Contrairement à classe CalculsCinematique et ses héritières qui utilise la loi de levée comme loi entrée sortie, la classe CalculsCinematiqueFromCame utilise le profil de la came comme loi d'entrée-sortie. Cette classe est un peu avancée mais pas aboutie. Pour l'implémenter il faudra travailler davantage dessus.

    Args:
        assemblage (AssemblageLinguet): L'assemblage étudié.

    Attributes:
        x (np.ndarray): The x-axis unit vector.
        yc (np.ndarray): The y-axis unit vector.
        zc (np.ndarray): The z-axis unit vector.
        oc (np.ndarray): The coordinates of the cam.
        ol (np.ndarray): The coordinates of the lever.
        sensrot (str): The rotation direction of the cam.
        rb (float): The base radius of the cam.
        rpc (float): The curvature radius of the cam follower.
        rps (float): The curvature radius of the valve follower.
        l_ling (float): The length of the lever.
        gamma0 (float): The initial angle between the lever and cam.
        rho (callable): The profile of the cam.
        rho_doeps (callable): The first derivative of the cam profile.
        rho_ddoeps (callable): The second derivative of the cam profile.
        beta0 (float): The initial beta angle.
        lc (np.ndarray): The vector from the cam to the lever.
        norm_lc (float): The norm of the lc vector.
        lb (np.ndarray): The computed lb vector.
        norm_lb (float): The norm of the lb vector.
    """
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
        matrot = self.matrot(beta)
        y1 = self.y1(ac)
        return np.einsum("ijk, ik -> ij", matrot, y1)
    
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
        cos_delta_defined = (cos_delta >= -1) & (cos_delta <= 1)
        cos_delta_sup = cos_delta > 1
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
