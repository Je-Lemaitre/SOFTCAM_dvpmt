
from abc import ABC, abstractmethod

import numpy as np

from domain.entities.assemblage import Assemblage, AssemblageLinguet, AssemblageDirecte
from domain.entities.loiscame import LoisCame
from domain.services.calculscinematique import CalculsCinematique, CalculsCinematiqueLevier, CalculsCinematiqueDirecte
from domain.services.calculsprofilcame import CalculsProfilCame, CalculsProfilCameLevier, CalculsProfilCameDirecte

class CalculEfforts(ABC):
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

    def force_ressort(self, ac):
        lbd = self.lbd(ac)
        return self.k*(lbd + self.dr)
    
    @abstractmethod
    def couple_arbre(self, ac, regime_moteur):
        pass

    @abstractmethod
    def effort_contact(self, ac, regime_moteur, contact=None):
        pass

    @abstractmethod
    def force_frottement(self, ac, regime_moteur, contact=None):
        pass

class CalculEffortsLevier(CalculEfforts):
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
    
    def couple_arbre(self, ac, regime_moteur):
        ac_ddot = 0 # C'est l'une des hypothèses les plus importantes du modèle implémenté dans le logiciel. On considère que la vitesse de rotation de l'arbre à cames est constante.
        t23 = self.calccinematique.t23(ac)
        n23 = self.calccinematique.n23(ac)
        ci_came = self.calccinematique.ci_came(ac)
        frottement_pc = self.force_frottement(ac, regime_moteur, contact="Came/Patin")
        z23 = self.z23(ac, regime_moteur)
        return self.j3*ac_ddot - frottement_pc*np.einsum("ij, ij -> i", ci_came, n23) - z23*np.einsum("ij, ij -> i", ci_came, t23)

    def effort_contact(self, ac, regime_moteur, contact=None):
        if contact == "Came/Patin":
            return self.z23(ac, regime_moteur)
        elif contact == "Soupape/Patin":
            return self.z12(ac, regime_moteur)
        else :
            return np.array([
                self.effort_contact(ac, regime_moteur, "Came/Patin"),
                self.effort_contact(ac, regime_moteur, "Soupape/Patin")
            ])
    def force_frottement(self, ac, regime_moteur, contact=None):
        if contact == "Came/Patin":
            return -np.sign(self.calccinematique.vg23(ac))*self.mupc*self.z23(ac, regime_moteur)
        elif contact == "Soupape/Patin":
            return -np.sign(self.calccinematique.vg12(ac=ac))*self.mups*self.z12(ac, regime_moteur)
        else :
            return np.array([
                self.force_frottement(ac, regime_moteur, "Came/Patin"),
                self.force_frottement(ac, regime_moteur, "Soupape/Patin")
            ])

    def z23(self, ac, regime_moteur):
        frottement_patinsoupape = self.force_frottement(ac, regime_moteur, contact="Soupape/Patin")
        z12 = self.z12(ac, regime_moteur)
        li = self.calccinematique.li(ac) 
        m_l_12 = np.dot(
            np.cross(
                -np.einsum("i,j -> ij", frottement_patinsoupape, self.calccinematique.y1) + np.einsum("i,j -> ij", z12, self.calccinematique.z1), 
                li ), 
            self.calccinematique.x
            )

        vg23 = self.calccinematique.vg23(ac)
        li_came = self.calccinematique.li_came(ac)
        t23 = self.calccinematique.t23(ac)
        n23 = self.calccinematique.n23(ac)
        denom = np.dot(
            np.cross(
                self.mupc*np.einsum("i,ij -> ij", np.sign(vg23), t23) + n23, 
                li_came ),
            self.calccinematique.x
            )

        return (self.j2*self.calccinematique.beta_ddoac(ac)*regime_moteur**2/4 + m_l_12)/denom

    def z12(self, ac, regime_moteur):
        lbd_ddoac = self.lbd_ddoac(ac)
        return self.m1*lbd_ddoac*regime_moteur**2/4 + self.force_ressort(ac) - self.fs
    
class CalculEffortsDirecte(CalculEfforts):
    def __init__(self, assemblage : AssemblageDirecte, loiscame : LoisCame, calculscinematique : CalculsCinematiqueLevier):
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
    def __init__(self, assemblage : Assemblage, loiscame : LoisCame, calccinematique : CalculsCinematique, calcprofil : CalculsProfilCame):
        self.calccinematique = calccinematique
        self.calcprofil = calcprofil
        self.calcefforts = None
        self.soupape = assemblage.soupape
        self.came = assemblage.came

    def coefficient_grippage(self, ac, regime_moteur, contact=None):
        return self.pression_hertz(ac, regime_moteur, contact) *self.vitesse_glissement(ac, regime_moteur, contact)

    def pression_hertz(self, ac, regime_moteur, contact=None):
        return np.sqrt(
            self.effort_lineique(ac, regime_moteur, contact) 
            *self.module_young_equivalent(contact) 
            *self.courbure_equivalente(ac, contact) /np.pi
            )
    
    def vitesse_glissement(self, ac, regime_moteur, contact=None):
        return self.calccinematique.vitesse_glissement(ac, contact)*regime_moteur

    @abstractmethod
    def effort_lineique(ac, regime_mot, contact=None):
        pass
    @abstractmethod
    def courbure_equivalente(ac, contact=None):
        pass
    @abstractmethod
    def module_young_equivalent(self, contact=None):
        pass
        
class CalculsMecaniqueLevier(CalculsMecanique):
    def __init__(self, assemblage : AssemblageLinguet, loiscame : LoisCame, calccinematique : CalculsCinematiqueLevier, calcprofil : CalculsProfilCameLevier):
        super().__init__(assemblage, loiscame, calccinematique, calcprofil)
        
        self.calcefforts = CalculEffortsLevier(
            assemblage=assemblage,
            loiscame=loiscame,
            calccinematique=calccinematique
        )

        self.patin_came = assemblage.levier.patin_came
        self.patin_soupape = assemblage.levier.patin_soupape

    def effort_lineique(self, ac, regime_mot, contact=None):
        """Calcul l'effort linéique au contact.

        Args:
            ac (float): Angle de rotation de la came
            regime_mot (float, optional): Régime moteur pour lequel les calculs sont réalisés. Defaults to 0.

        Returns:
            float: Effort linéique.
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
    
    def courbure_equivalente(self, ac, contact=None):
        """Calcul l'inverse du rayon de courbure équivalent au contact.

        Args:
            ac (float): Angle de rotation de la came.

        Returns:
            float: Rayon de Courbure Equivalent
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

    def module_young_equivalent(self, contact=None):
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