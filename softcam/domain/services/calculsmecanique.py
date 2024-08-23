import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from abc import ABC, abstractmethod

import numpy as np

from domain.entities.assemblage import Assemblage, AssemblageLinguet, AssemblageDirecte
from domain.entities.loiscame import LoisCame
from domain.services.calculscinematique import CalculsCinematique, CalculsCinematiqueLevier, CalculsCinematiqueDirecte
from domain.services.calculsprofilcame import CalculsProfilCame, CalculsProfilCameLevier, CalculsProfilCameDirecte

class CalculEfforts(ABC):
    """CalculEfforts est une classe abstraite conçue pour le calcul des efforts auxquels est soumis le système.

    Cette class initialise des paramètres mécaniques communs à tous les systèmes T. Des méthodes abstraites implémentées par tous les systèmes sont également définies.

    Args:
        assemblage (Assemblage): L'assemblage créé.
        loiscame (LoisCame): Les lois de distribution créées.
        calccinematique (CalculsCinematique): Utilitaire permettant le calcul des grandeurs cinématiques.

    Properties:
        m1 (float): Masse de l'ensemble cinématique de la soupape.
        j3 (float): Moment d'inertie de la came autour de son axe de rotation.
        fs (float): Force de frottement guide-poussoir
        k (float): Raideur du ressort.
        dr (float): Precharge/Raideur = Différence entre la longueur à vide et la longeur à levée nulle et jeu nul.
        lbd (float): Levée de soupapa.
        lbd_doac (float): Vitesse de soupape.
        lbd_ddoac (float): Acceleration de soupape.

    Methods:
        force_ressort(ac): Calcule la force de rappel du ressort.
        couple_arbre(ac, regime_moteur): Méthode abstraite pour le calcul du couple sur la came.
        effort_contact(ac, regime_moteur, contact=None): Méthode abstraite pour le calcul des efforts normaux au contact indiqué.
        force_frottement(ac, regime_moteur, contact=None): Méthode abstraite pour le calcul de la force de frottement au contact indiqué.
    """

    def __init__(self, assemblage : Assemblage, loiscame : LoisCame, calccinematique : CalculsCinematique):
        
        self.__m1 = assemblage.soupape.masse_coupelle + assemblage.soupape.masse_soupape + assemblage.ressort.masse/3
        self.__j3 = assemblage.came.inertie
        self.__fs = 0
        self.__k = assemblage.ressort.raideur
        self.__dr = assemblage.ressort.precharge/assemblage.ressort.raideur

        self.__lbd = loiscame.l
        self.__lbd_doac = loiscame.v
        self.__lbd_ddoac = loiscame.a

        self.calccinematique = calccinematique
    
    @property
    def m1(self):
        return self.__m1
    @property
    def j3(self):
        return self.__j3
    @property
    def fs(self):
        return self.__fs
    @property
    def k(self):
        return self.__k
    @property
    def dr(self):
        return self.__dr
    @property
    def lbd(self):
        return self.__lbd
    @property
    def lbd_doac(self):
        return self.__lbd_doac
    @property
    def lbd_ddoac(self):
        return self.__lbd_ddoac

    def force_ressort(self, ac : float) -> float:
        """Calcul la force de rappel du ressort.

        La force de rappel du ressort est modélisée par la loi de Hooke. Cette fonction calcul d'abord la levée pour en déduire la force.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float: Force de rappel du ressort.
        """
        lbd = self.lbd(ac)
        return self.k*(lbd + self.dr)
    
    @abstractmethod
    def couple_arbre(self, ac: float, regime_moteur: float) -> float:
        pass

    @abstractmethod
    def effort_contact(self, ac: float, regime_moteur: float, contact: str= None) -> float:
        pass

    @abstractmethod
    def force_frottement(self, ac: float, regime_moteur: float, contact: str= None) -> float:
        pass

