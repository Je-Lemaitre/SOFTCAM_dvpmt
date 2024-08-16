import pytest
from softcam.domain.entities.levier import Patin

def test_patin_model_init():
    patin = Patin(
        rayon_courbure = 27e-3, #Rayon de courbure au niveau du contact (cas du poussoir courbe)
        largeur = 6e-3,
        module_young=210e9,
        coefficient_poisson=0.3,
    )
    assert patin.rayon_courbure == 27e-3
    assert patin.largeur == 6e-3
    assert patin.module_young==210e9
    assert patin.coefficient_poisson==0.3

def test_patin_model_from_dict():
    init_dict = {
        "rayon_courbure":27e-3, 
        "largeur":6e-3,
        "module_young":210e9,
        "coefficient_poisson":0.3
    }
    patin = Patin.from_dict(init_dict)
    assert patin.rayon_courbure == 27e-3
    assert patin.largeur == 6e-3
    assert patin.module_young==210e9
    assert patin.coefficient_poisson==0.3
    
def test_patin_model_to_dict():
    init_dict = {
        "rayon_courbure":27e-3, 
        "largeur":6e-3,
        "module_young":210e9,
        "coefficient_poisson":0.3
    }
    patin = Patin.from_dict(init_dict)
    assert patin.to_dict() == init_dict

def test_patin_model_comparaison():
    init_dict = {
        "rayon_courbure":27e-3, 
        "largeur":6e-3,
        "module_young":210e9,
        "coefficient_poisson":0.3
    }
    patin1 = Patin.from_dict(init_dict)
    patin2 = Patin.from_dict(init_dict)
    assert patin1 == patin2

def test_patin_model_validate_largeur():
    init_dict = {
        "rayon_courbure":27e-3, 
        "largeur":-6e-3,
        "module_young":210e9,
        "coefficient_poisson":0.3
    }
    with pytest.raises(ValueError):
        Patin.from_dict(init_dict)

def test_patin_model_validate_module_young():
    init_dict = {
        "rayon_courbure":27e-3, 
        "largeur":6e-3,
        "module_young":-210e9,
        "coefficient_poisson":0.3
    }
    with pytest.raises(ValueError):
        Patin.from_dict(init_dict)

def test_patin_model_validate_coefficient_poisson():
    init_dict = {
        "rayon_courbure":27e-3, 
        "largeur":6e-3,
        "module_young":210e9,
        "coefficient_poisson":1.3
    }
    with pytest.raises(ValueError):
        Patin.from_dict(init_dict)