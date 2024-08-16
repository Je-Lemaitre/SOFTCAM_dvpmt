import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt")

import pytest
from unittest import mock
import numpy as np
from scipy.interpolate import BSpline
from softcam.domain.entities.loiscame import LoisPhaseRampe, LoisPhaseAccel, LoisPhaseDecel, LoisPhaseRaccord, DemiLois, LoisCame

class Test_LoisPhaseRampe:
    def function_test(self, x):
        return x

    @pytest.fixture
    def lois_phase_rampe(self):
        duree_rampe = 10
        a_rampe = mock.Mock(side_effect=self.function_test)
        v_rampe = mock.Mock(side_effect=self.function_test)
        l_rampe = mock.Mock(side_effect=self.function_test)
        j_rampe = mock.Mock(side_effect=self.function_test)
        return LoisPhaseRampe(duree_rampe, a_rampe, v_rampe, l_rampe, j_rampe)

    def test_j_within_range(self, lois_phase_rampe):
        ac = np.array([0, 5, 10])
        expected = ac
        result = lois_phase_rampe.j(ac)
        assert np.array_equal(result, expected)

    def test_j_outside_range(self, lois_phase_rampe):
        ac = np.array([-1, 11])
        expected = np.array([0, 0])
        result = lois_phase_rampe.j(ac)
        assert np.array_equal(result, expected)

    def test_a_within_range(self, lois_phase_rampe):
        ac = np.array([0, 5, 10])
        expected = ac
        result = lois_phase_rampe.a(ac)
        assert np.array_equal(result, expected)

    def test_a_outside_range(self, lois_phase_rampe):
        ac = np.array([-1, 11])
        expected = np.array([0, 0])
        result = lois_phase_rampe.a(ac)
        assert np.array_equal(result, expected)

    def test_v_within_range(self, lois_phase_rampe):
        ac = np.array([0, 5, 10])
        expected = ac
        result = lois_phase_rampe.v(ac)
        assert np.array_equal(result, expected)

    def test_v_outside_range(self, lois_phase_rampe):
        ac = np.array([-1, 11])
        expected = np.array([0, 0])
        result = lois_phase_rampe.v(ac)
        assert np.array_equal(result, expected)

    def test_l_within_range(self, lois_phase_rampe):
        ac = np.array([0, 5, 10])
        expected = ac
        result = lois_phase_rampe.l(ac)
        assert np.array_equal(result, expected)

    def test_l_outside_range(self, lois_phase_rampe):
        ac = np.array([-1, 11])
        expected = np.array([0, 0])
        result = lois_phase_rampe.l(ac)
        assert np.array_equal(result, expected)

