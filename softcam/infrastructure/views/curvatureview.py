import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import numpy as np

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
import pyqtgraph as pg

import domain.services.unitees as unit

from infrastructure.ui.curvature_dialog import Ui_CurvatureDialog
from infrastructure.controllers.controller import Controller


class CurvatureDialog(QDialog, Ui_CurvatureDialog):
    def __init__(self, controller : Controller):
        super(CurvatureDialog, self).__init__()

        self.controller = controller

        self.setupUi(self)

        ## Affichage Complémentaire
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)

        # Intervalles Affichage par Défault
        self.x_range = (0, 200)
        self.y_range = (-200, 200)

        curvature = self.controller.current_study.fabrication.courbure
        try:
            self.curvedata = np.column_stack((
                curvature.rayon_courbure[:,0] /unit.DEGREE_TO_RADIAN,
                curvature.rayon_courbure[:,1] /unit.MILLIMETER_TO_METER
            ))
            self.curvatureCurve.setData(self.curvedata)
        except Exception:
            self.curvedata = None

        self.limitradiusEdit.setText(str(round(curvature.diametre_meule_taillage /unit.MILLIMETER_TO_METER, 3)))

        self.maxradius_line = pg.InfiniteLine(
            pos= -float(self.limitradiusEdit.text()), 
            angle=0, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )

        self.curvaturePlotWidget.addItem(self.maxradius_line)

        self.stackedWidget.setCurrentIndex(0)

        self.computeButton.clicked.connect(self.compute_curvature)
        self.limitradiusEdit.textChanged.connect(self.move_line)
        self.resetviewButton.clicked.connect(self.reset_view)
        
    def accept(self):
        cutting_radius = float(self.limitradiusEdit.text()) *unit.MILLIMETER_TO_METER
        curvature = np.column_stack((
            self.curvedata[:,0] *unit.DEGREE_TO_RADIAN,
            self.curvedata[:,1] *unit.MILLIMETER_TO_METER
        ))
        self.controller.update_curvature(
            cutting_radius = cutting_radius,
            curvature = curvature
        )    
        super().accept()

    def compute_curvature(self):
        curvature = self.controller.compute_curvature()
        self.curvedata = np.column_stack((
            curvature[:,0] /unit.DEGREE_TO_RADIAN, 
            curvature[:,1] /unit.MILLIMETER_TO_METER))
        self.curvatureCurve.setData(self.curvedata)

    def move_line(self, str_pos):
        try :
            self.maxradius_line.setPos(-float(str_pos))

        except ValueError :
            print("Le rayon de meule renseigné n'est pas valide.")

    def reset_view(self):
        self.curvaturePlotWidget.setXRange(*self.x_range)
        self.curvaturePlotWidget.setYRange(*self.y_range)
    