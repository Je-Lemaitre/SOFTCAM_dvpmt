import pytest
from softcam.domain.entities.soupape import SoupapeSansPoussoir, SoupapeAvecPoussoir

class Test_SoupapeSansPoussoir:
    def test_soupape_model_init(self):
        soupape = SoupapeSansPoussoir(
            masse_soupape=43.5e-3,
            masse_coupelle=5.5e-3, #Lunules et Grain compris
            module_young=210e9,
            coefficient_poisson=0.3,
            diametre_soupape = 6e-3
        )
        assert soupape.masse_soupape==43.5e-3
        assert soupape.masse_coupelle==5.5e-3
        assert soupape.module_young==210e9
        assert soupape.coefficient_poisson==0.3
        assert soupape.diametre_soupape==6e-3

    def test_soupape_model_from_dict(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "diametre_soupape":6e-3
        }
        soupape = SoupapeSansPoussoir.from_dict(init_dict)
        assert soupape.masse_soupape==43.5e-3
        assert soupape.masse_coupelle==5.5e-3
        assert soupape.module_young==210e9
        assert soupape.coefficient_poisson==0.3
        assert soupape.diametre_soupape==6e-3

    def test_soupape_model_to_dict(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "diametre_soupape":6e-3
        }
        soupape = SoupapeSansPoussoir.from_dict(init_dict)
        assert soupape.to_dict() == init_dict

    def test_soupape_model_comparaison(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "diametre_soupape":6e-3
        }
        soupape1 = SoupapeSansPoussoir.from_dict(init_dict)
        soupape2 = SoupapeSansPoussoir.from_dict(init_dict)
        assert soupape1 == soupape2

    def test_soupape_model_validate_masses(self):
        init_dict1 = {
            "masse_soupape":-43.5e-3,
            "masse_coupelle":5.5e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "diametre_soupape":6e-3
        }
        init_dict2 = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":-5.5e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "diametre_soupape":6e-3
        }
        with pytest.raises(ValueError):
            SoupapeSansPoussoir.from_dict(init_dict1)
            SoupapeSansPoussoir.from_dict(init_dict2)

    def test_soupape_model_validate_diametre_soupape(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "diametre_soupape":-6e-3
        }
        with pytest.raises(ValueError):
            SoupapeSansPoussoir.from_dict(init_dict)

    def test_soupape_model_validate_module_young(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "module_young":-210e9,
            "coefficient_poisson":0.3,
            "diametre_soupape":6e-3
        }
        with pytest.raises(ValueError):
            SoupapeSansPoussoir.from_dict(init_dict)

    def test_soupape_model_validate_coefficient_poisson(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "module_young":210e9,
            "coefficient_poisson":-1.5,
            "diametre_soupape":6e-3
        }
        with pytest.raises(ValueError):
            SoupapeSansPoussoir.from_dict(init_dict)

