from abc import ABC, abstractmethod

from domain.entities.etude import Etude
from domain.entities.loiscame import LoisCame
from domain.services.calculscinematique import CalculsCinematique
from domain.services.calculsprofilcame import CalculsProfilCame
from domain.services.calculsmecanique import CalculsMecanique

class ControllerInterface(ABC):
    def __init__(self, study : Etude = None):
        self.current_study = study
        self.current_laws = LoisCame()
        self.calccinematique = CalculsCinematique()
        self.calcprofil = CalculsProfilCame()
        self.calcmecanique = CalculsMecanique()
        self.precision = 0.001