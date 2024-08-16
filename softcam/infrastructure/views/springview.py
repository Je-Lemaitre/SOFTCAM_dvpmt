import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")

from PySide6.QtWidgets import QDialog

import domain.services.unitees as unit
from infrastructure.ui.spring_dialog import Ui_RessortDialog
from infrastructure.controllers.controller import Controller

class RessortDialog(QDialog, Ui_RessortDialog):
    def __init__(self, controller : Controller):
        super(RessortDialog, self).__init__()

        self.controller = controller
        self.spring = controller.current_study.assemblage.ressort

        self.setupUi(self)

        self.massEdit.setText(str(round(self.spring.masse /unit.GRAMM_TO_KILOGRAMM, 3)))
        self.stiffnessEdit.setText(str(round(self.spring.raideur *unit.MILLIMETER_TO_METER, 3)))
        self.preloadEdit.setText(str(round(self.spring.precharge, 3)))
    
    def accept(self):
        masse = float(self.massEdit.text()) *unit.GRAMM_TO_KILOGRAMM
        raideur = float(self.stiffnessEdit.text()) /unit.MILLIMETER_TO_METER
        precharge = float(self.preloadEdit.text()) 

        self.controller.update_spring(
            masse=masse,
            raideur=raideur,
            precharge=precharge
        )

        super().accept()
    
    