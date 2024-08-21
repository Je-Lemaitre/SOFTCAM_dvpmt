import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import pandas as pd
import openpyxl

from domain.entities.etude import Etude
from application.interfaces.repository_interface import RepositoryInterface

class ExcelRepository(RepositoryInterface):
    """Attention !!! Cette classe n'est pas du tout aboutie. Il n'est actuellement pas possible de convertir une étude en un fichier Excel. Ceci contstitue un manque important. 
    À terme, implémentation du repository permettant de charger une étude d'un fichier excel et de la sauvegarder en un fichier excel.

    Args:
        path (str): Le chemin d'accès au fichier excel.

    Methods:
        load_data() -> Etude:
            Charge une étude à partir d'un fichier Excel et crée une instance de la classe Etude.
        save_data(study: Etude):
            Sauvegarde les données de l'étude chargée en un fichier excel. Cette fonction importante aux yeux de Frédéric n'est pas implémenté et donc pas fonctionnelle.
        load_profile(profile_path: str):
            Charge un profil de came à partir d'un fichier excel. Cette fonction ne peut pas être utilisée actuellement.
    """
    def __init__(self, path: str):
        super(ExcelRepository, self).__init__(path)

    def load_data(self):
        try:
            with open(self.study_path, 'r') as file:
                data = json.load(file)
            return Etude.from_dict(data)
        except FileNotFoundError:
            return None
        
        try:
            df = pd.read_excel(self.file_path)
            return [User(row['user_id'], row['name'], row['age'], row['city']) for index, row in df.iterrows()]
        except FileNotFoundError:
            return []

    def save_data(self, study : Etude):
        with open(self.study_path, 'w') as file:
            json.dump(study.to_dict(), file, indent=4)
        
        df = pd.DataFrame([user.__dict__ for user in users])
        df.to_excel(self.file_path, index=False)

    def load_profile(self, profile_path):
        try:
            with open(profile_path, 'r') as file:
                profile = json.load(file)
            return profile
        except FileNotFoundError:
            return None
        
        try:
            df = pd.read_excel(self.file_path)
            return [User(row['user_id'], row['name'], row['age'], row['city']) for index, row in df.iterrows()]
        except FileNotFoundError:
            return []