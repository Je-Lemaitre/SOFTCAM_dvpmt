# This Python file uses the following encoding: utf-8
import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")

import domain.services.unitees as unit

from PySide6.QtWidgets import QDialog
from infrastructure.ui.patin_dialog import Ui_PatinDialog
from infrastructure.ui.rockerarm_dialog import Ui_LinguetDialog
from infrastructure.controllers.controller import Controller

class LinguetDialog(QDialog, Ui_LinguetDialog):
    def __init__(self, controller : Controller):
        super(LinguetDialog, self).__init__()
        
        self.controller = controller
        self.rockerarm = controller.current_study.assemblage.levier
        
        self.setupUi(self)

        self.massEdit.setText(str(round(self.rockerarm.masse /unit.GRAMM_TO_KILOGRAMM, 3)))
        self.inertiaEdit.setText(str(round(self.rockerarm.inertie /unit.GRAMM_TO_KILOGRAMM/unit.MILLIMETER_TO_METER**2, 3)))
        self.lengthEdit.setText(str(round(self.rockerarm.longueur /unit.MILLIMETER_TO_METER, 3)))

        self.createpcButton.clicked.connect(self.open_patincame_dialog)
        self.createpsButton.clicked.connect(self.open_patinsoup_dialog)
    
    def accept(self):
        
        masse = float(self.massEdit.text()) *unit.GRAMM_TO_KILOGRAMM
        inertie = float(self.inertiaEdit.text()) *unit.GRAMM_TO_KILOGRAMM*unit.MILLIMETER_TO_METER**2
        longueur = float(self.lengthEdit.text()) *unit.MILLIMETER_TO_METER
        
        self.controller.update_rockerarm(
            masse = masse,
            inertie = inertie, 
            longueur = longueur)

        super().accept()

    def open_patincame_dialog(self):
        patin_dialog = PatinDialog(controller = self.controller, loc="came")
        patin_dialog.exec()
    
    def open_patinsoup_dialog(self):
        patin_dialog = PatinDialog(controller = self.controller, loc="soupape")
        patin_dialog.exec()

class PatinDialog(QDialog, Ui_PatinDialog):
    def __init__(self, controller : Controller, loc = "soupape"):
        super(PatinDialog, self).__init__()

        self.loc = loc

        self.controller = controller
        if loc == "came":
            self.patin = controller.current_study.assemblage.levier.patin_came

        elif loc == "soupape":
            self.patin = controller.current_study.assemblage.levier.patin_soupape
        self.setupUi(self)

        self.setWindowTitle(f"Patin coté {self.loc}")
        self.rpEdit.setText(str(round(self.patin.rayon_courbure /unit.MILLIMETER_TO_METER, 3)))
        self.widthEdit.setText(str(round(self.patin.largeur /unit.MILLIMETER_TO_METER, 3)))
        self.youngEdit.setText(str(round(self.patin.module_young /unit.GIGAPASCAL_TO_PASCAL, 3)))
        self.poissonEdit.setText(str(self.patin.coefficient_poisson))

    def accept(self):
        rayon_courbure = float(self.rpEdit.text()) *unit.MILLIMETER_TO_METER
        largeur = float(self.widthEdit.text()) *unit.MILLIMETER_TO_METER
        module_young = float(self.youngEdit.text()) *unit.GIGAPASCAL_TO_PASCAL
        coefficient_poisson = float(self.poissonEdit.text())

        self.controller.update_patin(
            loc = self.loc,
            rayon_courbure=rayon_courbure,
            largeur=largeur,
            module_young=module_young,
            coefficient_poisson=coefficient_poisson
        )
        super().accept()