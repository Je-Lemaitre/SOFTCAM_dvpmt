import pytest

from domain.services.unitees import TRPMIN_TO_RADPSEC

from domain.entities.assemblage import Assemblage
from softcam.domain.entities.soupape import Soupape
from softcam.domain.entities.levier import Levier
from softcam.application.usecases.assemblage import AssemblageLinguetUseCases


import numpy as np

class Test_AssemblageLinguetUseCases:
    
    def test_levee_from_inclinaison(self):
        inclinaison_initiale = -0.35
        longueur_linguet = 36.8e-3
        inclinaison_soupape = 0.1
        assemblage = Assemblage(
            soupape=Soupape(inclinaison_axe=inclinaison_soupape),
            levier=Levier(inclinaison_position_fermee=inclinaison_initiale, longueur=longueur_linguet)
            )
        inclinaison_linguet = np.array([-0.35, 0, 1])
        test_levee = longueur_linguet*(np.sin(inclinaison_linguet-inclinaison_soupape) - np.sin(inclinaison_initiale-inclinaison_soupape))
        assemblage_usecase = AssemblageLinguetUseCases(assemblage)

        assert np.array_equal(assemblage_usecase.levee_from_inclinaison(inclinaison_linguet), test_levee)
    
    def test_inclinaison_from_levee(self):
        inclinaison_initiale = -0.35
        longueur_linguet = 36.8e-3
        inclinaison_soupape = 0.1
        assemblage = Assemblage(
            soupape=Soupape(inclinaison_axe=inclinaison_soupape),
            levier=Levier(inclinaison_position_fermee=inclinaison_initiale, longueur=longueur_linguet)
            )
        levee = np.array([0, -2e-3, -6e-3])
        test_inclinaison = np.arcsin(levee/(longueur_linguet + np.sin(inclinaison_initiale-inclinaison_soupape))) + inclinaison_soupape
        assemblage_usecase = AssemblageLinguetUseCases(assemblage)

        assert np.array_equal(assemblage_usecase.inclinaison_from_levee(levee), test_inclinaison)
    
    def test_vitesse_balayage(self):
        derivee_inclinaison_linguet = 0.1
        derivee_rotation_came = 0.3
        regime_moteur = 9000 *TRPMIN_TO_RADPSEC
        rayon_came = 19.654e-3

        coords_contact = (10e-3,12.5e-3)
        coords_linguet = (35.7e-3,5.4e-3)
        coords_came =(14.2e-3,31.7e-3)

        vitesse_balayage_new = np.sqrt(
        (derivee_rotation_came*regime_moteur*rayon_came)**2 
        + (derivee_inclinaison_linguet*regime_moteur)**2*(
            (coords_contact[0] - coords_linguet[0])**2 + (coords_contact[1] - coords_linguet[1])**2
            )
        - 2*derivee_rotation_came*derivee_inclinaison_linguet*regime_moteur**2*(
            (coords_contact[0] - coords_linguet[0])*(coords_contact[0] - coords_came[0]) +
            (coords_contact[1] - coords_linguet[1])*(coords_contact[1] - coords_came[1])
        )
        )
        vitesse_balayage_prev = derivee_inclinaison_linguet*regime_moteur*np.sqrt(
            (coords_contact[0] - coords_linguet[0])**2 + (coords_contact[1] - coords_linguet[1])**2
        )
        + (
            rayon_came*regime_moteur
        )

        assemblage_usecase = AssemblageLinguetUseCases(Assemblage())
    
        assert assemblage_usecase.vitesse_balayage(regime_moteur, coords_contact)

