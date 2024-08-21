import dataclasses

@dataclasses.dataclass
class Patin:
    rayon_courbure : float = 27e-3 #Rayon de courbure au niveau du contact (cas du poussoir courbe)
    largeur: float = 6e-3
    module_young : float = 210e9
    coefficient_poisson : float = 0.3
        
    def __post_init__(self):
        self.valide_largeur()
        self.valide_module_young()
        self.valide_coefficient_poisson()

    def valide_largeur(self):
        if self.largeur <= 0:
            raise ValueError("La largeur doit être positive.")

    def valide_module_young(self):
        if self.module_young <= 0:
            raise ValueError("Le module de Young doit être positif.")
    
    def valide_coefficient_poisson(self):
        if not -1 <= self.coefficient_poisson <= 0.5 :
            raise ValueError("Le coefficient de poisson doit être entre -1 et 0.5.")

    @classmethod
    def from_dict(cls, d):
        return cls(**d)
    
    def to_dict(self):
        return dataclasses.asdict(self)

@dataclasses.dataclass
class Levier:
    masse : float = 70e-3
    inertie : float = 9e-6
    longueur : float = 36.8e-3
    patin_came : Patin = dataclasses.field(default_factory=lambda:Patin())
    patin_soupape : Patin = dataclasses.field(default_factory=lambda:Patin())
        
    def __post_init__(self):
        self.valide_masse()
        self.valide_inertie()
        self.valide_longueur()
        self.valide_patins()

    def valide_masse(self):
        if self.masse < 0:
            raise ValueError("La masse doit être positive.")
    
    def valide_inertie(self):
        if self.inertie < 0:
            raise ValueError("L'inertie doit être positive.")
    
    def valide_longueur(self):
        if self.longueur <= 0:
            raise ValueError("La longueur doit être strictement positive.")
    
    def valide_patins(self):
        if not all((isinstance(self.patin_came, Patin), isinstance(self.patin_soupape, Patin))) :
            raise ValueError("Les patins doivent être de type Patin")

    @classmethod
    def from_dict(cls, d):
        return cls(
            masse = d["masse"],
            inertie = d["inertie"],
            longueur = d["longueur"],
            patin_came = Patin.from_dict(d["patin_came"]),
            patin_soupape = Patin.from_dict(d["patin_soupape"])
        )
    
    def to_dict(self):
        return {
            "masse" : self.masse,
            "inertie" : self.inertie,
            "longueur" : self.longueur,
            "patin_came" : self.patin_came.to_dict(),
            "patin_soupape" : self.patin_soupape.to_dict()
        }