import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
import pyqtgraph as pg

import domain.services.unitees as unit

from infrastructure.ui.hertz_dialog import Ui_HertzDialog
from infrastructure.controllers.controller import Controller


class HertzDialog(QDialog, Ui_HertzDialog):
    def __init__(self, controller : Controller):
        super(HertzDialog, self).__init__()

        self.controller = controller

        self.setupUi(self)

        ## Affichage Complémentaire
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)

        # Intervalles Affichage par Défault
        self.angle_range = (0, 200)
        self.pressure_range = (0, 1500)
        
        self.angle_evalpts = None
        self.hertz_static_camepatin = None
        self.hertz_static_soupapepatin = None
        self.hertz_usespeed_camepatin = None
        self.hertz_usespeed_soupapepatin = None
        self.hertz_floatspeed_camepatin = None
        self.hertz_floatspeed_soupapepatin = None

        self.floatspeedEdit.setText(str(round(float(self.controller.current_study.loiscame.demilois_ouverture.regime_affolement_opt) /unit.RPM_TO_RADPSEC, 3)))
        self.usespeedEdit.setText("7500")
        self.limitpressureEdit.setText("850") 
        
        self.maxpressure_static_line = pg.InfiniteLine(
            pos= float(self.limitpressureEdit.text()), 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        self.maxpressure_usespeed_line = pg.InfiniteLine(
            pos= float(self.limitpressureEdit.text()), 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        self.maxpressure_floatspeed_line = pg.InfiniteLine(
            pos= float(self.limitpressureEdit.text()), 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        
        self.staticPlotWidget.addItem(self.maxpressure_static_line)
        self.usespeedPlotWidget.addItem(self.maxpressure_usespeed_line)
        self.floatspeedPlotWidget.addItem(self.maxpressure_floatspeed_line)
        self.stackedWidget.setCurrentIndex(0)
        
        self.contactComboBox.currentTextChanged.connect(self.change_display_graph)

        self.computeButton.clicked.connect(self.compute_pressure)
        self.staticButton.clicked.connect(self.show_static)
        self.usespeedButton.clicked.connect(self.show_usespeed)
        self.floatspeedButton.clicked.connect(self.show_floatspeed)
        self.resetviewButton.clicked.connect(self.reset_view)
        
    def accept(self):
        
        super().accept()

    def compute_pressure(self):
        if self.stackedWidget.currentIndex() == 0 :
            self.angle_evalpts, (self.hertz_static_camepatin, self.hertz_static_soupapepatin) = self.controller.compute_hertz_pressure(speed = 0, contact = None)
            self.update_static_curves()

        elif self.stackedWidget.currentIndex() == 1 :
            self.angle_evalpts, (self.hertz_usespeed_camepatin, self.hertz_usespeed_soupapepatin) = self.controller.compute_hertz_pressure(
                speed = float(self.usespeedEdit.text()) *unit.RPM_TO_RADPSEC,
                contact=None
                )
            self.update_usespeed_curves()
            
        elif self.stackedWidget.currentIndex() == 2 :
            self.angle_evalpts, (self.hertz_floatspeed_camepatin, self.hertz_floatspeed_soupapepatin) = self.controller.compute_hertz_pressure(
                speed = float(self.floatspeedEdit.text()) *unit.RPM_TO_RADPSEC,
                contact=None
                )
            self.update_floatspeed_curves()


    def reset_view(self):
        self.staticPlotWidget.setXRange(*self.angle_range)
        self.usespeedPlotWidget.setXRange(*self.angle_range)
        self.floatspeedPlotWidget.setXRange(*self.angle_range)

        self.staticPlotWidget.setYRange(*self.pressure_range)
        self.usespeedPlotWidget.setYRange(*self.pressure_range)
        self.floatspeedPlotWidget.setYRange(*self.pressure_range)

    def update_static_curves(self):
        self.contact1_staticCurve.setData(self.angle_evalpts /unit.DEGREE_TO_RADIAN, self.hertz_static_camepatin /unit.MEGAPASCAL_TO_PASCAL)
        self.contact2_staticCurve.setData(self.angle_evalpts /unit.DEGREE_TO_RADIAN, self.hertz_static_soupapepatin /unit.MEGAPASCAL_TO_PASCAL)

        if self.contactComboBox.currentText() == "Came/Patin":
            self.contact1_staticCurve.show()
            self.contact2_staticCurve.hide()

        elif self.contactComboBox.currentText() == "Soupape/Patin":
            self.contact1_staticCurve.hide()
            self.contact2_staticCurve.show()
        
        self.floatspeedPlotWidget.autoRange()

    def update_usespeed_curves(self):
        self.contact1_usespeedCurve.setData(self.angle_evalpts /unit.DEGREE_TO_RADIAN, self.hertz_usespeed_camepatin /unit.MEGAPASCAL_TO_PASCAL)
        self.contact2_usespeedCurve.setData(self.angle_evalpts /unit.DEGREE_TO_RADIAN, self.hertz_usespeed_soupapepatin /unit.MEGAPASCAL_TO_PASCAL)

        if self.contactComboBox.currentText == "Came/Patin":
                self.contact1_usespeedCurve.show()
                self.contact2_usespeedCurve.hide()

        elif self.contactComboBox.currentText == "Soupape/Patin":
            self.contact1_usespeedCurve.hide()
            self.contact2_usespeedCurve.show()
        
        self.floatspeedPlotWidget.autoRange()

    def update_floatspeed_curves(self):
        self.contact1_floatspeedCurve.setData(self.angle_evalpts /unit.DEGREE_TO_RADIAN, self.hertz_floatspeed_camepatin /unit.MEGAPASCAL_TO_PASCAL)
        self.contact2_floatspeedCurve.setData(self.angle_evalpts /unit.DEGREE_TO_RADIAN, self.hertz_floatspeed_soupapepatin /unit.MEGAPASCAL_TO_PASCAL)

        if self.contactComboBox.currentText == "Came/Patin":
                self.contact1_floatspeedCurve.show()
                self.contact2_floatspeedCurve.hide()

        elif self.contactComboBox.currentText == "Soupape/Patin":
            self.contact1_floatspeedCurve.hide()
            self.contact2_floatspeedCurve.show()
        
        self.floatspeedPlotWidget.autoRange()

    def change_display_graph(self, text):
        if text == "Came/Patin":
            self.contact1_staticCurve.show()
            self.contact2_staticCurve.hide()
            self.contact1_usespeedCurve.show()
            self.contact2_usespeedCurve.hide()
            self.contact1_floatspeedCurve.show()
            self.contact2_floatspeedCurve.hide()

        elif text == "Soupape/Patin":
            self.contact1_staticCurve.hide()
            self.contact2_staticCurve.show()
            self.contact1_usespeedCurve.hide()
            self.contact2_usespeedCurve.show()
            self.contact1_floatspeedCurve.hide()
            self.contact2_floatspeedCurve.show()
        
        else :
            self.contact1_staticCurve.show()
            self.contact2_staticCurve.show()
            self.contact1_usespeedCurve.show()
            self.contact2_usespeedCurve.show()
            self.contact1_floatspeedCurve.show()
            self.contact2_floatspeedCurve.show()
        
        self.usespeedPlotWidget.autoRange()
        self.floatspeedPlotWidget.autoRange()

    def show_static(self): 
        self.stackedWidget.setCurrentWidget(self.staticPage)
        
    def show_usespeed(self):
        self.stackedWidget.setCurrentWidget(self.usespeedPage)
        
    def show_floatspeed(self):
        self.stackedWidget.setCurrentWidget(self.floatspeedPage)
    