import dataclasses
import numpy as np

@dataclasses.dataclass
class Poussoir():
    masse : float = 5e-3
    diametre : float = 25e-3
    rayon_courbure : float = 30e-3
    largeur_courbure: float = 6e-3
    frottement_poussoir_guide : float = 0
        
    def __post_init__(self):
        self.valide_masse()
        self.valide_diametre()
        self.valide_largeur_courbure() 

    def valide_masse(self):
        if self.masse<0:
            raise ValueError("Les masses doivent être positives.")
        
    def valide_diametre(self):
        if self.diametre <= 0:
            raise ValueError("Le diamètre doit être positif.")

    def valide_largeur_courbure(self):
        if self.largeur_courbure <= 0:
            raise ValueError("La largeur doit être positive.")
    
    @classmethod
    def from_dict(cls, d):
        return cls(**d)
    
    def to_dict(self):
        return dataclasses.asdict(self)

@dataclasses.dataclass
class Soupape():
    masse_soupape : float = 43.5e-3
    masse_coupelle : float = 5.5e-3 #Lunules et Grain compris
    diametre_soupape : float = 6e-3
    poussoir : Poussoir = None
    module_young : float = 210e9
    coefficient_poisson : float = 0.3
    
    def __post_init__(self):
        self.valide_masses()
        self.valide_diametre_soupape()
        self.valide_module_young()
        self.valide_coefficient_poisson()
        
    def valide_masses(self):
        if any((self.masse_soupape<0, self.masse_coupelle<0)):
            raise ValueError("Les masses doivent être positives.")
        
    def valide_diametre_soupape(self):
        if self.diametre_soupape <= 0:
            raise ValueError("Le diamètre doit être positif.")

    def valide_module_young(self):
        if self.module_young <= 0:
            raise ValueError("Le module de Young doit être positif.")

    def valide_coefficient_poisson(self):
        if not -1 <= self.coefficient_poisson <= 0.5 :
            raise ValueError("Le coefficient de poisson doit être entre -1 et 0.5.")

    @classmethod
    def from_dict(cls, d):
        if d["poussoir"] == None :
            return cls(
                masse_soupape = d["masse_soupape"],
                masse_coupelle = d["masse_coupelle"],
                diametre_soupape = d["diametre_soupape"],
                poussoir = None,
                module_young = d["module_young"],
                coefficient_poisson = d["coefficient_poisson"]
            )

        else :
            return cls(
                masse_soupape = d["masse_soupape"],
                masse_coupelle = d["masse_coupelle"],
                diametre_soupape = d["diametre_soupape"],
                poussoir = Poussoir.from_dict(d["poussoir"]),
                module_young = d["module_young"],
                coefficient_poisson = d["coefficient_poisson"]
            )

    def to_dict(self):
        if self.poussoir is None :
            dict_poussoir = None
        else :
            dict_poussoir = self.poussoir.__dict__

        return {
            "masse_soupape" : self.masse_soupape,
            "masse_coupelle" : self.masse_coupelle,
            "diametre_soupape" : self.diametre_soupape,
            "poussoir" : dict_poussoir,
            "module_young" : self.module_young,
            "coefficient_poisson" : self.coefficient_poisson 
        }
    
        
    
    
    
    

    