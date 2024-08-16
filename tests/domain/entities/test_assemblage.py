import pytest
import numpy as np

from domain.services.unitees import DEGREE_TO_RADIAN, TRPMIN_TO_RADPSEC, MEGAPASCAL_TO_PASCAL
from domain.entities.assemblage import AssemblageLinguet, AssemblageDirecte
from softcam.domain.entities.came import Came
from softcam.domain.entities.levier import Levier
from softcam.domain.entities.ressort import Ressort
from softcam.domain.entities.soupape import Soupape

class Test_AssemblageLinguet:
    def test_distribution_model_init(self):
        came = Came()
        levier = Levier()
        ressort = Ressort()
        soupape = SoupapeSansPoussoir()
        distribution = AssemblageLinguet(
            angle_came = 0,
            came = came,
            coords_came = np.array([14.2e-3, 31.7e-3]),
            sens_rotation_came = 1,
            ressort = ressort,
            soupape = soupape,
            coords_soupape = np.array([0, 0]),
            inclinaison_soupape = 0,
            levier = levier,
            coords_levier = np.array([35.6e-3, 5.4e-3]),
            angle_leviercame_init = 5.3 *DEGREE_TO_RADIAN,
            angles_limites_patinsoupape = (25,35),
            angles_limites_patincame =(20,25)
        )
        assert distribution.angle_came == 0
        assert distribution.came == came
        assert np.array_equal(distribution.coords_came, np.array([14.2e-3, 31.7e-3]))
        assert distribution.sens_rotation_came == 1
        assert distribution.ressort == ressort
        assert distribution.soupape == soupape
        assert np.array_equal(distribution.coords_soupape, np.array([0, 0]))
        assert distribution.inclinaison_soupape == 0
        assert distribution.levier == levier
        assert np.array_equal(distribution.coords_levier, np.array([35.6e-3, 5.4e-3]))
        assert distribution.angle_leviercame_init == 5.3 *DEGREE_TO_RADIAN
        assert distribution.angles_limites_patinsoupape == (25,35)
        assert distribution.angles_limites_patincame ==(20,25)

    def test_distribution_model_from_dict(self):
        came = Came()
        levier = Levier()
        ressort = Ressort()
        soupape = SoupapeSansPoussoir()
        init_dict = {
            "angle_came" : 0,
            "came" : came,
            "coords_came" : np.array([14.2e-3, 31.7e-3]),
            "sens_rotation_came" : 1,
            "ressort" : ressort,
            "soupape" : soupape,
            "coords_soupape" : np.array([0, 0]),
            "inclinaison_soupape" : 0,
            "levier" : levier,
            "coords_levier" : np.array([35.6e-3, 5.4e-3]),
            "angle_leviercame_init" : 5.3 *DEGREE_TO_RADIAN,
            "angles_limites_patinsoupape" : (25,35),
            "angles_limites_patincame" :(20,25)
        }
        distribution = AssemblageLinguet.from_dict(init_dict)
        assert distribution.angle_came == 0
        assert distribution.came == came
        assert np.array_equal(distribution.coords_came, np.array([14.2e-3, 31.7e-3]))
        assert distribution.sens_rotation_came == 1
        assert distribution.ressort == ressort
        assert distribution.soupape == soupape
        assert np.array_equal(distribution.coords_soupape, np.array([0, 0]))
        assert distribution.inclinaison_soupape == 0
        assert distribution.levier == levier
        assert np.array_equal(distribution.coords_levier, np.array([35.6e-3, 5.4e-3]))
        assert distribution.angle_leviercame_init == 5.3 *DEGREE_TO_RADIAN
        assert distribution.angles_limites_patinsoupape == (25,35)
        assert distribution.angles_limites_patincame ==(20,25)

    def test_distribution_model_to_dict(self):
        came = Came()
        levier = Levier()
        ressort = Ressort()
        soupape = SoupapeSansPoussoir()
        init_dict = {
            "angle_came" : 0,
            "came" : came,
            "coords_came" : np.array([14.2e-3, 31.7e-3]),
            "sens_rotation_came" : 1,
            "ressort" : ressort,
            "soupape" : soupape,
            "coords_soupape" : np.array([0, 0]),
            "inclinaison_soupape" : 0,
            "levier" : levier,
            "coords_levier" : np.array([35.6e-3, 5.4e-3]),
            "angle_leviercame_init" : 5.3 *DEGREE_TO_RADIAN,
            "angles_limites_patinsoupape" : (25,35),
            "angles_limites_patincame" :(20,25)
        }
        distribution = AssemblageLinguet.from_dict(init_dict)
        np.testing.assert_equal(distribution.to_dict(), init_dict)

    def test_distribution_model_comparaison(self):
        came = Came()
        levier = Levier()
        ressort = Ressort()
        soupape = SoupapeSansPoussoir()
        init_dict = {
            "angle_came" : 0,
            "came" : came,
            "coords_came" : np.array([14.2e-3, 31.7e-3]),
            "sens_rotation_came" : 1,
            "ressort" : ressort,
            "soupape" : soupape,
            "coords_soupape" : np.array([0, 0]),
            "inclinaison_soupape" : 0,
            "levier" : levier,
            "coords_levier" : np.array([35.6e-3, 5.4e-3]),
            "angle_leviercame_init" : 5.3 *DEGREE_TO_RADIAN,
            "angles_limites_patinsoupape" : (25,35),
            "angles_limites_patincame" :(20,25)
        }
        distribution1 = AssemblageLinguet.from_dict(init_dict)
        distribution2 = AssemblageLinguet.from_dict(init_dict)
        assert distribution1 == distribution2

    def test_distribution_model_angle_came(self):
        came = Came()
        levier = Levier()
        ressort = Ressort()
        soupape = SoupapeSansPoussoir()
        init_dict = {
            "angle_came" : 7,
            "came" : came,
            "coords_came" : np.array([14.2e-3, 31.7e-3]),
            "sens_rotation_came" : 1,
            "ressort" : ressort,
            "soupape" : soupape,
            "coords_soupape" : np.array([0, 0]),
            "inclinaison_soupape" : 0,
            "levier" : levier,
            "coords_levier" : np.array([35.6e-3, 5.4e-3]),
            "angle_leviercame_init" : 5.3 *DEGREE_TO_RADIAN,
            "angles_limites_patinsoupape" : (25,35),
            "angles_limites_patincame" :(20,25)
        }
        with pytest.raises(ValueError):
            AssemblageLinguet.from_dict(init_dict)