class CalculEffortsLevier(CalculEfforts):
    """Implémentation pour les systèmes à "levier" de la classe abstraite CalculEfforts.

    Cette classe calcule les efforts pour les sytèmes à levier de type linguet ou basculeur.

    Args:
        assemblage (AssemblageLinguet): L'assemblage créé. Celui-ci doit être un assemblage de type levier.
        loiscame (LoisCame): Les lois de distribution créées.
        calccinematique (CalculsCinematiqueLevier): Utilitaire permettant le calcul des grandeurs cinématiques. Doit être de type levier.

    Properties:
        mups (float): Coefficient de frottement dynamique au contact patin-soupape.
        mupc (float): Coefficient de frottement dynamique au contact patin-came.
        j2 (float): Moment d'inertie du levier autour de sont axe de rotation.

    Methods:
        couple_arbre(ac, regime_moteur): Calcule le couple sur la came.
        effort_contact(ac, regime_moteur, contact=None): Calcul l'effort normal au contact indiqué.
        force_frottement(ac, regime_moteur, contact=None): Calcul la force de frottement au contact indiqué.
    """
    def __init__(self, assemblage : AssemblageLinguet, loiscame : LoisCame, calccinematique : CalculsCinematiqueLevier):
        super().__init__(
            assemblage=assemblage,
            loiscame=loiscame,
            calccinematique=calccinematique
        )
        
        self.__mups = assemblage.frottement_patinsoupape
        self.__mupc = assemblage.frottement_patincame
        self.__j2 = assemblage.levier.inertie
        
    @property
    def mups(self):
        return self.__mups
    @property
    def mupc(self):
        return self.__mupc
    @property
    def j2(self):
        return self.__j2
    
    def couple_arbre(self, ac: float, regime_moteur: float) -> float:
        """Calcule le couple sur la came.

        Cette méthode détermine le couple créé par le moteur sur la came. La démonstration de la relation est donnée dans le rapport associé. 

        Args:
            ac (float): Angle de rotation de la came.
            regime_moteur (float): Régime moteur auquel effectuer le calcul.

        Returns:
            float: Couple sur la came.
        """
        ac_ddot = 0 # C'est l'une des hypothèses les plus importantes du modèle implémenté dans le logiciel. On considère que la vitesse de rotation de l'arbre à cames est constante.
        t23 = self.calccinematique.t23(ac)
        n23 = self.calccinematique.n23(ac)
        ci_came = self.calccinematique.ci_c(ac)
        frottement_pc = self.force_frottement(ac, regime_moteur, contact="Came/Patin")
        z23 = self.z23(ac, regime_moteur)
        return self.j3*ac_ddot - frottement_pc*np.einsum("ij, ij -> i", ci_came, n23) - z23*np.einsum("ij, ij -> i", ci_came, t23)

    def effort_contact(self, ac: float, regime_moteur: float, contact: str= None) -> float:
        """Calcule l'effort normal au contact indiqué.

        Cette méthode détermine la l'effort normal au contact indiqué, pour un angle de rotation de la came et un régime moteur donnés. Le contact est soit "Came/Patin", soit "Soupape/Patin". Si aucun contact n'est indiqué, la force de frottement est calculée pour les deux systèmes.

        Args:
            ac (float): Angle de rotation de la came.
            regime_moteur (float): Régime moteur auquel effectuer le calcul.
            contact (str, optional): La position du contact. 
                Options : "Came/Patin" et "Soupape/Patin". Si non spécifié, la force est calculée pour les deux contacts.

        Returns:
            float or np.array: Effort normal au contact.
        """
        if contact == "Came/Patin":
            return self.z23(ac, regime_moteur)
        elif contact == "Soupape/Patin":
            return self.z12(ac, regime_moteur)
        else :
            return np.array([
                self.effort_contact(ac, regime_moteur, "Came/Patin"),
                self.effort_contact(ac, regime_moteur, "Soupape/Patin")
            ])
        
    def force_frottement(self, ac: float, regime_moteur: float, contact: str= None) -> float:
        """Calcule la force de frottement au contact indiqué.

        Cette méthode détermine la force de frottement agissant sur le système au contact indiqué, pour un angle de rotation de la came et un régime moteur donnés. Le contact est soit "Came/Patin", soit "Soupape/Patin". Si aucun contact n'est indiqué, la force de frottement est calculée pour les deux systèmes. La modélisation retenue pour le calcul du frottement utilise les lois de Coulomb.

        Args:
            ac (float): Angle de rotation de la came.
            regime_moteur (float): Régime moteur auquel effectuer le calcul.
            contact (str, optional): La position du contact. 
                Options : "Came/Patin" et "Soupape/Patin". Si non spécifié, la force est calculée pour les deux contacts.

        Returns:
            float or np.array: Force de frottement.
        """
        if contact == "Came/Patin":
            return -np.sign(self.calccinematique.vg23(ac))*self.mupc*self.z23(ac, regime_moteur)
        elif contact == "Soupape/Patin":
            return -np.sign(self.calccinematique.vg12(ac=ac))*self.mups*self.z12(ac, regime_moteur)
        else :
            return np.array([
                self.force_frottement(ac, regime_moteur, "Came/Patin"),
                self.force_frottement(ac, regime_moteur, "Soupape/Patin")
            ])

    def z23(self, ac: float, regime_moteur: float) -> float:
        """Calcule l'effort normal du patin sur la came.

        Dépend de l'angle de rotation de la came et du régime moteur. Démonstration de la formule dans le rapport.

        Args:
            ac (float): Angle de rotation de la came.
            regime_moteur (float): Régime moteur auquel effectuer le calcul.

        Returns:
            float: Effort normal du patin sur la came.
        """
        frottement_patinsoupape = self.force_frottement(ac, regime_moteur, contact="Soupape/Patin")
        z12 = self.z12(ac, regime_moteur)
        li_s = self.calccinematique.li_s(ac) 
        m_l_12 = np.dot(
            np.cross(
                -np.einsum("i,j -> ij", frottement_patinsoupape, self.calccinematique.y1) + np.einsum("i,j -> ij", z12, self.calccinematique.z1), 
                li_s ), 
            self.calccinematique.x
            )

        vg23 = self.calccinematique.vg23(ac)
        li_came = self.calccinematique.li_c(ac)
        t23 = self.calccinematique.t23(ac)
        n23 = self.calccinematique.n23(ac)
        denom = np.dot(
            np.cross(
                self.mupc*np.einsum("i,ij -> ij", np.sign(vg23), t23) + n23, 
                li_came ),
            self.calccinematique.x
            )

        return (self.j2*self.calccinematique.beta_ddoac(ac)*regime_moteur**2/4 + m_l_12)/denom

    def z12(self, ac: float, regime_moteur: float) -> float:
        """Calcule l'effort normal de la soupape sur le patin.

        Dépend de l'angle de rotation de la came et du régime moteur. Démonstration de la formule dans le rapport.

        Args:
            ac (float): Angle de rotation de la came.
            regime_moteur (float): Régime moteur auquel effectuer le calcul.

        Returns:
            float: Effort normal de la soupape sur le patin.
        """
        lbd_ddoac = self.lbd_ddoac(ac)
        return self.m1*lbd_ddoac*regime_moteur**2/4 + self.force_ressort(ac) - self.fs
    
