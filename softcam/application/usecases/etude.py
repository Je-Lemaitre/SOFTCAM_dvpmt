import uuid

import numpy as np

from domain.entities.etude import Etude
from domain.entities.assemblage import AssemblageLinguet
from domain.entities.loiscame import LoisCame
from domain.services.calculsmecanique import CalculsMecanique, CalculsMecaniqueLevier, CalculsMecaniqueDirecte
from domain.services.calculscinematique import CalculsCinematique, CalculsCinematiqueLevier, CalculsCinematiqueDirecte
from domain.services.calculsprofilcame import CalculsProfilCame, CalculsProfilCameLevier, CalculsProfilCameDirecte
from application.interfaces.repository_interface import RepositoryInterface
from application.interfaces.controller_interface import ControllerInterface

class CreeEtude():
    def __init__(self, init_repository : RepositoryInterface):
        self.init_repo = init_repository
    
    def __call__(self, name, type_assemblage, step_time) -> Etude :
        study = self.init_repo.load_data()
        one_id = uuid.uuid4()
        study.id = one_id
        study.nom = name
        study.type_assemblage = type_assemblage
        study.pas_temporel = step_time
        return study

class EnregistreEtude():
    def __init__(self, repository : RepositoryInterface):
        self.repo = repository
    
    def __call__(self, study : Etude):
        self.repo.save_data(study)

class ChargeEtude():
    def __init__(self, repository : RepositoryInterface):
        self.repo = repository
    
    def __call__(self) -> Etude :
        return self.repo.load_data()

class ExportExcel():
    def __init__(self, controller : ControllerInterface):
        self.controller = controller

    def __call__(self):
        pass

class CreeUtilitairesCalcul() :
    def __init__(self, controller : ControllerInterface):
        self.study = controller.current_study

    def __call__(self, angles_rotation_evalpts):
        if self.study.type_assemblage == "Linguet / Basculeur":
            calccinematique = CalculsCinematiqueLevier(
                assemblage=self.study.assemblage,
                loiscame=self.study.loiscame
            )

            calcprofil = CalculsProfilCameLevier(
                assemblage = self.study.assemblage,
                loiscame = self.study.loiscame,
                calccinematique = calccinematique,
                ac_evalpts=angles_rotation_evalpts
            )

            calcmecanique = CalculsMecaniqueLevier(
                assemblage=self.study.assemblage,
                loiscame=self.study.loiscame,
                calccinematique=calccinematique,
                calcprofil=calcprofil
            )
        
        return calccinematique, calcprofil, calcmecanique
    
class CalculPositionContact():
    def __init__(self, controller : ControllerInterface):
        self.calccinematique = controller.calccinematique
    
    def __call__(self, angles_rotation, contact = None):
        return self.calccinematique.position_contact(angles_rotation, contact)
    
class CalculVitesseGlissement():
    def __init__(self, controller : ControllerInterface):
        self.calcmecanique = controller.calcmecanique
    
    def __call__(self, angles_rotation, regime_moteur : float = 785, contact : str = None):
        return self.calcmecanique.vitesse_glissement(angles_rotation, regime_moteur, contact)


class CalculPressionHertz():
    def __init__(self, controller : ControllerInterface):
        self.calcmecanique = controller.calcmecanique

    def __call__(self, angles_rotation, regime_moteur : float = 785, contact : str = None) -> np.ndarray :
        
        return self.calcmecanique.pression_hertz(angles_rotation, regime_moteur, contact)