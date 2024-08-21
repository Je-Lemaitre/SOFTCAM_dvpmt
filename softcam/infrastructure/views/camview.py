import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import QCoreApplication

import domain.services.unitees as unit

from infrastructure.ui.cam_dialog import Ui_CamDialog
from infrastructure.controllers.controller import Controller

class CamDialog(QDialog, Ui_CamDialog):
    def __init__(self, controller : Controller, parent = None):
        super(CamDialog, self).__init__(parent)

        self.controller = controller
        self.cam = controller.current_study.assemblage.came

        self.setupUi(self)
        self.browseProfileButton.clicked.connect(self.open_filebrowser_dialog)
        self.profile_path = None
        self.profile_name = None

        self.rbEdit.setText(str(round(self.cam.rayon_base /unit.MILLIMETER_TO_METER, 3)))
        self.widthEdit.setText(str(round(self.cam.largeur /unit.MILLIMETER_TO_METER, 3)))
        self.youngEdit.setText(str(round(self.cam.module_young /unit.GIGAPASCAL_TO_PASCAL, 3)))
        self.poissonEdit.setText(str(self.cam.coefficient_poisson))
        self.browseProfileButton.setText(str(self.profile_name))
    
    def open_filebrowser_dialog(self):
        filebrowser_dialog = QFileDialog()
        file = filebrowser_dialog.getOpenFileName()
        self.file_path = file[0]
        self.file_name = self.file_path.split("/")[-1]
        self.browseProfileButton.setText(QCoreApplication.translate("CamDialog", self.file_name, None))
    
    def accept(self):
        rayon_base = float(self.rbEdit.text()) *unit.MILLIMETER_TO_METER
        largeur = float(self.widthEdit.text()) *unit.MILLIMETER_TO_METER
        module_young = float(self.youngEdit.text()) *unit.GIGAPASCAL_TO_PASCAL
        coefficient_poisson = float(self.poissonEdit.text())
        if self.profile_path is None :
            profil = None
        else :
            profil = self.controller.load_profile(self.profile_path)
        
        self.controller.update_cam(
            rayon_base = rayon_base,
            largeur = largeur,
            module_young = module_young,
            coefficient_poisson = coefficient_poisson,
            profil = profil
        )
        super().accept()