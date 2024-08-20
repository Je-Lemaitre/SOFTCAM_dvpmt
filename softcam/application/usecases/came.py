import numpy as np
import scipy.interpolate as scitp

from application.interfaces.controller_interface import ControllerInterface
from application.interfaces.repository_interface import RepositoryInterface

class ChargeProfil():
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
    def __init__(self, controller : ControllerInterface) -> None:
        self.duree_levee = controller.current_study.loiscame.dac_leveemax_ouverture + controller.current_study.loiscame.dac_leveemax_fermeture
        self.angles_evalpts = np.arange(0, self.duree_levee, controller.precision)
        self.calcprofil = controller.calcprofil

    def __call__(self):
        return self.calcprofil.profil_cartesien(self.angles_evalpts)

class CalculRayonCourbure():
    def __init__(self, controller : ControllerInterface):
        self.calcprofil = controller.calcprofil

    def __call__(self, angles_rotation) -> np.ndarray :
        angle_polaire = self.calcprofil.angle_polaire(angles_rotation)
        rayon_courbure = self.calcprofil.rayon_courbure(angle_polaire)
        
        return np.array([angle_polaire, rayon_courbure]).T
    
class CalculRollerDisplacement():
    def __init__(self, controller : ControllerInterface):
        self.calcprofil = controller.calcprofil

    def __call__(self, angles_rotation, rayon_roller : float):
        angle_polaire, deplacement = self.calcprofil.position_polaire_roller(angles_rotation, rayon_roller)

        return np.array([angle_polaire, deplacement]).T