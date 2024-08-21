import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import numpy as np

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
import pyqtgraph as pg

import domain.services.unitees as unit

from infrastructure.ui.pv_dialog import Ui_PVDialog
from infrastructure.controllers.controller import Controller


class PVDialog(QDialog, Ui_PVDialog):
    def __init__(self, controller : Controller):
        super(PVDialog, self).__init__()

        self.controller = controller

        self.setupUi(self)

        ## Affichage Complémentaire
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)

        # Intervalles Affichage par Défault
        self.angle_range = (0, 200)
        self.pressure_range = (0, 1500)
        

        self.angle_evalpts = np.arange(0, 10/9*np.pi, 0.001)
        self.pv_camrockerarm = None
        self.pv_valverockerarm = None
        self.pv_camvalve = None

        self.floatspeedEdit.setText(str(round(float(self.controller.current_study.loiscame.demilois_ouverture.regime_affolement_opt) /unit.RPM_TO_RADPSEC, 3)))
        self.usespeedEdit.setText("7500")
        self.limitpvEdit.setText("1000") 
        
        self.maxpv_camrockerarm_line = pg.InfiniteLine(
            pos= 850, 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        self.maxpv_valverockerarm_line = pg.InfiniteLine(
            pos= 850, 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        self.maxpv_camvalve_line = pg.InfiniteLine(
            pos= 850, 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        
        self.stackedWidget.setCurrentIndex(0)
        
        self.computeButton.clicked.connect(self.compute_pv)
        self.camrockerarmButton.clicked.connect(self.show_camrockerarm)
        self.valverockerarmButton.clicked.connect(self.show_valverockerarm)
        self.camvalveButton.clicked.connect(self.show_camvalve)
        self.resetviewButton.clicked.connect(self.reset_view)
        
    def accept(self):
        super().accept()

    def compute_pv(self):
        pass

    def reset_view(self):
        pass

    def show_camrockerarm(self): 
        self.stackedWidget.setCurrentWidget(self.camrockerarmPage)
        
    def show_valverockerarm(self):
        self.stackedWidget.setCurrentWidget(self.valverockerarmPage)
        
    def show_camvalve(self):
        self.stackedWidget.setCurrentWidget(self.camvalvePage)
    