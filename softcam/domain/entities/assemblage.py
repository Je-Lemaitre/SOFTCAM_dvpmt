import dataclasses
from abc import ABC, abstractmethod
import numpy as np

from domain.services.unitees import DEGREE_TO_RADIAN, RPM_TO_RADPSEC, MEGAPASCAL_TO_PASCAL
from domain.entities.came import Came
from domain.entities.levier import Levier
from domain.entities.ressort import Ressort
from domain.entities.soupape import Soupape

@dataclasses.dataclass
class Assemblage(ABC):
    sens_rotation_came : float = 1
    soupape : Soupape = dataclasses.field(default_factory= lambda: Soupape())
    coords_soupape : np.ndarray = dataclasses.field(default_factory= lambda: np.array([0.0, 0.0, 0.0]))
    inclinaison_soupape : float = 0
    ressort : Ressort = dataclasses.field(default_factory= lambda: Ressort())
    levier : Levier = None
    came : Came = dataclasses.field(default_factory= lambda: Came())
    jeu : float = 0.0

    @abstractmethod
    def __post_init__(self):
        """Fonction appelée à l'initialisation de l'instance. Permet notamment de faire les tests pour vérifier la cohérence des paramètres."""
    
    @classmethod
    def from_dict(cls, d):
        if d["levier"] is None :
            return AssemblageDirecte.from_dict(d)
        else :
            return AssemblageLinguet.from_dict(d)
    
    @abstractmethod
    def to_dict(self):
        return dataclasses.asdict(self)

@dataclasses.dataclass
class AssemblageLinguet(Assemblage):
    levier : Levier = dataclasses.field(default_factory= lambda: Levier())
    coords_levier : np.ndarray = dataclasses.field(default_factory= lambda: np.array([0.0, 35.6e-3, 5.4e-3]))
    coords_came : np.ndarray = dataclasses.field(default_factory= lambda: np.array([0.0, 14.2e-3, 31.7e-3]))
    angle_leviercame_init: float = 5.3 *DEGREE_TO_RADIAN
    angles_limites_patinsoupape : tuple = (25,35)
    angles_limites_patincame : tuple = (20,25)
    frottement_patinsoupape : float = 0.2
    frottement_patincame : float = 0.2

    def __post_init__(self):
        pass
    
    @classmethod
    def from_dict(cls, d):
        return cls(
            sens_rotation_came = d["sens_rotation_came"],
            soupape = Soupape.from_dict(d["soupape"]),
            coords_soupape = np.array(d["coords_soupape"]),
            inclinaison_soupape = d["inclinaison_soupape"],
            ressort = Ressort.from_dict(d["ressort"]),
            levier = Levier.from_dict(d["levier"]),
            coords_levier = np.array(d["coords_levier"]),
            came = Came.from_dict(d["came"]),
            coords_came = np.array(d["coords_came"]),
            angle_leviercame_init = d["angle_leviercame_init"],
            frottement_patinsoupape = d["frottement_patinsoupape"],
            frottement_patincame = d["frottement_patincame"],
            angles_limites_patinsoupape = d["angles_limites_patinsoupape"],
            angles_limites_patincame = d["angles_limites_patincame"],
            jeu = d["jeu"]
        )
    
    def to_dict(self):
        return {
            "sens_rotation_came" : self.sens_rotation_came,
            "soupape" : self.soupape.to_dict(),
            "coords_soupape" : list(self.coords_soupape),
            "inclinaison_soupape" : self.inclinaison_soupape,
            "ressort" : self.ressort.to_dict(),
            "levier" : self.levier.to_dict(),
            "coords_levier" : list(self.coords_levier),
            "came" : self.came.to_dict(),
            "coords_came" : list(self.coords_came),
            "angle_leviercame_init" : self.angle_leviercame_init,
            "frottement_patinsoupape" : self.frottement_patinsoupape,
            "frottement_patincame" : self.frottement_patincame,
            "angles_limites_patinsoupape" : list(self.angles_limites_patinsoupape),
            "angles_limites_patincame" : list(self.angles_limites_patincame),
            "jeu" : self.jeu
        }

@dataclasses.dataclass
class AssemblageDirecte(Assemblage):
    offset : float = 0
    frottement_poussoircame : float = 0.2

    def __post_init__(self):
        pass
    
    @classmethod
    def from_dict(cls, d):
        return cls(
            sens_rotation_came = d["sens_rotation_came"],
            soupape = Soupape.from_dict(d["soupape"]),
            coords_soupape = np.array(d["coords_soupape"]),
            inclinaison_soupape = d["inclinaison_soupape"],
            ressort = Ressort.from_dict(d["ressort"]),
            levier = None,
            came = Came.from_dict(d["came"]),
            offset = d["offset"],
            frottement_poussoircame = d["frottement_poussoircame"],
            jeu = d["jeu"]
        )
    
    def to_dict(self):
        return {
            "sens_rotation_came" : self.sens_rotation_came,
            "soupape" : self.soupape.to_dict(),
            "coords_soupape" : list(self.coords_soupape),
            "inclinaison_soupape" : self.inclinaison_soupape,
            "ressort" : self.ressort.to_dict(),
            "levier" : None,
            "came" : self.came.to_dict(),
            "offset" : self.offset,
            "frottement_poussoircame" : self.frottement_poussoircame,
            "jeu" : self.jeu
        }