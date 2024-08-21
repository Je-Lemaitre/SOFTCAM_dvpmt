import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from scipy.interpolate import BSpline
import numpy as np

from application.usecases.etude import CreeEtude, EnregistreEtude, ChargeEtude, ExportExcel, CreeUtilitairesCalcul, CalculVitesseGlissement, CalculPositionContact, CalculPressionHertz
from application.usecases.assemblage import MetAJourAssemblage
from application.usecases.soupape import MetAJourSoupape, MetAJourPoussoir
from application.usecases.ressort import MetAJourRessort
from application.usecases.levier import MetAJourLevier, MetAJourPatinSoupape, MetAJourPatinCame
from application.usecases.came import ChargeProfil, MetAJourCame, CalculProfil, CalculRayonCourbure, CalculRollerDisplacement
from application.usecases.loiscame import CreeLois, CalculLoisReelles, CalculEfficacite
from application.interfaces.repository_interface import RepositoryInterface
from application.interfaces.controller_interface import ControllerInterface
from domain.entities.soupape import Poussoir

class Controller(ControllerInterface):
    """Implémentation complète du contrôleur.

    Cette classe permet de contrôler l'application et de faire le lien entre les données stockées, la logique de l'application et l'interface utilisateur. Chaque méthode de cette classe représente un cas d'usage et appelle la classe correspondante parmi celles du module application.usecases . C'est également cette classe qui permet de stocker les données temporaires de l'application.
    Les fonctions qui réalisent des mises à jours sont appelées à chaque fois que l'utilisateur clique sur le bouton "Ok" d'une boite de dialogue. 

    Args:
        repository (RepositoryInterface): Le repository utilisé pour stocker les données.

    Attributes:
        repository (RepositoryInterface): Le repository utilisé pour stocker les données.
        precision (float): La précision utilisée pour les calculs, en angle de rotation de la came, 0.001 par défaut.
        current_study (Etude): L'étude chargée.
        current_laws (LoisCame): Les lois de distribution étudiées.
        calccinematique (CalculsCinematique): Utilitaire pour les calculs cinématique.
        calcprofil (CalculsProfilCame): Utilitaire pour les calculs des grandeurs liées au profil de la came.
        calcmecanique (CalculsMecanique): Utilitaire pour les calculs des critères de dimensionnement mécaniques.

    Methods:
        create_study(name, assembly_type, step_time):
            Crée une nouvelle loi.
        load_study():
            Charge une étude existante.
        save_study():
            Sauvegarde l'étude actuellement chargée en session.
        export_to_excel():
            Exporte l'étude dans un fichier Excel (non implémentée).
        load_profile(profile_path):
            Charge un profil de came existant.
        update_study_path(path):
            Met à jour le chemin d'accès à l'étude.
        update_profile_path(path):
            Met à jour le chemin d'accès au profil.
        update_precision(new_precision):
            Met à jour la précision de calcul.
        update_options(studyname, stepangle, stepdisplay, steptime):
            Met à jour les options (non implémenté).
        update_rockerarmassembly(sens_rotation_came, coords_levier, coords_came, angle_leviercame_init, inclinaison_soupape):
            Met à jour l'assemblage à levier.
        update_valve(masse_soupape, masse_coupelle, diametre_soupape, poussoir, module_young, coefficient_poisson):
            Met à jour la soupape.
        update_tappet(masse, diametre, rayon_courbure, largeur_courbure, frottement_poussoir_guide):
            Met à jour le poussoir.
        update_spring(masse, raideur, precharge):
            Met à jour le ressort.
        update_rockerarm(masse, inertie, longueur):
            Met à jour le levier.
        update_patin(loc, rayon_courbure, largeur, module_young, coefficient_poisson):
            Met à jour le patin.
        update_cam(rayon_base, largeur, module_young, coefficient_poisson, profil):
            Met à jour la came.
        update_laws():
            Met à jour les lois.
        update_curvature(cutting_radius, curvature):
            Met à jour le rayon de courbure.
        update_roller(roller_radius, displacement):
            Met à jour les coordonnées polaires du centre du roller.
        optimise_laws(symmetry, valve_float_speed, openaccel_skl_raw, closeaccel_skl_raw, openspeed_skl_raw, closespeed_skl_raw, openlift_skl_raw, closelift_skl_raw, openjoin_angle_raw, closejoin_angle_raw):
            Ajuste les demi-lois de distribution.
        compute_effective_laws(clearance):
            Calcule les lois réelle.
        compute_opening(clearance):
            Calcule l'ouverture de la loi de levée.
        compute_area(clearance):
            Calcule l'aire sous la courbe de levée réelle.
        compute_efficiency(clearance):
            Calcule l'efficacité.
        compute_profile():
            Calcule le profil de la came en coordonnées cartésiennes.
        compute_curvature():
            Calcule le rayon de courbure de la came.
        compute_roller_displacement(roller_radius):
            Calcule les coordonnées polaires du centre du roller.
        compute_contactpos(contact):
            Calcul la position du point de contact pour le contact spécifié.
        compute_hertz_pressure(speed, contact):
            Calcul la pression de Hertz pour le régime moteur et le contact indiqués.
        compute_slidingspeed(speed, contact):
            Calcule la vitesse de glissement pour le régime moteur et le contact indiqués.
        check_mechanics():
            Vérifie que les critères de dimensionnement mécaniques sont respectés.
        check_manufacturing():
            Vérifie que les critères de dimensionnement de fabrication sont respectés.
    """
    def __init__(self, repository : RepositoryInterface):
        self.repository = repository
        self.precision = 0.001
        self.current_study = None  # Stocker l'étude actuellement chargée
        self.current_laws = None
        self.calccinematique = None
        self.calcprofil = None
        self.calcmecanique = None
        

    def create_study(self, name, assembly_type, step_time) :
        use_case = CreeEtude(self.repository)
        self.current_study = use_case(name, assembly_type, step_time)
        self.current_laws = self.current_study.loiscame
        self.calccinematique = None
        self.calcprofil = None
        self.calcefforts = None
        return self.current_study

    def load_study(self):
        use_case = ChargeEtude(self.repository)
        self.current_study = use_case()
        return self.current_study
    
    def save_study(self):
        use_case = EnregistreEtude(self.repository)
        return use_case(self.current_study)
    
    def export_to_excel(self):
        use_case = ExportExcel()
        return use_case()
    
    def load_profile(self, profile_path):
        use_case = ChargeProfil(self.repository)
        return use_case(profile_path)
    
    def update_study_path(self, path):
        self.repository.study_path = path
    
    def update_profile_path(self, path):
        self.repository.profile_path = path
    
    def update_precision(self, new_precision):
        self.precision = new_precision
    
    def update_options(self, studyname : str, stepangle : float, stepdisplay : float, steptime : float):
        self.current_study.nom = studyname
        self.current_study.pas_angulaire = stepangle
        self.precision = stepdisplay
        self.current_study.pas_temporel = steptime

    def update_rockerarmassembly(
            self, 
            sens_rotation_came : int, 
            coords_levier : list, 
            coords_came : list, 
            angle_leviercame_init : float, 
            inclinaison_soupape : float
            ):
        
        use_case = MetAJourAssemblage(self)
        return use_case(
            sens_rotation_came = sens_rotation_came, 
            coords_levier = coords_levier, 
            coords_came = coords_came, 
            angle_leviercame_init = angle_leviercame_init, 
            inclinaison_soupape = inclinaison_soupape
            )    
    def update_valve(
            self,
            masse_soupape : float,
            masse_coupelle : float,
            diametre_soupape : float,
            poussoir : Poussoir,
            module_young : float,
            coefficient_poisson : float
        ):

        use_case = MetAJourSoupape(self)
        return use_case(
            masse_soupape = masse_soupape,
            masse_coupelle = masse_coupelle,
            diametre_soupape = diametre_soupape,
            poussoir = poussoir,
            module_young = module_young,
            coefficient_poisson = coefficient_poisson
        )
    def update_tappet(
            self,
            masse : float,
            diametre : float,
            rayon_courbure : float,
            largeur_courbure : float,
            frottement_poussoir_guide : float
            ):

        use_case = MetAJourPoussoir(self)
        return use_case(
            masse = masse,
            diametre = diametre,
            rayon_courbure = rayon_courbure,
            largeur_courbure = largeur_courbure,
            frottement_poussoir_guide = frottement_poussoir_guide
        )  
    def update_spring(
            self,
            masse : float,
            raideur : float,
            precharge : float
        ):

        use_case = MetAJourRessort(self)
        return use_case(
            masse = masse,
            raideur = raideur,
            precharge = precharge
        )  
    def update_rockerarm(
            self,
            masse : float,
            inertie : float,
            longueur : float
        ):

        use_case = MetAJourLevier(self)
        return use_case(
            masse = masse,
            inertie = inertie,
            longueur = longueur
        )
    def update_patin(
            self, 
            loc : str, 
            rayon_courbure : float,
            largeur : float,
            module_young : float,
            coefficient_poisson : float
            ):
        
        if loc == "soupape":
            use_case = MetAJourPatinSoupape(self)
        elif loc == "came":
            use_case = MetAJourPatinCame(self)
        
        return use_case(
            rayon_courbure = rayon_courbure,
            largeur = largeur,
            module_young = module_young,
            coefficient_poisson = coefficient_poisson
        )    
    def update_cam(
            self,
            rayon_base : float,
            largeur : float,
            module_young : float,
            coefficient_poisson : float,
            profil : BSpline
        ):

        use_case = MetAJourCame(self)
        return use_case(
            rayon_base = rayon_base,
            largeur = largeur,
            module_young = module_young,
            coefficient_poisson = coefficient_poisson,
            profil = profil
        )   
    def update_laws(self):
        self.current_study.loiscame = self.current_laws
        use_case = CreeUtilitairesCalcul(self)
        self.calccinematique, self.calcprofil, self.calcmecanique = use_case(
            angles_rotation_evalpts=np.arange(0, 2*np.pi, self.precision)
        )    
    def update_curvature(self, cutting_radius, curvature):
        self.current_study.fabrication.courbure.diametre_meule_taillage = cutting_radius
        self.current_study.fabrication.courbure.rayon_courbure = curvature
    def update_roller(self, roller_radius, displacement):
        self.current_study.fabrication.roller.rayon_roller = roller_radius
        self.current_study.fabrication.roller.deplacement_roller = displacement

    def optimise_laws(self, symmetry : bool, valve_float_speed,
                openaccel_skl_raw, closeaccel_skl_raw,
                openspeed_skl_raw, closespeed_skl_raw, 
                openlift_skl_raw, closelift_skl_raw,
                openjoin_angle_raw, closejoin_angle_raw
                ) :
        angles = np.arange(0, closelift_skl_raw[-1,0], self.precision)
        use_case = CreeLois(self.current_study.assemblage)
        self.current_laws = use_case(
            symetrie = symmetry, 
            regime_affolement_init = valve_float_speed,
            accel_squelbrut_ouverture = openaccel_skl_raw, 
            accel_squelbrut_fermeture = closeaccel_skl_raw,
            vitesse_squelbrut_ouverture = openspeed_skl_raw, 
            vitesse_squelbrut_fermeture = closespeed_skl_raw, 
            levee_squelbrut_ouverture = openlift_skl_raw, 
            levee_squelbrut_fermeture = closelift_skl_raw,
            raccord_anglebrut_ouverture = openjoin_angle_raw, 
            raccord_anglebrut_fermeture = closejoin_angle_raw
            )
        
        return angles, self.current_laws.a(angles), self.current_laws.v(angles), self.current_laws.l(angles)
    
    def compute_effective_laws(self, clearance : float):
        angles = np.arange(0, self.current_laws.dac_leveemax_ouverture + self.current_laws.dac_leveemax_fermeture, self.precision)
        use_case = CalculLoisReelles(self)
        return use_case(angles, clearance)
    
    def compute_opening(self, clearance : float):
        use_case = CalculLoisReelles(self)
        return use_case.calcul_ouverture(jeu = clearance)
    
    def compute_area(self, clearance : float):
        use_case = CalculEfficacite(self)
        return use_case.calcul_aire_reelle(jeu = clearance)
    
    def compute_efficiency(self, clearance : float):
        use_case = CalculEfficacite(self)
        return use_case(jeu = clearance)

    def compute_profile(self):
        use_case = CalculProfil(self)
        return use_case()
    
    def compute_curvature(self) :
        use_case = CalculRayonCourbure(self)
        return use_case(angles_rotation=np.arange(0, 2*np.pi, self.precision))
    
    def compute_roller_displacement(self, roller_radius : float = 8.5e-3):
        use_case = CalculRollerDisplacement(self)
        return use_case(
            angles_rotation=np.arange(0, 2*np.pi, self.precision),
            rayon_roller=roller_radius
            )
    
    def compute_contactpos(self, contact=None):
        angles_evalpts = np.arange(0, 2*np.pi, self.precision)
        use_case = CalculPositionContact(self)
        contactpos = use_case(
            angles_rotation=angles_evalpts,
            contact=contact
        )
        return angles_evalpts, contactpos
        
    def compute_sliding_speed(self, speed):
        pass
    def compute_hertz_pressure(self, speed : float, contact : str) :
        use_case = CalculPressionHertz(self)
        angles_evalpts = np.arange(0, 2*np.pi, self.precision)
        phertz = use_case(
            angles_rotation=angles_evalpts, 
            regime_moteur=speed,
            contact=contact
            )
        return angles_evalpts, phertz
    
    def compute_slidingspeed(self, speed : float , contact : str = None):
        use_case = CalculVitesseGlissement(self)
        angles_evalpts = np.arange(0, 2*np.pi, self.precision)
        slidingspeed = use_case(
            angles_rotation=angles_evalpts, 
            regime_moteur=speed,
            contact=contact
            )
        return angles_evalpts, slidingspeed

    def check_mechanics(self):
        pass
    def check_manufacturing(self):
        pass
    
    
    

