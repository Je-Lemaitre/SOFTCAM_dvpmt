import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt

import domain.services.unitees as unit
from infrastructure.ui.option_dialog import Ui_OptionDialog
from infrastructure.controllers.controller import Controller


class OptionDialog(QDialog, Ui_OptionDialog):
    def __init__(self, controller : Controller):
        super(OptionDialog, self).__init__()

        self.controller = controller

        self.setupUi(self)

        ## Affichage Complémentaire
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)

        # Intervalles Affichage par Défault
        self.studynameEdit.setText(self.controller.current_study.nom)
        self.stepangleEdit.setText(str(round(self.controller.current_study.pas_angulaire /unit.DEGREE_TO_RADIAN, 6)))
        self.stepdisplayEdit.setText(str(round(self.controller.precision /unit.DEGREE_TO_RADIAN, 6)))
        self.steptimeEdit.setText(str(round(self.controller.current_study.pas_temporel /unit.MILLISECOND_TO_SECOND, 3)))
        
        
    def accept(self):
        
        super().accept()
    