class Test_AssemblageDirecte:
    def test_distribution_model_init(self):
        came = Came()
        ressort = Ressort()
        soupape = SoupapeAvecPoussoir()
        distribution = AssemblageDirecte(
            angle_came = 0,
            came = came,
            coords_came = np.array([14.2e-3, 31.7e-3]),
            sens_rotation_came = 1,
            ressort = ressort,
            soupape = soupape,
            coords_soupape = np.array([0, 0]),
            inclinaison_soupape = 0,
            offset = 1
        )
        assert distribution.angle_came == 0
        assert distribution.came == came
        assert np.array_equal(distribution.coords_came, np.array([14.2e-3, 31.7e-3]))
        assert distribution.sens_rotation_came == 1
        assert distribution.ressort == ressort
        assert distribution.soupape == soupape
        assert np.array_equal(distribution.coords_soupape, np.array([0, 0]))
        assert distribution.inclinaison_soupape == 0
    
    def test_distribution_model_from_dict(self):
        came = Came()
        ressort = Ressort()
        soupape = SoupapeAvecPoussoir()
        init_dict = {
            "angle_came" : 0,
            "came" : came,
            "coords_came" : np.array([14.2e-3, 31.7e-3]),
            "sens_rotation_came" : 1,
            "ressort" : ressort,
            "soupape" : soupape,
            "coords_soupape" : np.array([0, 0]),
            "inclinaison_soupape" : 0,
            "offset" : 1
        }
        distribution = AssemblageDirecte.from_dict(init_dict)
        assert distribution.angle_came == 0
        assert distribution.came == came
        assert np.array_equal(distribution.coords_came, np.array([14.2e-3, 31.7e-3]))
        assert distribution.sens_rotation_came == 1
        assert distribution.ressort == ressort
        assert distribution.soupape == soupape
        assert np.array_equal(distribution.coords_soupape, np.array([0, 0]))
        assert distribution.inclinaison_soupape == 0
        assert distribution.offset == 1

    def test_distribution_model_to_dict(self):
        came = Came()
        ressort = Ressort()
        soupape = SoupapeAvecPoussoir()
        init_dict = {
            "angle_came" : 0,
            "came" : came,
            "coords_came" : np.array([14.2e-3, 31.7e-3]),
            "sens_rotation_came" : 1,
            "ressort" : ressort,
            "soupape" : soupape,
            "coords_soupape" : np.array([0, 0]),
            "inclinaison_soupape" : 0,
            "offset" : 1
        }
        distribution = AssemblageDirecte.from_dict(init_dict)
        np.testing.assert_equal(distribution.to_dict(), init_dict)

    def test_distribution_model_comparaison(self):
        came = Came()
        ressort = Ressort()
        soupape = SoupapeAvecPoussoir()
        init_dict = {
            "angle_came" : 0,
            "came" : came,
            "coords_came" : np.array([14.2e-3, 31.7e-3]),
            "sens_rotation_came" : 1,
            "ressort" : ressort,
            "soupape" : soupape,
            "coords_soupape" : np.array([0, 0]),
            "inclinaison_soupape" : 0,
            "offset" : 1
        }
        distribution1 = AssemblageDirecte.from_dict(init_dict)
        distribution2 = AssemblageDirecte.from_dict(init_dict)
        assert distribution1 == distribution2

    def test_distribution_model_angle_came(self):
        came = Came()
        ressort = Ressort()
        soupape = SoupapeAvecPoussoir()
        init_dict = {
            "angle_came" : 7,
            "came" : came,
            "coords_came" : np.array([14.2e-3, 31.7e-3]),
            "sens_rotation_came" : 1,
            "ressort" : ressort,
            "soupape" : soupape,
            "coords_soupape" : np.array([0, 0]),
            "inclinaison_soupape" : 0,
            "offset" : 1
        }
        with pytest.raises(ValueError):
            AssemblageDirecte.from_dict(init_dict)