import pytest
import uuid
from domain.services.unitees import DEGREE_TO_RADIAN, TRPMIN_TO_RADPSEC, MEGAPASCAL_TO_PASCAL
from softcam.domain.entities.etude import Etude
from domain.entities.assemblage import AssemblageLinguet
from softcam.domain.entities.loiscame import LoisCame

def test_etude_model_init():
    id = uuid.uuid4()
    nom = "Étude test"
    distribution = AssemblageLinguet()
    loicame = LoisCame()
    etude = Etude(
        id = id,
        nom = nom,
        pas_angulaire = 1 *DEGREE_TO_RADIAN,
        regime_affolement = 9500 *TRPMIN_TO_RADPSEC,
        regime_utilisation = 7500 *TRPMIN_TO_RADPSEC,
        distribution = [distribution],
        loicame = loicame
    )
    assert etude.id == id
    assert etude.nom == nom
    assert etude.pas_angulaire == 1 *DEGREE_TO_RADIAN 
    assert etude.regime_affolement == 9500 *TRPMIN_TO_RADPSEC
    assert etude.regime_utilisation == 7500 *TRPMIN_TO_RADPSEC
    assert etude.distribution == [distribution]
    assert etude.loicame == loicame

def test_etude_model_from_dict():
    id = uuid.uuid4()
    nom = "Étude test"
    distribution = AssemblageLinguet()
    loicame = LoisCame()
    init_dict = {
        "id" : id,
        "nom" : nom,
        "pas_angulaire" : 1 *DEGREE_TO_RADIAN,
        "regime_affolement" : 9500 *TRPMIN_TO_RADPSEC,
        "regime_utilisation" : 7500 *TRPMIN_TO_RADPSEC,
        "distribution" : [distribution],
        "loicame" : loicame
    }
    etude = Etude.from_dict(init_dict)
    assert etude.id == id
    assert etude.nom == nom
    assert etude.pas_angulaire == 1 *DEGREE_TO_RADIAN 
    assert etude.regime_affolement == 9500 *TRPMIN_TO_RADPSEC
    assert etude.regime_utilisation == 7500 *TRPMIN_TO_RADPSEC
    assert etude.distribution == [distribution]
    assert etude.loicame == loicame

def test_etude_model_to_dict():
    id = uuid.uuid4()
    nom = "Étude test"
    distribution = AssemblageLinguet()
    loicame = LoisCame()
    init_dict = {
        "id" : id,
        "nom" : nom,
        "pas_angulaire" : 1 *DEGREE_TO_RADIAN,
        "regime_affolement" : 9500 *TRPMIN_TO_RADPSEC,
        "regime_utilisation" : 7500 *TRPMIN_TO_RADPSEC,
        "distribution" : [distribution],
        "loicame" : loicame
    }
    etude = Etude.from_dict(init_dict)
    etude.to_dict() == init_dict

def test_etude_model_comparaison():
    id = uuid.uuid4()
    nom = "Étude test"
    distribution = AssemblageLinguet()
    loicame = LoisCame()
    init_dict = {
        "id" : id,
        "nom" : nom,
        "pas_angulaire" : 1 *DEGREE_TO_RADIAN,
        "regime_affolement" : 9500 *TRPMIN_TO_RADPSEC,
        "regime_utilisation" : 7500 *TRPMIN_TO_RADPSEC,
        "distribution" : [distribution],
        "loicame" : loicame
    }
    etude1 = Etude.from_dict(init_dict)
    etude2 = Etude.from_dict(init_dict)
    assert etude1 == etude2

def test_etude_model_validate_pas_angulaire():
    id = uuid.uuid4()
    nom = "Étude test"
    distribution = AssemblageLinguet()
    loicame = LoisCame()
    init_dict = {
        "id" : id,
        "nom" : nom,
        "pas_angulaire" : 360 *DEGREE_TO_RADIAN,
        "regime_affolement" : 9500 *TRPMIN_TO_RADPSEC,
        "regime_utilisation" : 7500 *TRPMIN_TO_RADPSEC,
        "distribution" : [distribution],
        "loicame" : loicame
    }
    with pytest.raises(ValueError):
        Etude.from_dict(init_dict)

def test_etude_model_validate_regimes():
    id = uuid.uuid4()
    nom = "Étude test"
    distribution = AssemblageLinguet()
    loicame = LoisCame()
    init_dict = {
        "id" : id,
        "nom" : nom,
        "pas_angulaire" : 1 *DEGREE_TO_RADIAN,
        "regime_affolement" : 7500 *TRPMIN_TO_RADPSEC,
        "regime_utilisation" : 9500 *TRPMIN_TO_RADPSEC,
        "distribution" : [distribution],
        "loicame" : loicame
    }
    with pytest.raises(ValueError):
        Etude.from_dict(init_dict)

def test_etude_model_validate_distribution():
    id = uuid.uuid4()
    nom = "Étude test"
    distribution = AssemblageLinguet()
    loicame = LoisCame()
    init_dict = {
        "id" : id,
        "nom" : nom,
        "pas_angulaire" : 1 *DEGREE_TO_RADIAN,
        "regime_affolement" : 9500 *TRPMIN_TO_RADPSEC,
        "regime_utilisation" : 7500 *TRPMIN_TO_RADPSEC,
        "distribution" : ["À Linguet"],
        "loicame" : loicame
    }
    with pytest.raises(ValueError):
        Etude.from_dict(init_dict)