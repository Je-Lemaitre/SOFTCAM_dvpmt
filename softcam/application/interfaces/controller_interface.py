import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from abc import ABC, abstractmethod

from domain.entities.etude import Etude
from domain.entities.loiscame import LoisCame
from domain.services.calculscinematique import CalculsCinematique
from domain.services.calculsprofilcame import CalculsProfilCame
from domain.services.calculsmecanique import CalculsMecanique

class ControllerInterface(ABC):
    """Classe abstraite définissant les attributs que doivent posséder et les méthodes que doivent implémenter tous les contrôleurs de l'application.

    Cette classe permet de mettre en place le principe d'inversion des dépendances.

    Args:
        study (Etude, optional): L'étude chargée dans l'application. None par défaut.

    Attributes:
        current_study (Etude): L'étude chargée dans l'application.
        current_laws (LoisCame): Les lois de distribution utilisé pour le dimensionnement.
        calccinematique (CalculsCinematique): Utilitaire pour réaliser les calculs d'ordre cinématique.
        calcprofil (CalculsProfilCame): Utilitaire pour réaliser les calculs liés au profil de la came.
        calcmecanique (CalculsMecanique): Utilitaire pour réaliser les calculs d'ordre mécanique.
        precision (float): Précision sur l'angle de rotation de la came utilisé pour réaliser les calculs et l'affichage, 0.001 par défaut.
    """
    def __init__(self, study : Etude = None):
        self.current_study = study
        self.current_laws = LoisCame()
        self.calccinematique = CalculsCinematique()
        self.calcprofil = CalculsProfilCame()
        self.calcmecanique = CalculsMecanique()
        self.precision = 0.001