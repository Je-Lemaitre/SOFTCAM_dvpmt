# This Python file uses the following encoding: utf-8
import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")
import numpy as np

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
import pyqtgraph as pg

import domain.services.unitees as unit
from infrastructure.ui.lubrication_dialog import Ui_LubricationDialog
from infrastructure.controllers.controller import Controller


class LubricationDialog(QDialog, Ui_LubricationDialog):
    def __init__(self, controller : Controller):
        super(LubricationDialog, self).__init__()

        self.controller = controller

        self.setupUi(self)

        ## Affichage Complémentaire
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)

        # Intervalles Affichage par Défault
        self.angle_range = (0, 200)
        self.pressure_range = (0, 1500)
        

        self.angle_evalpts = np.arange(0, 10/9*np.pi, 0.001)
        self.lubrication_static = None
        self.lubrication_usespeed = None
        self.lubrication_floatspeed = None

        self.floatspeedEdit.setText(str(round(float(self.controller.current_study.loiscame.demilois_ouverture.regime_affolement_opt) /unit.RPM_TO_RADPSEC, 3)))
        self.usespeedEdit.setText("7500")
        self.limitthicknessEdit.setText("2") 
        
        self.minthickness_static_line = pg.InfiniteLine(
            pos= 850, 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        self.minthickness_usespeed_line = pg.InfiniteLine(
            pos= 850, 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        self.minthickness_floatspeed_line = pg.InfiniteLine(
            pos= 850, 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        
        self.stackedWidget.setCurrentIndex(0)
        
        self.computeButton.clicked.connect(self.compute_thickness)
        self.camrockerarmButton.clicked.connect(self.show_camrockerarm)
        self.valverockerarmButton.clicked.connect(self.show_valverockerarm)
        self.camvalveButton.clicked.connect(self.show_camvalve)
        self.resetviewButton.clicked.connect(self.reset_view)
        
    def accept(self):
        
        super().accept()

    def compute_thickness(self):
        pass

    def reset_view(self):
        pass

    def show_camrockerarm(self): 
        self.stackedWidget.setCurrentWidget(self.camrockerarmPage)
        
    def show_valverockerarm(self):
        self.stackedWidget.setCurrentWidget(self.valverockerarmPage)
        
    def show_camvalve(self):
        self.stackedWidget.setCurrentWidget(self.camvalvePage)
    