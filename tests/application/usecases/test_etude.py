import pytest
import numpy as np
from softcam.application.usecases.loiscame import CalculLoiCameUseCase
from softcam.domain.entities.etude import Etude

def test_phase_accel_rampe_ouverture():
    etude = Etude()
    calcul_loi_came = CalculLoiCameUseCase(etude)
    calcul_loi_came.phase_accel_rampe_ouverture()
    
    pass

def test_phase_nulle_rampe_ouverture():
    etude = Etude()
    calcul_loi_came = CalculLoiCameUseCase(etude)
    calcul_loi_came.phase_accel_rampe_ouverture()
    calcul_loi_came.phase_nulle_rampe_ouverture()

def test_phase_montee_accel_ouverture():
    etude = Etude()
    calcul_loi_came = CalculLoiCameUseCase(etude)
    calcul_loi_came.phase_accel_rampe_ouverture()
    calcul_loi_came.phase_nulle_rampe_ouverture()
    calcul_loi_came.phase_montee_accel_ouverture()

def test_phase_palier_accel_ouverture():
    etude = Etude()
    calcul_loi_came = CalculLoiCameUseCase(etude)
    calcul_loi_came.phase_accel_rampe_ouverture()
    calcul_loi_came.phase_nulle_rampe_ouverture()
    calcul_loi_came.phase_montee_accel_ouverture()
    calcul_loi_came.phase_palier_accel_ouverture()

def test_phase_descente_accel_ouverture():
    etude = Etude()
    calcul_loi_came = CalculLoiCameUseCase(etude)
    calcul_loi_came.phase_accel_rampe_ouverture()
    calcul_loi_came.phase_nulle_rampe_ouverture()
    calcul_loi_came.phase_montee_accel_ouverture()
    calcul_loi_came.phase_palier_accel_ouverture()
    angles_phase = calcul_loi_came.phase_descente_accel_ouverture()
    calcul_loi_came.plot()



#def test_integration():
#    etude = Etude()
#    calcul_loi_came = CalculLoiCameUseCase(etude)
#    calcul_loi_came.calcul_loicame()
#    pass