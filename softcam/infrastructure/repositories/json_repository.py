# infrastructure/persistence/json_repository.py
import json
from domain.entities.etude import Etude
from application.interfaces.repository_interface import RepositoryInterface
import numpy as np

class JSONRepository(RepositoryInterface):
    def __init__(self, path: str):
        super(JSONRepository, self).__init__(path)

    def load_data(self):
        try:
            with open(self.study_path, 'r') as file:
                data = json.load(file, object_hook=self.deconvert)
            return Etude.from_dict(data)
        except FileNotFoundError:
            return None
    
    def save_data(self, study : Etude):
        with open(self.study_path, 'w') as file:
            json.dump(study.to_dict(), file, indent=4, default=self.convert)

    def load_profile(self, profile_path):
        try:
            with open(profile_path, 'r') as file:
                profile = json.load(file)
            return profile
        except FileNotFoundError:
            return None
        
    def convert(self, x):
        if hasattr(x, "tolist"):  # numpy arrays have this
            x_converted = x.tolist()
            if isinstance(x_converted, list) :
                return {"$array": x_converted}  # Make a tagged object
            else : 
                return x_converted
        raise TypeError(x)


    def deconvert(self, x):
        if len(x) == 1:  # Might be a tagged object...
            key, value = next(iter(x.items()))  # Grab the tag and value
            if key == "$array":  # If the tag is correct,
                return np.array(value)  # cast back to array
        return x

