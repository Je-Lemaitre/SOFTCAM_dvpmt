from domain.entities.ressort import Ressort
from application.interfaces.controller_interface import ControllerInterface

class MetAJourRessort():
    def __init__(self, controller : ControllerInterface):
        self.controller = controller
        self.ressort = controller.current_study.assemblage.ressort

    def __call__(
            self,
            masse : float,
            raideur : float,
            precharge : float
        ):

        self.ressort.masse = masse
        self.ressort.raideur = raideur
        self.ressort.precharge = precharge