# infrastructure/persistence/json_repository.py
import pandas as pd
import openpyxl
from domain.entities.etude import Etude
from application.interfaces.repository_interface import RepositoryInterface

class ExcelRepository(RepositoryInterface):
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