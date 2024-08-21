import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import dataclasses
import uuid

import domain.services.unitees as unit
from domain.entities.assemblage import Assemblage, AssemblageLinguet
from domain.entities.loiscame import LoisCame
from domain.entities.mecanique import Mecanique
from domain.entities.fabrication import Fabrication

@dataclasses.dataclass
class Etude():
    id : uuid.UUID = uuid.uuid4()
    nom : str = "Mon Étude"
    pas_angulaire : float = 1e-3
    pas_temporel : float = 1e-3
    type_assemblage : str = None
    assemblage : AssemblageLinguet = dataclasses.field(default_factory = lambda: AssemblageLinguet())
    loiscame : LoisCame = dataclasses.field(default_factory = lambda: LoisCame())
    mecanique : Mecanique = None
    fabrication : Fabrication = None

    def __post_init__(self):
        pass

    def valide_pas_angulaire(self):
        if not 0 < self.pas_angulaire < 360 *unit.DEGREE_TO_RADIAN :
            raise ValueError("Le pas angulaire doit être strictement positif et inférieur à 360 degrés.")
        if 360 % ( self.pas_angulaire / unit.DEGREE_TO_RADIAN ) != 0 : # Le signe % permet de calculer le reste de la division Euclidienne.
            raise ValueError("Le pas angulaire doit être multiple de 360 degrées.")

    def valide_assemblage(self):
        if not (isinstance(self.assemblage, list) and isinstance(self.assemblage[0], Assemblage)):
            raise ValueError("L'objet entré comme assemblage doit être une liste composée d'éléments de type Assemblage.")
    
    @classmethod
    def from_dict(cls, d):
        try :
            id_import = uuid.UUID(d["id"])
        except TypeError :
            id_import = uuid.uuid4()
        return cls(
            id = id_import,
            nom = d["nom"],
            pas_angulaire = d["pas_angulaire"],
            pas_temporel = d["pas_temporel"],
            type_assemblage = d["type_assemblage"],
            assemblage = Assemblage.from_dict(d["assemblage"]),
            loiscame = LoisCame.from_dict(d["loiscame"]),
            mecanique = Mecanique.from_dict(d["mecanique"]),
            fabrication = Fabrication.from_dict(d["fabrication"])
        )
    
    def to_dict(self):
        return {
            "id" : self.id.urn,
            "nom" : self.nom,
            "pas_angulaire" : self.pas_angulaire,
            "pas_temporel" : self.pas_temporel,
            "type_assemblage" : self.type_assemblage,
            "assemblage" : self.assemblage.to_dict(),
            "loiscame" : self.loiscame.to_dict(),
            "mecanique" : self.mecanique.to_dict(),
            "fabrication" : self.fabrication.to_dict()
        }