class CalculEffortsDirecte(CalculEfforts):
    """Implémentation pour les systèmes à attaque directe de la classe abstraite CalculEfforts.

    Args:
        assemblage (AssemblageDirecte): L'assemblage créé. Celui-ci doit être un assemblage de type attaque directe.
        loiscame (LoisCame): Les lois de distribution créées.
        calccinematique (CalculsCinematiqueDirecte): Utilitaire permettant le calcul des grandeurs cinématiques. Doit être de type attaque directe.

    Properties:
        mups (float): Coefficient de frottement dynamique au contact patin-soupape.

    Methods:
        couple_arbre(ac, regime_moteur): Calcule le couple sur la came. (Pas encore implémenté)
        effort_contact(ac, regime_moteur, contact=None): Calcul l'effort normal au contact indiqué. (Pas encore implémenté)
        force_frottement(ac, regime_moteur, contact=None): Calcul la force de frottement au contact indiqué. (Pas encore implémenté)
    """
    def __init__(self, assemblage : AssemblageDirecte, loiscame : LoisCame, calculscinematique : CalculsCinematiqueDirecte):
        super().__init__(
            assemblage=assemblage,
            loiscame=loiscame,
            calculscinematique=calculscinematique
        )
    
    def couple_arbre(self, ac, regime_moteur):
        pass
    def effort_contact(self, ac, regime_moteur, contact=None):
        pass
    def force_frottement(self, ac, regime_moteur, contact=None):
        pass