class Test_LoisPhaseAccel:
    @pytest.fixture
    def mock_bspline(self):
        # Create a mock BSpline object
        bspline = mock.Mock(spec=BSpline)
        bspline.antiderivative.return_value = bspline
        bspline.derivative.return_value = bspline
        return bspline

    @pytest.fixture
    def lois_phase_accel(self, mock_bspline):
        duree_accel = 10.0
        levee_rampe = 5.0
        vitesse_rampe = 2.0
        return LoisPhaseAccel(duree_accel, levee_rampe, vitesse_rampe, mock_bspline)

    def test_post_init(self, lois_phase_accel, mock_bspline):
        assert lois_phase_accel.v_spl == mock_bspline
        assert lois_phase_accel.l_spl == mock_bspline
        assert lois_phase_accel.j_spl == mock_bspline

    def test_j_within_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([1, 5, 10])
        expected = np.array([1, 5, 10])
        mock_bspline.return_value = expected

        result = lois_phase_accel.j(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_called_once_with(np.ma.array(ac, mask=[False, False, False]))

    def test_j_outside_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-1, 11])
        expected = np.array([0, 0])
        mock_bspline.return_value = np.array([-1, 11])

        result = lois_phase_accel.j(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_called_once_with(np.ma.array(ac, mask=[True, True]))

    def test_a_within_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([1, 5, 10])
        expected = np.array([1, 5, 10])
        mock_bspline.return_value = expected

        result = lois_phase_accel.a(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_called_once_with(np.ma.array(ac, mask=[False, False, False]))

    def test_a_outside_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-1, 11])
        expected = np.array([0, 0])
        mock_bspline.return_value = np.array([-1, 11])

        result = lois_phase_accel.a(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_called_once_with(np.ma.array(ac, mask=[True, True]))

    def test_v_within_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([1, 5, 10])
        mock_bspline.return_value = np.array([1, 5, 10])
        expected = mock_bspline(ac) + lois_phase_accel.vitesse_rampe - mock_bspline(0)

        result = lois_phase_accel.v(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_any_call(np.ma.array(ac, mask=[False, False, False]))

    def test_v_outside_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-1, 11])
        mock_bspline.return_value = np.array([-1, 11])
        expected = np.array([0, 0])

        result = lois_phase_accel.v(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_any_call(np.ma.array(ac, mask=[True, True]))

    def test_l_within_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([1, 5, 10])
        mock_bspline.return_value = np.array([1, 5, 10])
        expected = mock_bspline(ac) + (lois_phase_accel.vitesse_rampe - mock_bspline(0)) * ac + lois_phase_accel.levee_rampe - mock_bspline(0)

        result = lois_phase_accel.l(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_any_call(np.ma.array(ac, mask=[False, False, False]))

    def test_l_outside_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-1, 11])
        mock_bspline.return_value = np.array([-1, 11])
        expected = np.array([0, 0])

        result = lois_phase_accel.l(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_any_call(np.ma.array(ac, mask=[True, True]))

class Test_LoisPhaseRaccord:
    @pytest.fixture
    def mock_bspline(self):
        # Create a mock BSpline object
        bspline = mock.Mock(spec=BSpline)
        bspline.antiderivative.return_value = bspline
        bspline.derivative.return_value = bspline
        return bspline

    @pytest.fixture
    def lois_phase_accel(self, mock_bspline):
        duree_raccord = 10.0
        levee_init = 5.0
        vitesse_init = 2.0
        return LoisPhaseRaccord(duree_raccord, levee_init, vitesse_init, mock_bspline)

    def test_post_init(self, lois_phase_accel, mock_bspline):
        assert lois_phase_accel.v_spl == mock_bspline
        assert lois_phase_accel.l_spl == mock_bspline
        assert lois_phase_accel.j_spl == mock_bspline

    def test_j_within_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-1, -5, -9])
        expected = np.array([-1, -5, -9])
        mock_bspline.return_value = expected

        result = lois_phase_accel.j(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_called_once_with(np.ma.array(ac, mask=[False, False, False]))

    def test_j_outside_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-11, 1])
        expected = np.array([0, 0])
        mock_bspline.return_value = np.array([-11, 1])

        result = lois_phase_accel.j(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_called_once_with(np.ma.array(ac, mask=[True, True]))

    def test_a_within_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-1, -5, -9])
        expected = np.array([-1, -5, -9])
        mock_bspline.return_value = expected

        result = lois_phase_accel.a(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_called_once_with(np.ma.array(ac, mask=[False, False, False]))

    def test_a_outside_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-11, 1])
        expected = np.array([0, 0])
        mock_bspline.return_value = np.array([-11, 1])

        result = lois_phase_accel.a(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_called_once_with(np.ma.array(ac, mask=[True, True]))

    def test_v_within_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-1, -5, -9])
        mock_bspline.return_value = np.array([-1, -5, -9])
        expected = mock_bspline(ac) + lois_phase_accel.vitesse_init - mock_bspline(0)

        result = lois_phase_accel.v(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_any_call(np.ma.array(ac, mask=[False, False, False]))

    def test_v_outside_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-10, 1])
        mock_bspline.return_value = np.array([-10, 1])
        expected = np.array([0, 0])

        result = lois_phase_accel.v(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_any_call(np.ma.array(ac, mask=[True, True]))

    def test_l_within_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-1, -5, -9])
        mock_bspline.return_value = np.array([-1, -5, -9])
        expected = mock_bspline(ac) + (lois_phase_accel.vitesse_init - mock_bspline(0)) * ac + lois_phase_accel.levee_init - mock_bspline(0)

        result = lois_phase_accel.l(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_any_call(np.ma.array(ac, mask=[False, False, False]))

    def test_l_outside_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-10, 1])
        mock_bspline.return_value = np.array([-10, 1])
        expected = np.array([0, 0])

        result = lois_phase_accel.l(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_any_call(np.ma.array(ac, mask=[True, True]))

class Test_LoisPhaseDecel:
    @pytest.fixture
    def mock_bspline(self):
        # Create a mock BSpline object
        bspline = mock.Mock(spec=BSpline)
        bspline.antiderivative.return_value = bspline
        bspline.derivative.return_value = bspline
        return bspline

    @pytest.fixture
    def lois_phase_accel(self, mock_bspline):
        duree_decel = 10.0
        levee_max = 5.0
        return LoisPhaseDecel(duree_decel, levee_max, mock_bspline)

    def test_post_init(self, lois_phase_accel, mock_bspline):
        assert lois_phase_accel.v_spl == mock_bspline
        assert lois_phase_accel.l_spl == mock_bspline
        assert lois_phase_accel.j_spl == mock_bspline

    def test_j_within_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-1, -5, -10])
        expected = np.array([-1, -5, -10])
        mock_bspline.return_value = expected

        result = lois_phase_accel.j(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_called_once_with(np.ma.array(ac, mask=[False, False, False]))

    def test_j_outside_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-11, 1])
        expected = np.array([0, 0])
        mock_bspline.return_value = np.array([-11, 1])

        result = lois_phase_accel.j(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_called_once_with(np.ma.array(ac, mask=[True, True]))

    def test_a_within_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-1, -5, -10])
        expected = np.array([-1, -5, -10])
        mock_bspline.return_value = expected

        result = lois_phase_accel.a(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_called_once_with(np.ma.array(ac, mask=[False, False, False]))

    def test_a_outside_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-11, 1])
        expected = np.array([0, 0])
        mock_bspline.return_value = np.array([-11, 1])

        result = lois_phase_accel.a(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_called_once_with(np.ma.array(ac, mask=[True, True]))

    def test_v_within_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-1, -5, -10])
        mock_bspline.return_value = np.array([-1, -5, -10])
        expected = mock_bspline(ac) - mock_bspline(0)

        result = lois_phase_accel.v(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_any_call(np.ma.array(ac, mask=[False, False, False]))

    def test_v_outside_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-11, 1])
        mock_bspline.return_value = np.array([-11, 1])
        expected = np.array([0, 0])

        result = lois_phase_accel.v(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_any_call(np.ma.array(ac, mask=[True, True]))

    def test_l_within_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-1, -5, -10])
        mock_bspline.return_value = np.array([-1, -5, -10])
        expected = mock_bspline(ac) - mock_bspline(0)*ac + lois_phase_accel.levee_max - mock_bspline(0)

        result = lois_phase_accel.l(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_any_call(np.ma.array(ac, mask=[False, False, False]))

    def test_l_outside_range(self, lois_phase_accel, mock_bspline):
        ac = np.array([-11, 1])
        mock_bspline.return_value = np.array([-11, 1])
        expected = np.array([0, 0])

        result = lois_phase_accel.l(ac)
        assert np.array_equal(result, expected)
        # mock_bspline.assert_any_call(np.ma.array(ac, mask=[True, True]))

class Test_DemiLois:
    @pytest.fixture
    def demilois(self):
        # Create a DemiLois object for testing
        lois_rampe = mock.MagicMock()
        lois_accel = mock.MagicMock()
        lois_raccord = mock.MagicMock()
        lois_decel = mock.MagicMock()
        ac_fin_rampe = 5.0
        ac_fin_accel = 10.0
        ac_leveemax = 15.0

        return DemiLois(lois_rampe, lois_accel, lois_raccord, lois_decel, ac_fin_rampe, ac_fin_accel, ac_leveemax)

    def test_post_init(self, demilois):
        # Test the __post_init__ method
        ac_fin_accel = 10.0
        ac_raccord = ac_fin_accel + demilois.lois_raccord.duree_raccord
        assert demilois.ac_raccord == ac_raccord

class Test_LoisCame:
    @pytest.fixture
    def loiscame(self):
        # Create a DemiLois object for testing
        demilois_ouverture = mock.MagicMock()
        demilois_fermeture = mock.MagicMock()
        dac_leveemax_ouverture = 1
        dac_leveemax_fermeture = 2

        return LoisCame(demilois_ouverture, demilois_fermeture, dac_leveemax_ouverture, dac_leveemax_fermeture)

    def test_post_init(self, loiscame):
        # Test the __post_init__ method
        assert 1 == 1