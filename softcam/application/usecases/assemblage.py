import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import numpy as np
from application.interfaces.controller_interface import ControllerInterface

class MetAJourAssemblage():
    def __init__(self, controller : ControllerInterface):
        self.controller = controller
        self.assemblage = controller.current_study.assemblage

    def __call__(
            self, 
            sens_rotation_came : int, 
            coords_levier : list, 
            coords_came : list, 
            angle_leviercame_init : float, 
            inclinaison_soupape : float):

        self.assemblage.sens_rotation_came = sens_rotation_came
        self.assemblage.coords_levier = np.array(coords_levier)
        self.assemblage.coords_came = np.array(coords_came)
        self.assemblage.angle_leviercame_init = angle_leviercame_init
        self.assemblage.inclinaison_soupape = inclinaison_soupape