class CalculsMecanique(ABC):
    """CalculsMecanique est une classe abstraite pour le calcul de critères d'ordre mécanique, dynamique.

    Cette classe utilise la classe CalculEfforts définie précédemment ainsi que les utilitaires pour réaliser les calculs cinématiques et les calculs sur le profil de la came.

    Args:
        assemblage (Assemblage): L'assemblage étudié.
        loiscame (LoisCame): Les lois de distributions définies.
        calccinematique (CalculsCinematique): Utilitaire pour réaliser le calcul cinématique.
        calcprofil (CalculsProfilCame): Utilitaire pour calculer le profil de la came et toutes les grandeurs qui lui sont liées.

    Methods:
        coefficient_grippage(ac, regime_moteur, contact=None): Calcule le coefficient de grippage pour le contact indiqué.
        pression_hertz(ac, regime_moteur, contact=None): Calcule la pression de Hertz pour le contact indiqué.
        vitesse_glissement(ac, regime_moteur, contact=None): Calcule la vitesse de glissement (en m/s) pour le contact indiqué.
        effort_lineique(ac, regime_moteur, contact): Méthode abstraite pour le calcul de l'effort linéique au contact indiqué.
        courbure_equivalente(ac, contact): Méthode abstraite pour le calcul du rayon de courbure équivalent au contact indiqué.
        module_young_equivalent(contact): Méthode abstraite pour le calcul du module de Young au contact indiqué.
    """

    def __init__(self, assemblage : Assemblage, loiscame : LoisCame, calccinematique : CalculsCinematique, calcprofil : CalculsProfilCame):
        self.calccinematique = calccinematique
        self.calcprofil = calcprofil
        self.calcefforts = None
        self.soupape = assemblage.soupape
        self.came = assemblage.came

    def coefficient_grippage(self, ac: float, regime_moteur: float, contact: str= None) -> float:
        """Calcule le coefficient de grippage au contact indiqué.

        Le coefficient de grippage n'est rien d'autre que le produit de la pression de Hertz par la vitesse de glissement. Le type de contact est soit "Came/Patin" ou "Soupape/Patin" si aucun contact n'est renseigné, le coefficient de grippage est calculé pour les deux contacts.

        Args:
            ac (float): Angle de rotation de la came.
            regime_moteur (float): Régime du moteur.
            contact (str, optional): Le type de contact est soit "Came/Patin" et "Soupape/Patin".

        Returns:
            float or np.ndarray: Coefficient de grippage.
        """
        return self.pression_hertz(ac, regime_moteur, contact) *self.vitesse_glissement(ac, regime_moteur, contact)

    def pression_hertz(self, ac: float, regime_moteur: float, contact: str= None) -> float:
        """Calcule la pression de Hertz au contact indiqué.

        La pression de Hertz est un moyen d'évaluer la pression de contact. Celle-ci dépend de l'angle de rotation de la came et du régime moteur.

        Args:
            ac (float): Angle de rotation de la came.
            regime_moteur (float): Régime du moteur.
            contact (str, optional): Le type de contact est soit "Came/Patin" et "Soupape/Patin". Si aucun de ces contacts n'est renseigné, la pression de Hertz est calculée pour les deux contacts.

        Returns:
            float or np.ndarray: Pression de Hertz.
        """
        return np.sqrt(
            self.effort_lineique(ac, regime_moteur, contact) *
            self.module_young_equivalent(contact) *
            self.courbure_equivalente(ac, contact) /np.pi
            )
    
    def vitesse_glissement(self, ac: float, regime_moteur: float, contact: str= None) -> float:
        """Calcule la vitesse de glissement au contact indiqué.

        Ici la vitesse de glissement est exprimée en m/s contrairement à celle calculée à partir de l'utilitaire de calculs cinématiques.

        Args:
            ac (float): Angle de rotation de la came.
            regime_moteur (float): Régime du moteur.
            contact (str, optional): Le type de contact est soit "Came/Patin" et "Soupape/Patin". Si aucun de ces contacts n'est renseigné, la pression de Hertz est calculée pour les deux contacts.

        Returns:
            float or np.ndarray: Vitesse de glissement en m/s.
        """
        return self.calccinematique.vitesse_glissement(ac, contact)*regime_moteur

    @abstractmethod
    def effort_lineique(ac: float, regime_moteur: float, contact: str) -> float:
        pass
    @abstractmethod
    def courbure_equivalente(ac: float, contact: str) -> float:
        pass
    @abstractmethod
    def module_young_equivalent(self, contact: str) -> float:
        pass
        
