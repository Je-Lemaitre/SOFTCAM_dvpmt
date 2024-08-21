import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from abc import ABC, abstractmethod

from domain.entities.etude import Etude

class RepositoryInterface(ABC):
    def __init__(self, path):
        self.study_path = path
        self.profile_path = None

    @abstractmethod
    def load_data(self) -> Etude :
        pass

    @abstractmethod
    def save_data(self, study : Etude) -> None:
        pass

    @abstractmethod
    def load_profile(self, profile_path : str) -> dict:
        pass