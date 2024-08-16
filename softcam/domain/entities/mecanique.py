import dataclasses
from abc import ABC, abstractmethod
import numpy as np

@dataclasses.dataclass
class Cinematique():
    position_contact_camepatin : np.ndarray = None
    position_contact_soupapepatin : np.ndarray = None
    vitesse_balayage_camepatin : np.ndarray = None
    vitesse_balayage_soupapepatin : np.ndarray = None
    vitesse_balayage_limite : float = 1
    estvalide : bool = False

    @classmethod
    def from_dict(cls, d):
        return Cinematique(
            position_contact_camepatin = np.array(d["position_contact_camepatin"]),
            position_contact_soupapepatin = np.array(d["position_contact_soupapepatin"]),
            vitesse_balayage_camepatin = np.array(d["vitesse_balayage_camepatin"]),
            vitesse_balayage_soupapepatin = np.array(d["vitesse_balayage_soupapepatin"]),
            vitesse_balayage_limite = d["vitesse_balayage_limite"],
            estvalide = d["estvalide"],
        )
    
    def to_dict(self):
        return dataclasses.asdict(self)

@dataclasses.dataclass
class Efforts():
    phertz_camepatin : np.ndarray = None
    phertz_soupapepatin : np.ndarray = None
    pression_hertz_limite : float = 850e6
    phertz_estvalide : bool = False
    coefficient_grippage_camepatin : np.ndarray = None
    coefficient_grippage_soupapepatin : np.ndarray = None
    coefficient_grippage_estvalide : bool = False

    @classmethod
    def from_dict(cls, d):
        return Efforts(
            phertz_camepatin = np.array(d["phertz_camepatin"]),
            phertz_soupapepatin = np.array(d["phertz_soupapepatin"]),
            pression_hertz_limite = d["pression_hertz_limite"],
            phertz_estvalide = d["phertz_estvalide"],
            coefficient_grippage_camepatin = np.array(d["coefficient_grippage_camepatin"]),
            coefficient_grippage_soupapepatin = np.array(d["coefficient_grippage_soupapepatin"]),
            coefficient_grippage_estvalide = d["coefficient_grippage_estvalide"]
        )
    
    def to_dict(self):
        return dataclasses.asdict(self)

@dataclasses.dataclass
class Lubrification():
    epaisseur_film_huile_camepatin : np.ndarray = None
    epaisseur_film_huile_soupapepatin : np.ndarray = None
    estvalide : bool = False

    @classmethod
    def from_dict(cls, d):
        return Lubrification(
            epaisseur_film_huile_camepatin = np.array(d["epaisseur_film_huile_camepatin"]),
            epaisseur_film_huile_soupapepatin = np.array(d["epaisseur_film_huile_soupapepatin"]),
            estvalide = d["estvalide"]
        )
    
    def to_dict(self):
        return dataclasses.asdict(self)
    
@dataclasses.dataclass
class Mecanique():
    cinematique : Cinematique
    efforts : Efforts
    lubrification : Lubrification

    
    @classmethod
    def from_dict(cls, d):
        return Mecanique(
            cinematique=Cinematique.from_dict(d["cinematique"]),
            efforts=Efforts.from_dict(d["efforts"]),
            lubrification=Lubrification.from_dict(d["lubrification"])
        )
    
    def to_dict(self):
        return {
            "cinematique" : self.cinematique.to_dict(),
            "efforts" : self.efforts.to_dict(),
            "lubrification" : self.lubrification.to_dict()
        }
    

