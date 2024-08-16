# This Python file uses the following encoding: utf-8
import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")
import numpy as np

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
import pyqtgraph as pg

import domain.services.unitees as unit
from infrastructure.ui.slidingspeed_dialog import Ui_SlidingSpeedDialog
from infrastructure.controllers.controller import Controller


class SlidingSpeedDialog(QDialog, Ui_SlidingSpeedDialog):
    def __init__(self, controller : Controller):
        super(SlidingSpeedDialog, self).__init__()

        self.controller = controller

        self.setupUi(self)

        ## Affichage Complémentaire
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)

        # Intervalles Affichage par Défault
        self.x_range = (0, 200)
        self.y_range = (-20, 20)
        
        self.angles = None
        self.slidingspeed_usespeed_camepatin = None
        self.slidingspeed_usespeed_soupapepatin = None
        self.slidingspeed_floatspeed_camepatin = None
        self.slidingspeed_floatspeed_soupapepatin = None

        self.floatspeedEdit.setText(str(round(float(self.controller.current_study.loiscame.demilois_ouverture.regime_affolement_opt) /unit.RPM_TO_RADPSEC, 3)))
        self.usespeedEdit.setText("7500")
        self.limitspeedEdit.setText("18")
        
        self.maxspeed_usespeed_line = pg.InfiniteLine(
            pos= float(self.limitspeedEdit.text()), 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=1.5) 
            )
        self.minspeed_usespeed_line = pg.InfiniteLine(
            pos= -float(self.limitspeedEdit.text()), 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=1.5) 
            )
        self.maxspeed_floatspeed_line = pg.InfiniteLine(
            pos= float(self.limitspeedEdit.text()), 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=1.5) 
            )
        self.minspeed_floatspeed_line = pg.InfiniteLine(
            pos= -float(self.limitspeedEdit.text()), 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=1.5) 
            )
        
        self.usespeedPlotWidget.addItem(self.maxspeed_usespeed_line)
        self.usespeedPlotWidget.addItem(self.minspeed_usespeed_line)
        self.floatspeedPlotWidget.addItem(self.maxspeed_floatspeed_line)
        self.floatspeedPlotWidget.addItem(self.minspeed_floatspeed_line)

        self.stackedWidget.setCurrentIndex(0)
        
        self.contactComboBox.currentTextChanged.connect(self.change_display_graph)
        
        self.computeButton.clicked.connect(self.compute_speed)
        self.usespeedButton.clicked.connect(self.show_usespeed)
        self.floatspeedButton.clicked.connect(self.show_floatspeed)
        self.resetviewButton.clicked.connect(self.reset_view)
        
    def accept(self):
        
        super().accept()

    def compute_speed(self):
        if self.stackedWidget.currentWidget() == self.usespeedPage :
            self.angles, (self.slidingspeed_usespeed_camepatin, self.slidingspeed_usespeed_valvepatin) = self.controller.compute_slidingspeed(
                speed = float(self.usespeedEdit.text()) *unit.RPM_TO_RADPSEC,
                contact=None
            )
            
            self.update_usespeed_curves()

        elif self.stackedWidget.currentWidget() == self.floatspeedPage:
            self.angles, (self.slidingspeed_floatspeed_camepatin, self.slidingspeed_floatspeed_valvepatin) = self.controller.compute_slidingspeed(
                speed = float(self.floatspeedEdit.text()) *unit.RPM_TO_RADPSEC,
                contact=None
            )
            
            self.update_floatspeed_curves()

    def reset_view(self):
        self.usespeedPlotWidget.setXRange(*self.x_range)
        self.floatspeedPlotWidget.setXRange(*self.x_range)

        self.usespeedPlotWidget.setYRange(*self.y_range)
        self.floatspeedPlotWidget.setYRange(*self.y_range)

    def update_usespeed_curves(self):
        self.contact1_usespeedCurve.setData(self.angles /unit.DEGREE_TO_RADIAN, self.slidingspeed_usespeed_camepatin /unit.MEGAPASCAL_TO_PASCAL)
        self.contact2_usespeedCurve.setData(self.angles /unit.DEGREE_TO_RADIAN, self.slidingspeed_usespeed_soupapepatin /unit.MEGAPASCAL_TO_PASCAL)

        if self.contactComboBox.currentText == "Came/Patin":
                self.contact1_usespeedCurve.show()
                self.contact2_usespeedCurve.hide()

        elif self.contactComboBox.currentText == "Soupape/Patin":
            self.contact1_usespeedCurve.hide()
            self.contact2_usespeedCurve.show()
        
        self.floatspeedPlotWidget.autoRange()

    def update_floatspeed_curves(self):
        self.contact1_floatspeedCurve.setData(self.angles /unit.DEGREE_TO_RADIAN, self.slidingspeed_floatspeed_camepatin /unit.MEGAPASCAL_TO_PASCAL)
        self.contact2_floatspeedCurve.setData(self.angles /unit.DEGREE_TO_RADIAN, self.slidingspeed_floatspeed_soupapepatin /unit.MEGAPASCAL_TO_PASCAL)

        if self.contactComboBox.currentText == "Came/Patin":
                self.contact1_floatspeedCurve.show()
                self.contact2_floatspeedCurve.hide()

        elif self.contactComboBox.currentText == "Soupape/Patin":
            self.contact1_floatspeedCurve.hide()
            self.contact2_floatspeedCurve.show()
        
        self.floatspeedPlotWidget.autoRange()

    def change_display_graph(self, text):
        if text == "Came/Patin":
            self.contact1_usespeedCurve.show()
            self.contact2_usespeedCurve.hide()
            self.contact1_floatspeedCurve.show()
            self.contact2_floatspeedCurve.hide()

        elif text == "Soupape/Patin":
            self.contact1_usespeedCurve.hide()
            self.contact2_usespeedCurve.show()
            self.contact1_floatspeedCurve.hide()
            self.contact2_floatspeedCurve.show()
        
        else :
            self.contact1_usespeedCurve.show()
            self.contact2_usespeedCurve.show()
            self.contact1_floatspeedCurve.show()
            self.contact2_floatspeedCurve.show()
        
        self.usespeedPlotWidget.autoRange()
        self.floatspeedPlotWidget.autoRange()

    def show_usespeed(self):
        self.stackedWidget.setCurrentWidget(self.usespeedPage)
        
    def show_floatspeed(self):
        self.stackedWidget.setCurrentWidget(self.floatspeedPage)
    