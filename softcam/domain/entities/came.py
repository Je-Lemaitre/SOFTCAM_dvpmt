import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import dataclasses

import scipy.interpolate as scitp

@dataclasses.dataclass
class Came:
    rayon_base : float = 19e-3
    largeur : float = 8e-3
    module_young : float = 210e9
    coefficient_poisson : float = 0.3
    inertie : float = 1e-6
    profil : scitp.BSpline = None

    def __post_init__(self):
        self.valide_rayon_base()
        self.valide_largeur()
        self.valide_module_young()
        self.valide_coefficient_poisson()

    def valide_rayon_base(self):
        if self.rayon_base <= 0:
            raise ValueError("Le rayon de base doit être positif.")
    
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
        profil_import = None if d["profil"] is None else scitp.BSpline(d["profil"])
        return cls(
            rayon_base = d["rayon_base"],
            largeur = d["largeur"],
            inertie = d["inertie"],
            module_young = d["module_young"],
            coefficient_poisson = d["coefficient_poisson"],
            profil = profil_import
        )
    
    def to_dict(self):
        profil_export = None if self.profil is None else self.profil.__dict__
        return {
            "rayon_base" : self.rayon_base,
            "largeur" : self.largeur,
            "inertie" : self.inertie,
            "module_young" : self.module_young,
            "coefficient_poisson" : self.coefficient_poisson,
            "profil" : profil_export
        }
    