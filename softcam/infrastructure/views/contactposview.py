# This Python file uses the following encoding: utf-8
import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")
import numpy as np

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
import pyqtgraph as pg

import domain.services.unitees as unit
from infrastructure.ui.contactpos_dialog import Ui_ContactPosDialog
from infrastructure.controllers.controller import Controller


class ContactPosDialog(QDialog, Ui_ContactPosDialog):
    def __init__(self, controller : Controller):
        super(ContactPosDialog, self).__init__()

        self.controller = controller

        self.setupUi(self)

        ## Affichage Complémentaire
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)

        # Intervalles Affichage par Défault
        self.x_range = (0, 200)
        self.y_range = (-20, 20)

        self.angles = None
        self.angles_contact_camepatin = None

        self.poslimitEdit.setText("35")
        self.neglimitEdit.setText("25")     

        self.neglimit_camrockerarm_line = pg.InfiniteLine(
            pos= 35, 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        self.poslimit_camrockerarm_line = pg.InfiniteLine(
            pos= -25, 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        
        self.neglimit_valverockerarm_line = pg.InfiniteLine(
            pos= 35, 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        self.poslimit_valverockerarm_line = pg.InfiniteLine(
            pos= -25, 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        
        self.neglimit_camvalve_line = pg.InfiniteLine(
            pos= 35, 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        self.poslimit_camvalve_line = pg.InfiniteLine(
            pos= -25, 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        
        self.camrockerarmPlotWidget.addItem(self.neglimit_camrockerarm_line)
        self.camrockerarmPlotWidget.addItem(self.poslimit_camrockerarm_line)
        self.valverockerarmPlotWidget.addItem(self.neglimit_valverockerarm_line)
        self.valverockerarmPlotWidget.addItem(self.poslimit_valverockerarm_line)
        self.camvalvePlotWidget.addItem(self.neglimit_camvalve_line)
        self.camvalvePlotWidget.addItem(self.poslimit_camvalve_line)
        
        self.stackedWidget.setCurrentIndex(0)
        
        self.computeButton.clicked.connect(self.compute_position)
        self.camrockerarmButton.clicked.connect(self.show_camrockerarm)
        self.valverockerarmButton.clicked.connect(self.show_valverockerarm)
        self.camvalveButton.clicked.connect(self.show_camvalve)
        self.resetviewButton.clicked.connect(self.reset_view)
        
    def accept(self): 
        super().accept()

    def compute_position(self):
        self.angles, self.angles_contact_camepatin = self.controller.compute_contactpos(contact="Came/Patin")

        self.camrockerarmCurve.setData(
            self.angles /unit.DEGREE_TO_RADIAN, 
            self.angles_contact_camepatin /unit.DEGREE_TO_RADIAN
            )


    def reset_view(self):
        self.camrockerarmPlotWidget.setXRange(*self.x_range)
        self.valverockerarmPlotWidget.setXRange(*self.x_range)
        self.camvalvePlotWidget.setXRange(*self.x_range)

        self.camrockerarmPlotWidget.setYRange(*self.y_range)
        self.valverockerarmPlotWidget.setYRange(*self.y_range)
        self.camvalvePlotWidget.setYRange(*self.y_range)

    def show_camrockerarm(self): 
        self.stackedWidget.setCurrentWidget(self.camrockerarmPage)
        
    def show_valverockerarm(self):
        self.stackedWidget.setCurrentWidget(self.valverockerarmPage)
        
    def show_camvalve(self):
        self.stackedWidget.setCurrentWidget(self.camvalvePage)
    