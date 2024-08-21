import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import numpy as np

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt

import domain.services.unitees as unit
from infrastructure.ui.visu_dialog import Ui_VisuDialog
from infrastructure.controllers.controller import Controller


class VisuDialog(QDialog, Ui_VisuDialog):
    def __init__(self, controller : Controller):
        super(VisuDialog, self).__init__()

        self.controller = controller

        self.setupUi(self)

        ## Affichage Complémentaire
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)

        # Intervalles Affichage par Défault
        self.plot_angles = np.arange(0, 200, 0.1)
        self.angle_range = (0, 180)
        self.profile_range = (-40, 40)
        self.curvature_range = (-350, 350)
        self.kinematics_range = (0, 12)
        
        self.basecircle_profile = np.array([[np.cos(i/1000), np.sin(i/1000)] for i in range(int(2*np.pi*1000)+1)]) *self.controller.current_study.assemblage.came.rayon_base /unit.MILLIMETER_TO_METER

        self.cartesian_profile = None
        self.curvature = None

        self.basecircleCurve.setData(self.basecircle_profile[:,0], self.basecircle_profile[:,1])
        
        self.displayButton.clicked.connect(self.display_graph)
        self.profileButton.clicked.connect(self.show_profile)
        self.curvatureButton.clicked.connect(self.show_curvature)
        self.kinematicsButton.clicked.connect(self.show_kinematics)
        self.resetviewButton.clicked.connect(self.reset_view)
        
    
    def display_graph(self):
        precision = float(self.precisionEdit.text()) *unit.DEGREE_TO_RADIAN
        cartesian_profile = self.controller.compute_profile()
        self.cartesian_profile = cartesian_profile /unit.MILLIMETER_TO_METER
        self.profileCurve.setData(self.cartesian_profile[:,1], self.cartesian_profile[:,2])

        if self.stackedWidget.currentIndex() == 1: # Rayon de Courbure
            curvature = self.controller.compute_curvature()
            self.curvature = np.column_stack((curvature[:,0] /unit.DEGREE_TO_RADIAN, curvature[:,1] /unit.MILLIMETER_TO_METER))
            self.curvatureCurve.setData(self.curvature[:,0], self.curvature[:,1])

    def reset_view(self):
        self.profilePlotWidget.setXRange(*self.angle_range)
        self.curvaturePlotWidget.setXRange(*self.angle_range)
        self.kinematicsPlotWidget.setXRange(*self.angle_range)

        self.profilePlotWidget.setYRange(*self.profile_range)
        self.curvaturePlotWidget.setYRange(*self.curvature_range)
        self.kinematicsPlotWidget.setYRange(*self.kinematics_range)

    def show_profile(self): 
        self.stackedWidget.setCurrentWidget(self.profilePage)
        
    def show_curvature(self):
        self.stackedWidget.setCurrentWidget(self.curvaturePage)

    def show_kinematics(self):
        self.stackedWidget.setCurrentWidget(self.kinematicsPage)

    