class CalculsMecaniqueLevier(CalculsMecanique):
    """Implémentation de la classe abstraite CalculsMecanique pour les sytèmes utilisant un levier.

    Cette classe permet le calcul des critères de diensionnement d'ordre mécanique pour les systèmes utilisant un levier  (linguet ou basculeur).

    Args:
        assemblage (AssemblageLinguet): L'assemblage étudié qui doit être de type Levier.
        loiscame (LoisCame): Les lois de distributions définies.
        calccinematique (CalculsCinematiqueLevier): Utilitaire pour réaliser le calcul des gandeurs cinématiques des sytèmes à levier.
        calcprofil (CalculsProfilCameLevier): Utilitaire pour calculer le profil de la came pour un système à levier.

    Attributes:
        calcefforts (CalculsEffortsLevier): Utilitaire de calcul des efforts dans le système.
        patin_came (Patin): Patin du côté came.
        patin_soupape (Patin): Patin du côté soupape.

    Methods:
        effort_lineique(ac, regime_moteur, contact): Calcule de l'effort linéique au contact indiqué.
        courbure_equivalente(ac, contact): Calcule du rayon de courbure équivalent au contact indiqué.
        module_young_equivalent(contact): Calcule du module de Young au contact indiqué.
    """
    def __init__(self, assemblage : AssemblageLinguet, loiscame : LoisCame, calccinematique : CalculsCinematiqueLevier, calcprofil : CalculsProfilCameLevier):
        super().__init__(assemblage, loiscame, calccinematique, calcprofil)
        
        self.calcefforts = CalculEffortsLevier(
            assemblage=assemblage,
            loiscame=loiscame,
            calccinematique=calccinematique
        )

        self.patin_came = assemblage.levier.patin_came
        self.patin_soupape = assemblage.levier.patin_soupape

    def effort_lineique(self, ac: float, regime_mot: float, contact: str= None) -> float:
        """Calcule l'effort linéique au contact.

        L'effort linéique est la force excercée au contact, divisée par la largeur du contact.

        Args:
            ac (float): Angle de rotation de la came.
            regime_mot (float, optional): Régime moteur pour lequel les calculs sont réalisés. Defaults to 0.
            contact (str, optional): Contact auquel les calculs sont réalisés.
                Options: "Came/Patin" ou "Soupape/Patin". Si aucun des deux n'est renseigné, l'effort linéique est calcule pour les deux contacts. 

        Returns:
            float or np.ndarray: Effort linéique.
        """
        if contact == "Came/Patin" :
            longueur_contact = min(self.came.largeur, self.patin_came.largeur)
            return self.calcefforts.z23(ac, regime_mot)/longueur_contact
        elif contact == "Soupape/Patin":
            longueur_contact = min(self.soupape.diametre_soupape, self.patin_soupape.largeur)
            return self.calcefforts.z12(ac, regime_mot)/longueur_contact
        else :
            return np.array([
                self.effort_lineique(ac, regime_mot, contact="Came/Patin"), 
                self.effort_lineique(ac, regime_mot, contact="Soupape/Patin")
            ])
    
    def courbure_equivalente(self, ac: float, contact: str= None) -> float:
        """Calcule l'inverse du rayon de courbure équivalent au contact.

        Par propriété la courbure équivalente au contact est la somme des courbures de chacune des deux pièces en contact.

        Args:
            ac (float): Angle de rotation de la came.
            contact (str, optional): Contact auquel les calculs sont réalisés.
                Options: "Came/Patin" ou "Soupape/Patin". Si aucun des deux n'est renseigné, la courbure est calculée pour les deux contacts. 

        Returns:
            float or np.ndarray: Courbure équivalente
        """
        
        if contact == "Came/Patin" :
            came_rc = self.calcprofil.rayon_courbure(self.calcprofil.angle_polaire(ac))
            return 1/came_rc + 1/self.patin_came.rayon_courbure
        elif contact == "Soupape/Patin":
            return 1/self.patin_soupape.rayon_courbure *np.ones(len(ac))
        else :
            return np.array([
                self.courbure_equivalente(ac, contact="Came/Patin"), 
                self.courbure_equivalente(ac, contact="Soupape/Patin")
            ])

    def module_young_equivalent(self, contact: str= None) -> float:
        """Calcule le module d'Young équivalent pour le contact.

        Ce module d'Young équivalent dépend du module de Young et du coefficient de poisson de chacune des pièces en contact.

        Args:
            contact (str, optional): Contact auquel les calculs sont réalisés.
                Options: "Came/Patin" ou "Soupape/Patin". Si aucun des deux n'est renseigné, la courbure est calculée pour les deux contacts. 

        Returns:
            float or np.ndarray: Module de Young équivalent
        """
        if contact == "Came/Patin" :
            return ( 
                (1-self.came.coefficient_poisson**2)/self.came.module_young 
                + (1-self.patin_came.coefficient_poisson**2)/self.patin_came.module_young 
                )**(-1)
        elif contact == "Soupape/Patin":
            return ( 
                (1-self.soupape.coefficient_poisson**2)/self.soupape.module_young 
                + (1-self.patin_soupape.coefficient_poisson**2)/self.patin_soupape.module_young 
                )**(-1)
        else :
            return np.array([
                [self.module_young_equivalent(contact="Came/Patin")], 
                [self.module_young_equivalent(contact="Soupape/Patin")]
                ])

