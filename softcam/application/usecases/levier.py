from domain.entities.levier import Levier
from application.interfaces.controller_interface import ControllerInterface

class MetAJourLevier():
    def __init__(self, controller : ControllerInterface):
        self.controller = controller
        self.levier = controller.current_study.assemblage.levier

    def __call__(
            self,
            masse : float,
            inertie : float,
            longueur : float
        ):
        self.levier.masse = masse
        self.levier.inertie = inertie
        self.levier.longueur = longueur

class MetAJourPatinSoupape():
    def __init__(self, controller : ControllerInterface):
        self.controller = controller
        self.patinsoupape = controller.current_study.assemblage.levier.patin_soupape

    def __call__(
            self,
            rayon_courbure : float,
            largeur : float,
            module_young : float,
            coefficient_poisson : float
        ):
        self.patinsoupape.rayon_courbure = rayon_courbure
        self.patinsoupape.largeur = largeur
        self.patinsoupape.module_young = module_young
        self.patinsoupape.coefficient_poisson = coefficient_poisson

class MetAJourPatinCame():
    def __init__(self, controller : ControllerInterface):
        self.controller = controller
        self.patincame = controller.current_study.assemblage.levier.patin_came

    def __call__(
            self,
            rayon_courbure : float,
            largeur : float,
            module_young : float,
            coefficient_poisson : float
        ):
        self.patincame.rayon_courbure = rayon_courbure
        self.patincame.largeur = largeur
        self.patincame.module_young = module_young
        self.patincame.coefficient_poisson = coefficient_poisson

