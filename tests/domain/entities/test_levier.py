import pytest
import numpy as np
from softcam.domain.entities.levier import Levier, Patin

patin_came = Patin(27e-3,6e-3,210e9,0.3)
patin_soupape = Patin(18e-3,6e-3,210e9,0.3)

def test_levier_model_init():
    levier = Levier(
        masse = 70e-3,
        inertie = 9e-6,
        longueur = 36.8e-3,
        patin_came = patin_came,
        patin_soupape = patin_soupape
    )
    assert levier.masse == 70e-3
    assert levier.inertie == 9e-6
    assert levier.longueur == 36.8e-3
    assert levier.patin_came == patin_came
    assert levier.patin_soupape == patin_soupape

def test_levier_model_from_dict():
    init_dict = {
        "masse" : 70e-3,
        "inertie" : 9e-6,
        "longueur" : 36.8e-3,
        "patin_came" : patin_came,
        "patin_soupape" : patin_soupape,
    }
    levier = Levier.from_dict(init_dict)
    assert levier.masse == 70e-3
    assert levier.inertie == 9e-6
    assert levier.longueur == 36.8e-3
    assert levier.patin_came == patin_came
    assert levier.patin_soupape == patin_soupape

def test_levier_model_to_dict():
    init_dict = {
        "masse" : 70e-3,
        "inertie" : 9e-6,
        "longueur" : 36.8e-3,
        "patin_came" : patin_came,
        "patin_soupape" : patin_soupape,
    }
    levier = Levier.from_dict(init_dict)
    np.testing.assert_equal(levier.to_dict(),init_dict)

def test_levier_model_comparaison():
    init_dict = {
        "masse" : 70e-3,
        "inertie" : 9e-6,
        "longueur" : 36.8e-3,
        "patin_came" : patin_came,
        "patin_soupape" : patin_soupape,
    }
    levier1 = Levier.from_dict(init_dict)
    levier2 = Levier.from_dict(init_dict)
    assert levier1 == levier2

def test_levier_model_validate_masse():
    init_dict = {
        "masse" : -70e-3,
        "inertie" : 9e-6,
        "longueur" : 36.8e-3,
        "patin_came" : patin_came,
        "patin_soupape" : patin_soupape,
    }
    with pytest.raises(ValueError):
        Levier.from_dict(init_dict)

def test_levier_model_validate_inertie():
    init_dict = {
        "masse" : 70e-3,
        "inertie" : -9e-6,
        "longueur" : 36.8e-3,
        "patin_came" : patin_came,
        "patin_soupape" : patin_soupape,
    }
    with pytest.raises(ValueError):
        Levier.from_dict(init_dict)

def test_levier_model_validate_longueur():
    init_dict = {
        "masse" : 70e-3,
        "inertie" : 9e-6,
        "longueur" : -36.8e-3,
        "patin_came" : patin_came,
        "patin_soupape" : patin_soupape,
    }
    with pytest.raises(ValueError):
        Levier.from_dict(init_dict)

def test_levier_model_validate_patins():
    init_dict = {
        "masse" : 70e-3,
        "inertie" : 9e-6,
        "longueur" : 36.8e-3,
        "patin_came" : "patin_came",
        "patin_soupape" : patin_soupape,
    }
    with pytest.raises(ValueError):
        Levier.from_dict(init_dict)