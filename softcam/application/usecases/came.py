import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import numpy as np
import scipy.interpolate as scitp

from application.interfaces.controller_interface import ControllerInterface
from application.interfaces.repository_interface import RepositoryInterface

class ChargeProfil():
    """Classe correspondant au cas d'usage "chargement d'un profil de came".

    Cette classe charge une profil de came à partir de valeur stockée.

    Args:
        repository (RepositoryInterface): Le repository permettant l'accès aux données stockées pour le profil.

    Attributes:
        repo (object): Le repository permettant l'accès aux données stockées pour le profil.

    Methods:
        __call__(profile_path: str):
            Charge le profil de la came dans le logiciel.
    """
    def __init__(self, repository : RepositoryInterface):
        self.repo = repository
    
    def __call__(self, profile_path):
        return scitp.BSpline(self.repo.load_profile(profile_path))

class MetAJourCame():
    def __init__(self, controller : ControllerInterface):
        self.controller = controller
        self.came = controller.current_study.assemblage.came

    def __call__(
            self,
            rayon_base : float,
            largeur : float,
            module_young : float,
            coefficient_poisson : float,
            profil : scitp.BSpline
        ):

        self.came.rayon_base = rayon_base
        self.came.largeur = largeur
        self.came.module_young = module_young
        self.came.coefficient_poisson = coefficient_poisson
        self.came.profil = profil

class MetAJourProfil():
    def __init__(self, controller : ControllerInterface):
        self.controller = controller
        self.came = controller.current_study.assemblage.came

    def __call__(self, profil : scitp.BSpline):
        self.came.profil = profil

class CalculProfil():
    """Classe pour le cas d'usage "Affichage du profil de la came".

    Cette classe implémente des méthode permettant le calcul du profil de la came en coordonnées cartésiennes afin de pouvoir l'afficher.

    Args:
        controller (ControllerInterface): Contrôleur de l'application.

    Attributes:
        duree_levee (float): Durée totale durant laquelle la loi de levée à jeu nul n'est pas nulle.
        angles_evalpts (np.ndarray): Angles de rotation de la came pour lesquels seront calculés les points du profil.
        calcprofil (CalculsProfilCame): Instance de l'utilitaire de calcul du profil de la came (CalculsProfilCame).

    Methods:
        __call__() -> np.ndarray:
            Calcule les coordonnées cartésiennes, dans le repère lié à la came, des points du profil pour les angles de rotation entrés en paramètre.
    """
    def __init__(self, controller : ControllerInterface) -> None:
        self.duree_levee = controller.current_study.loiscame.dac_leveemax_ouverture + controller.current_study.loiscame.dac_leveemax_fermeture
        self.angles_evalpts = np.arange(0, self.duree_levee, controller.precision)
        self.calcprofil = controller.calcprofil

    def __call__(self) -> np.ndarray:
        return self.calcprofil.profil_cartesien(self.angles_evalpts)

class CalculRayonCourbure():
    """Classe pour le cas d'usage "Calcul du rayon de courbure du profil de la came".

    This class computes the curvature radius of a profile based on the polar 
    angles derived from the rotation angles of the cam. It provides a method 
    to obtain both the polar angles and their corresponding curvature radii.

    Args:
        controller (ControllerInterface): Contrôleur de l'application.

    Attributes:
        calcprofil (CalculsProfilCame): Instance de l'utilitaire de calcul du profil de la came (CalculsProfilCame).

    Methods:
        __call__(angles_rotation: np.ndarray) -> np.ndarray:
            Calcule l'angle polaire et le rayon de courbure pour les angles de rotation passés en paramètre.
    """
    def __init__(self, controller: ControllerInterface):
        self.calcprofil = controller.calcprofil

    def __call__(self, angles_rotation: np.ndarray) -> np.ndarray :
        """Calcule les angles polaires et les rayons de courbure pour les angles de rotation de came renseignés.

        Cette méthode utilise l'utilitaire réalisant les calculs liés au profil de la came, CalculsProfilCame

        Args:
            angles_rotation (np.ndarray): Angles de rotation de la came.

        Returns:
            np.ndarray: Array 2D contenant les angles polaires puis les rayons de courbure associés.
        """
        angle_polaire = self.calcprofil.angle_polaire(angles_rotation)
        rayon_courbure = self.calcprofil.rayon_courbure(angle_polaire)
        
        return np.array([angle_polaire, rayon_courbure]).T
    
class CalculRollerDisplacement():
    """Classe correspondant au cas d'usage "Génération d'un fichier roller".

    Cette classe calcule les coordonnées polaires du centre du roller. Ce sont ces coordonnées qui sont renseignées dans le fichier roller.

    Args:
        controller (ControllerInterface): Contrôleur de l'application.

    Attributes:
        calcprofil (CalculsProfilCame): Instance de l'utilitaire de calcul du profil de la came (CalculsProfilCame).

    Methods:
        __call__(angles_rotation: np.ndarray, rayon_roller: float) -> np.ndarray:
            Calcule les coordonnées polaires du centre du roller.
    """
    def __init__(self, controller : ControllerInterface):
        self.calcprofil = controller.calcprofil

    def __call__(self, angles_rotation: np.ndarray, rayon_roller : float) -> np.ndarray:
        """Calcule les coordonnées polaires du centre du roller dans le référentiel lié à la came.

        Cette fonction est associée au cas d'usage "Génération d'un fichier roller".

        Args:
            angles_rotation (array-like): Les angles de rotation de la came pour lesquels sont calculés la position du roller.
            rayon_roller (float): Le rayon du roller (8.5mm par défaut).

        Returns:
            np.ndarray: Un array contenant les angles polaires puis les rayons polaire permettant de repérer le centre du roller associé aux angles de rotation passés en paramètre.
        """
        angle_polaire, deplacement = self.calcprofil.position_polaire_roller(angles_rotation, rayon_roller)

        return np.array([angle_polaire, deplacement]).T