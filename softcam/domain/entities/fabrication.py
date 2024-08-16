import dataclasses
from abc import ABC, abstractmethod
import numpy as np

@dataclasses.dataclass
class Courbure():
    rayon_courbure : np.ndarray = None
    diametre_meule_taillage : float = 0.05
    estvalide : bool = False
    
    @classmethod
    def from_dict(cls, d):
        return Courbure(
            rayon_courbure = np.array(d["rayon_courbure"]),
            diametre_meule_taillage = d["diametre_meule_taillage"],
            estvalide = d["estvalide"]
        )
    
    def to_dict(self):
        return dataclasses.asdict(self)
    
@dataclasses.dataclass
class Roller():
    rayon_roller : float = 0.0085
    deplacement_roller : np.ndarray = None
    
    @classmethod
    def from_dict(cls, d):
        return Roller(
            rayon_roller = d["rayon_roller"],
            deplacement_roller = np.array(d["deplacement_roller"])
        )
    
    def to_dict(self):
        return dataclasses.asdict(self)
    
@dataclasses.dataclass
class Fabrication():
    courbure : Courbure
    roller : Roller
    
    @classmethod
    def from_dict(cls, d):
        return Fabrication(
            courbure = Courbure.from_dict(d["courbure"]),
            roller = Roller.from_dict(d["roller"])
        )
    
    def to_dict(self):
        return {
            "courbure" : self.courbure.to_dict(),
            "roller" : self.roller.to_dict()
        }