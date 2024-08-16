import pytest
import numpy as np
from domain.services.unitees import DEGREE_TO_RADIAN
from softcam.domain.entities.came import Came


def test_came_model_init():
    rayon_base = 19e-3
    theta = np.arange(0,360) *DEGREE_TO_RADIAN
    a = -4/np.pi**2*rayon_base
    b = 4/np.pi*rayon_base
    rayon = np.array([a*x**2 + b*x + rayon_base if 0 < x < 180 else rayon_base for x in theta]) 
    came = Came(
        rayon_base=rayon_base,
        largeur=8e-3,
        module_young=210e9,
        coefficient_poisson=0.3,
        profil = np.array([theta, rayon])
    )
    assert came.rayon_base==19e-3
    assert came.largeur==8e-3
    assert came.module_young == 210e9
    assert came.coefficient_poisson == 0.3
    assert np.array_equal(came.profil, np.array([theta, rayon]))

def test_came_model_from_dict():
    rayon_base = 19e-3
    theta = np.arange(0,360) *DEGREE_TO_RADIAN
    a = -4/np.pi**2*rayon_base
    b = 4/np.pi*rayon_base
    rayon = np.array([a*x**2 + b*x + rayon_base if 0 < x < 180 else rayon_base for x in theta]) 
    init_dict = {
        "rayon_base":19e-3,
        "largeur":8e-3,
        "module_young":210e9,
        "coefficient_poisson":0.3,
        "profil":np.array([theta, rayon])
    }
    came = Came.from_dict(init_dict)
    assert came.rayon_base==19e-3
    assert came.largeur==8e-3
    assert came.module_young == 210e9
    assert came.coefficient_poisson == 0.3
    assert np.array_equal(came.profil, np.array([theta, rayon]))

def test_came_model_to_dict():
    rayon_base = 19e-3
    theta = np.arange(0,360) *DEGREE_TO_RADIAN
    a = -4/np.pi**2*rayon_base
    b = 4/np.pi*rayon_base
    rayon = np.array([a*x**2 + b*x + rayon_base if 0 < x < 180 else rayon_base for x in theta]) 
    init_dict = {
        "rayon_base":19e-3,
        "largeur":8e-3,
        "module_young":210e9,
        "coefficient_poisson":0.3,
        "profil":np.array([theta, rayon])
    }
    came = Came.from_dict(init_dict)
    np.testing.assert_equal(came.to_dict(), init_dict)

def test_came_model_comparaison():
    rayon_base = 19e-3
    theta = np.arange(0,360) *DEGREE_TO_RADIAN
    a = -4/np.pi**2*rayon_base
    b = 4/np.pi*rayon_base
    rayon = np.array([a*x**2 + b*x + rayon_base if 0 < x < 180 else rayon_base for x in theta]) 
    init_dict = {
        "rayon_base":19e-3,
        "largeur":8e-3,
        "module_young":210e9,
        "coefficient_poisson":0.3,
        "profil":np.array([theta, rayon])
    }
    came1 = Came.from_dict(init_dict)
    came2 = Came.from_dict(init_dict)
    assert came1 == came2

def test_came_model_validate_rayon_base():
    rayon_base = 19e-3
    theta = np.arange(0,360) *DEGREE_TO_RADIAN
    a = -4/np.pi**2*rayon_base
    b = 4/np.pi*rayon_base
    rayon = np.array([a*x**2 + b*x + rayon_base if 0 < x < 180 else rayon_base for x in theta]) 
    init_dict = {
        "rayon_base":-rayon_base,
        "largeur":8e-3,
        "module_young":210e9,
        "coefficient_poisson":0.3,
        "profil":np.array([theta, rayon])
    }
    with pytest.raises(ValueError):
        Came.from_dict(init_dict)

def test_came_model_validate_largeur():
    rayon_base = 19e-3
    theta = np.arange(0,360) *DEGREE_TO_RADIAN
    a = -4/np.pi**2*rayon_base
    b = 4/np.pi*rayon_base
    rayon = np.array([a*x**2 + b*x + rayon_base if 0 < x < 180 else rayon_base for x in theta]) 
    init_dict = {
        "rayon_base":rayon_base,
        "largeur":-8e-3,
        "module_young":210e9,
        "coefficient_poisson":0.3,
        "profil":np.array([theta, rayon])
    }
    with pytest.raises(ValueError):
        Came.from_dict(init_dict)

def test_came_model_validate_module_young():
    rayon_base = 19e-3
    theta = np.arange(0,360) *DEGREE_TO_RADIAN
    a = -4/np.pi**2*rayon_base
    b = 4/np.pi*rayon_base
    rayon = np.array([a*x**2 + b*x + rayon_base if 0 < x < 180 else rayon_base for x in theta]) 
    init_dict = {
        "rayon_base":rayon_base,
        "largeur":8e-3,
        "module_young":-210e9,
        "coefficient_poisson":0.3,
        "profil":np.array([theta, rayon])
    }
    with pytest.raises(ValueError):
        Came.from_dict(init_dict)

def test_came_model_validate_coefficient_poisson():
    rayon_base = 19e-3
    theta = np.arange(0,360) *DEGREE_TO_RADIAN
    a = -4/np.pi**2*rayon_base
    b = 4/np.pi*rayon_base
    rayon = np.array([a*x**2 + b*x + rayon_base if 0 < x < 180 else rayon_base for x in theta]) 
    init_dict = {
        "rayon_base":rayon_base,
        "largeur":8e-3,
        "module_young":210e9,
        "coefficient_poisson":2.3,
        "profil":np.array([theta, rayon])
    }
    with pytest.raises(ValueError):
        Came.from_dict(init_dict)

def test_came_model_validate_profil():
    rayon_base = 19e-3
    theta = np.arange(0,360) *DEGREE_TO_RADIAN
    a = -4/np.pi**2*rayon_base
    b = 4/np.pi*rayon_base
    rayon = np.array([a*x**2 + b*x + rayon_base if 0 < x < 180 else rayon_base for x in theta]) 
    init_dict = {
        "rayon_base":rayon_base,
        "largeur":8e-3,
        "module_young":210e9,
        "coefficient_poisson":0.3,
        "profil": rayon
    }
    with pytest.raises(ValueError):
        Came.from_dict(init_dict)