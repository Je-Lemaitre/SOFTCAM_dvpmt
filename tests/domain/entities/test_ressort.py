import pytest
from softcam.domain.entities.ressort import Ressort

def test_ressort_model_init():
    ressort = Ressort(
        masse=27e-3,
        raideur=46.5e3,
        precharge=240
    )
    assert ressort.masse==27e-3
    assert ressort.raideur==46.5e3
    assert ressort.precharge==240

def test_ressort_model_from_dict():
    init_dict = {
        "masse" : 27e-3,
        "raideur" : 46.5e3,
        "precharge" : 240
    }
    ressort = Ressort.from_dict(init_dict)
    assert ressort.masse==27e-3
    assert ressort.raideur==46.5e3
    assert ressort.precharge==240

def test_ressort_model_to_dict():
    init_dict = {
        "masse" : 27e-3,
        "raideur" : 46.5e3,
        "precharge" : 240
    }
    ressort = Ressort.from_dict(init_dict)
    assert ressort.to_dict() == init_dict

def test_ressort_model_comparaison():
    init_dict = {
        "masse" : 27e-3,
        "raideur" : 46.5e3,
        "precharge" : 240
    }
    ressort1 = Ressort.from_dict(init_dict)
    ressort2 = Ressort.from_dict(init_dict)
    assert ressort1 == ressort2

def test_ressort_model_add():
    ressort1 = Ressort(
        masse = 0.027,
        raideur=46.5e3,
        precharge =240
    )
    ressort2 = Ressort(
        masse = 0.023,
        raideur=53.5e3,
        precharge =240
    )
    ressort_result = Ressort(
        masse = 0.05,
        raideur=1e5,
        precharge =480
    )
    assert ressort1 + ressort2 == ressort_result

def test_ressort_model_validate_masse():
    init_dict = {
        "masse" : -27e-3,
        "raideur" : 46.5e3,
        "precharge" : 240
    }
    with pytest.raises(ValueError):
        Ressort.from_dict(init_dict)

def test_ressort_model_validate_raideur():
    init_dict = {
        "masse" : 27e-3,
        "raideur" : -46.5e3,
        "precharge" : 240
    }
    with pytest.raises(ValueError):
        Ressort.from_dict(init_dict)