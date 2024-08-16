# This Python file uses the following encoding: utf-8
import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")
import numpy as np

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
import pyqtgraph as pg

import domain.services.unitees as unit
from infrastructure.ui.roller_dialog import Ui_RollerDialog
from infrastructure.controllers.controller import Controller


class RollerDialog(QDialog, Ui_RollerDialog):
    def __init__(self, controller : Controller):
        super(RollerDialog, self).__init__()

        self.controller = controller

        self.setupUi(self)

        ## Affichage Complémentaire
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)

        # Intervalles Affichage par Défault
        self.x_range = (0, 200)
        self.y_range = (self.controller.current_study.assemblage.came.rayon_base /unit.MILLIMETER_TO_METER, 40)
        
        roller = self.controller.current_study.fabrication.roller
        try :
            self.curvedata = np.column_stack((
                roller.deplacement_roller[:,0] /unit.DEGREE_TO_RADIAN,
                roller.deplacement_roller[:,1] /unit.MILLIMETER_TO_METER
            ))
            self.displacementCurve.setData(self.curvedata)
        except :
            self.curvedata = None

        self.rollerradiusEdit.setText(str(round(roller.rayon_roller /unit.MILLIMETER_TO_METER, 3)))
        
        self.stackedWidget.setCurrentIndex(0)
        
        self.computeButton.clicked.connect(self.compute_displacement)
        self.resetviewButton.clicked.connect(self.reset_view)
        
    def accept(self):
        roller_radius = float(self.rollerradiusEdit.text()) *unit.MILLIMETER_TO_METER
        displacement = np.column_stack((
            self.curvedata[:,0] *unit.DEGREE_TO_RADIAN,
            self.curvedata[:,1] *unit.MILLIMETER_TO_METER
        ))
        self.controller.update_roller(
            roller_radius = roller_radius,
            displacement = displacement
        ) 
        super().accept()

    def compute_displacement(self):
        roller_radius = float(self.rollerradiusEdit.text()) *unit.MILLIMETER_TO_METER
        displacement = self.controller.compute_roller_displacement(roller_radius)
        self.curvedata = np.column_stack((
            displacement[:,0] /unit.DEGREE_TO_RADIAN, 
            displacement[:,1] /unit.MILLIMETER_TO_METER
            ))
        self.displacementCurve.setData(self.curvedata)

    def reset_view(self):
        self.displacementPlotWidget.setXRange(*self.x_range)
        self.displacementPlotWidget.setYRange(*self.y_range)
    
    