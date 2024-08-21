import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from domain.entities.soupape import Soupape, Poussoir
from application.interfaces.controller_interface import ControllerInterface

class MetAJourSoupape():
    def __init__(self, controller : ControllerInterface):
        self.controller = controller
        self.soupape = controller.current_study.assemblage.soupape

    def __call__(
            self,
            masse_soupape : float,
            masse_coupelle : float,
            diametre_soupape : float,
            poussoir : Poussoir,
            module_young : float,
            coefficient_poisson : float
        ):
        self.soupape.masse_soupape = masse_soupape
        self.soupape.masse_coupelle = masse_coupelle
        self.soupape.diametre_soupape = diametre_soupape
        self.soupape.poussoir = poussoir
        self.soupape.module_young = module_young
        self.soupape.coefficient_poisson = coefficient_poisson


class MetAJourPoussoir():
    def __init__(self, controller : ControllerInterface):
        self.controller = controller
        self.poussoir = controller.current_study.assemblage.soupape.poussoir

    def __call__(
            self,
            masse : float,
            diametre : float,
            rayon_courbure : float,
            largeur_courbure : float,
            frottement_poussoir_guide : float
        ):
        if self.poussoir is None :
            self.poussoir = Poussoir(
                masse = masse,
                diametre = diametre,
                rayon_courbure = rayon_courbure,
                largeur_courbure = largeur_courbure,
                frottement_poussoir_guide = frottement_poussoir_guide
            )
        else :
            self.poussoir.masse = masse,
            self.poussoir.diametre = diametre,
            self.poussoir.rayon_courbure = rayon_courbure,
            self.poussoir.largeur_courbure = largeur_courbure,
            self.poussoir.frottement_poussoir_guide = frottement_poussoir_guide
        
        return self.poussoir