class CalculsMecaniqueDirecte(CalculsMecanique):
    """Implémentation de la classe abstraite CalculsMecanique pour les sytèmes à attaque directe.

    Cette classe permet le calcul des critères de dimensionnement d'ordre mécanique pour les systèmes à attaque directe.

    Args:
        assemblage (AssemblageDirecte): L'assemblage étudié qui doit être de type Levier.
        loiscame (LoisCame): Les lois de distributions définies.
        calccinematique (CalculsCinematiqueDirecte): Utilitaire pour réaliser le calcul des gandeurs cinématiques des sytèmes à attaque directe.
        calcprofil (CalculsProfilCameDirecte): Utilitaire pour calculer le profil de la came pour un système à attaque directe.

    Attributes:
        calcefforts (CalculsEffortsDirecte): Utilitaire de calcul des efforts dans le système.
        poussoir (Poussoir): Poussoir de l'assemblage étudié.
        
    Methods:
        effort_lineique(ac, regime_moteur, contact): Calcule de l'effort linéique au contact indiqué.
        courbure_equivalente(ac, contact): Calcule du rayon de courbure équivalent au contact indiqué.
        module_young_equivalent(contact): Calcule du module de Young au contact indiqué.
    """
    def __init__(self, assemblage : AssemblageDirecte, loiscame : LoisCame, calccinematique : CalculsCinematiqueDirecte, calcprofil : CalculsProfilCameDirecte):
        super().__init__(assemblage, loiscame, calccinematique, calcprofil)
        
        self.calcefforts = CalculEffortsDirecte(
            assemblage=assemblage,
            loiscame=loiscame,
            calccinematique=calccinematique
        )

        self.poussoir = assemblage.soupape.poussoir

    def effort_lineique(self, ac, regime_mot, contact=None):
        pass
    
    def courbure_equivalente(self, ac, contact=None):
        pass

    def module_young_equivalent(self, contact=None):
        pass