class Test_SoupapeAvecPoussoir:
    def test_soupape_model_init(self):
        soupape = SoupapeAvecPoussoir(
            masse_soupape=43.5e-3,
            masse_coupelle=5.5e-3, #Lunules et Grain compris
            masse_poussoir=5e-3,
            diametre_poussoir=25e-3,
            rayon_courbure = 35e-3, #Rayon de courbure au niveau du contact (cas du poussoir courbe)
            largeur_courbure = 6e-3,
            module_young=210e9,
            coefficient_poisson=0.3,
            frottement_poussoir_guide = 0,
        )
        assert soupape.masse_soupape==43.5e-3
        assert soupape.masse_coupelle==5.5e-3
        assert soupape.masse_poussoir==5e-3
        assert soupape.diametre_poussoir==25e-3
        assert soupape.rayon_courbure == 35e-3
        assert soupape.largeur_courbure == 6e-3
        assert soupape.module_young==210e9
        assert soupape.coefficient_poisson==0.3
        assert soupape.frottement_poussoir_guide == 0

    def test_soupape_model_from_dict(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "masse_poussoir":5e-3,
            "diametre_poussoir":25e-3,
            "rayon_courbure":35e-3, 
            "largeur_courbure":6e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "frottement_poussoir_guide":0,
        }
        soupape = SoupapeAvecPoussoir.from_dict(init_dict)
        assert soupape.masse_soupape == 43.5e-3
        assert soupape.masse_coupelle == 5.5e-3
        assert soupape.masse_poussoir == 5e-3
        assert soupape.diametre_poussoir == 25e-3
        assert soupape.rayon_courbure == 35e-3
        assert soupape.largeur_courbure == 6e-3
        assert soupape.module_young == 210e9
        assert soupape.coefficient_poisson == 0.3
        assert soupape.frottement_poussoir_guide == 0

    def test_soupape_model_to_dict(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "masse_poussoir":5e-3,
            "diametre_poussoir":25e-3,
            "rayon_courbure":35e-3, 
            "largeur_courbure":6e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "frottement_poussoir_guide":0,
        }
        soupape = SoupapeAvecPoussoir.from_dict(init_dict)
        assert soupape.to_dict() == init_dict

    def test_soupape_model_comparaison(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "masse_poussoir":5e-3,
            "diametre_poussoir":25e-3,
            "rayon_courbure":35e-3, 
            "largeur_courbure":6e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "frottement_poussoir_guide":0,
        }
        soupape1 = SoupapeAvecPoussoir.from_dict(init_dict)
        soupape2 = SoupapeAvecPoussoir.from_dict(init_dict)
        assert soupape1 == soupape2

    def test_soupape_model_validate_masses(self):
        init_dict1 = {
            "masse_soupape":-43.5e-3,
            "masse_coupelle":5.5e-3,
            "masse_poussoir":5e-3,
            "diametre_poussoir":25e-3,
            "rayon_courbure":35e-3, 
            "largeur_courbure":6e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "frottement_poussoir_guide":0,
        }
        init_dict2 = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":-5.5e-3,
            "masse_poussoir":5e-3,
            "diametre_poussoir":25e-3,
            "rayon_courbure":35e-3, 
            "largeur_courbure":6e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "frottement_poussoir_guide":0,
        }
        init_dict3 = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "masse_poussoir":-5e-3,
            "diametre_poussoir":25e-3,
            "rayon_courbure":35e-3, 
            "largeur_courbure":6e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "frottement_poussoir_guide":0,
        }
        with pytest.raises(ValueError):
            SoupapeAvecPoussoir.from_dict(init_dict1)
            SoupapeAvecPoussoir.from_dict(init_dict2)
            SoupapeAvecPoussoir.from_dict(init_dict3)

    def test_soupape_model_validate_diametre_poussoir(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "masse_poussoir":5e-3,
            "diametre_poussoir":-25e-3,
            "rayon_courbure":35e-3, 
            "largeur_courbure":6e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "frottement_poussoir_guide":0,
        }
        with pytest.raises(ValueError):
            SoupapeAvecPoussoir.from_dict(init_dict)

    def test_soupape_model_validate_largeur_courbure(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "masse_poussoir":5e-3,
            "diametre_poussoir":25e-3,
            "rayon_courbure":35e-3, 
            "largeur_courbure":-6e-3,
            "module_young":210e9,
            "coefficient_poisson":0.3,
            "frottement_poussoir_guide":0,
        }
        with pytest.raises(ValueError):
            SoupapeAvecPoussoir.from_dict(init_dict)

    def test_soupape_model_validate_module_young(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "masse_poussoir":5e-3,
            "diametre_poussoir":25e-3,
            "rayon_courbure":35e-3, 
            "largeur_courbure":6e-3,
            "module_young":-210e9,
            "coefficient_poisson":0.3,
            "frottement_poussoir_guide":0,
        }
        with pytest.raises(ValueError):
            SoupapeAvecPoussoir.from_dict(init_dict)

    def test_soupape_model_validate_coefficient_poisson(self):
        init_dict = {
            "masse_soupape":43.5e-3,
            "masse_coupelle":5.5e-3,
            "masse_poussoir":5e-3,
            "diametre_poussoir":25e-3,
            "rayon_courbure":35e-3, 
            "largeur_courbure":6e-3,
            "module_young":210e9,
            "coefficient_poisson":0.7,
            "frottement_poussoir_guide":0,
        }
        with pytest.raises(ValueError):
            SoupapeAvecPoussoir.from_dict(init_dict)