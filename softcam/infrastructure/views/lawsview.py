# This Python file uses the following encoding: utf-8
import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")
import numpy as np

from PySide6.QtWidgets import QDialog, QInputDialog
from PySide6.QtCore import Qt
import pyqtgraph as pg

import domain.services.unitees as unit
from infrastructure.ui.laws_dialog import Ui_LoisDialog, Ui_PointDialog
from infrastructure.controllers.controller import Controller

class PointDialog(QDialog, Ui_PointDialog):
    def __init__(self, point, weight = 1, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modification du Squelette")
        self.point = point
        self.weight = weight
        self.setupUi(self)
    
    def get_coordinates(self):
        return float(self.x_input.text()), float(self.y_input.text()), float(self.z_input.text())

class LoisDialog(QDialog, Ui_LoisDialog):
    def __init__(self, controller : Controller):
        super(LoisDialog, self).__init__()

        self.controller = controller
        self.laws = controller.current_laws
        self.opening = self.laws.demilois_ouverture
        self.closing = self.laws.demilois_fermeture

        self.setupUi(self)

        ## Affichage Complémentaire
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)

        self.openaccel_skeleton, self.closeaccel_skeleton = self.init_accel()
        self.openspeed_skeleton, self.closespeed_skeleton = self.init_speed()
        self.openlift_skeleton, self.closelift_skeleton = self.init_lift()

        self.angles = None
        self.accel = None
        self.speed = None
        self.lift = None
        self.effective_angles = None
        self.effective_accel = None
        self.effective_speed = None
        self.effective_lift = None

        # Intervalles Affichage par Défault
        self.angle_range = (0, 200)
        self.accel_range = (-10, 40)
        self.speed_range = (-350, 350)
        self.lift_range = (0, 12)

        self.symmetryCheckBox.setChecked(self.laws.symetrie)
        self.floatspeedEdit.setText(str(round(self.opening.regime_affolement_opt /unit.RPM_TO_RADPSEC, 3)))
        self.accelmaxEdit.setText(str(round(self.opening.accelmax_opt /unit.MICROMETER_TO_METER *unit.DEGREE_TO_RADIAN**2, 3)))
        self.clearanceEdit.setText(str(round(self.controller.current_study.assemblage.jeu /unit.MILLIMETER_TO_METER, 6)))

        self.openjoin_line = pg.InfiniteLine(
            pos=self.opening.ac_raccord /unit.DEGREE_TO_RADIAN, 
            angle=90, 
            movable=True,
            pen = pg.mkPen(color='r', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        self.closejoin_line = pg.InfiniteLine(
            pos= (self.laws.dac_leveemax_ouverture + self.laws.dac_leveemax_fermeture - self.closing.ac_raccord) /unit.DEGREE_TO_RADIAN, 
            angle=90, 
            movable=True,
            pen = pg.mkPen(color='g', style=pg.QtCore.Qt.DashLine, width=2) 
            )
        self.accelPlotWidget.addItem(self.openjoin_line)
        self.accelPlotWidget.addItem(self.closejoin_line)

        self.plot_skeleton()

        self.accelButton.clicked.connect(self.show_accel)
        self.speedButton.clicked.connect(self.show_speed)
        self.liftButton.clicked.connect(self.show_lift)
        self.optimisationButton.clicked.connect(self.optimise_laws)
        self.resetviewButton.clicked.connect(self.reset_view)
        
        self.openjoin_line.sigClicked.connect(self.modify_joinline)
        self.closejoin_line.sigClicked.connect(self.modify_joinline)
        self.openaccelScatterPlot.sigClicked.connect(self.modify_openaccel)
        self.openspeedScatterPlot.sigClicked.connect(self.modify_openspeed)
        self.openliftScatterPlot.sigClicked.connect(self.modify_openlift)
        self.closeaccelScatterPlot.sigClicked.connect(self.modify_closeaccel)
        self.closespeedScatterPlot.sigClicked.connect(self.modify_closespeed)
        self.closeliftScatterPlot.sigClicked.connect(self.modify_closelift)

    
    def accept(self):
        self.controller.update_laws()
        super().accept()

    def optimise_laws(self):
        is_symmetrical = self.symmetryCheckBox.isChecked()
        valve_float_speed = float(self.floatspeedEdit.text()) *unit.RPM_TO_RADPSEC
        
        accel_skeleton_units = np.array([unit.DEGREE_TO_RADIAN, unit.MICROMETER_TO_METER /unit.DEGREE_TO_RADIAN**2, 1])
        openaccel_skl = np.einsum( "ij, j -> ij", self.openaccel_skeleton, accel_skeleton_units)
        closeaccel_skl = np.einsum( "ij, j -> ij", self.closeaccel_skeleton, accel_skeleton_units)
        
        speed_skeleton_units = np.array([unit.DEGREE_TO_RADIAN, unit.MICROMETER_TO_METER /unit.DEGREE_TO_RADIAN])
        openspeed_skl = np.einsum( "ij, j -> ij", self.openspeed_skeleton, speed_skeleton_units)
        closespeed_skl = np.einsum( "ij, j -> ij", self.closespeed_skeleton, speed_skeleton_units)

        lift_skeleton_units = np.array([unit.DEGREE_TO_RADIAN, unit.MILLIMETER_TO_METER])
        openlift_skl = np.einsum( "ij, j -> ij", self.openlift_skeleton, lift_skeleton_units)
        closelift_skl = np.einsum( "ij, j -> ij", self.closelift_skeleton, lift_skeleton_units)
        
        openjoin_angle = self.openjoin_line.pos().x() *unit.DEGREE_TO_RADIAN
        closejoin_angle = self.closejoin_line.pos().x() *unit.DEGREE_TO_RADIAN

        self.angles, self.accel, self.speed, self.lift = self.controller.optimise_laws(
            symmetry = is_symmetrical, 
            valve_float_speed = valve_float_speed,
            openaccel_skl_raw = openaccel_skl,
            closeaccel_skl_raw = closeaccel_skl,
            openspeed_skl_raw = openspeed_skl,
            closespeed_skl_raw = closespeed_skl,
            openlift_skl_raw = openlift_skl,
            closelift_skl_raw = closelift_skl,
            openjoin_angle_raw = openjoin_angle,
            closejoin_angle_raw = closejoin_angle
        )
        self.laws = self.controller.current_laws

        self.floatspeedEdit.setText(str(round(self.laws.demilois_ouverture.regime_affolement_opt /unit.RPM_TO_RADPSEC, 3)))
        self.accelmaxEdit.setText(str(round(self.laws.demilois_ouverture.accelmax_opt /unit.MICROMETER_TO_METER *unit.DEGREE_TO_RADIAN**2, 3)))

        clearance = float(self.clearanceEdit.text()) *unit.MILLIMETER_TO_METER
        
        self.effective_angles, self.effective_accel, self.effective_speed, self.effective_lift = self.controller.compute_effective_laws(clearance)

        self.plot_optimised_curves()

        self.update_performances(clearance)
    
    def update_performances(self, clearance):
        opening = self.controller.compute_opening(clearance) /unit.DEGREE_TO_RADIAN
        area = self.controller.compute_area(clearance) /unit.MILLIMETER_TO_METER /unit.DEGREE_TO_RADIAN
        efficiency = self.controller.compute_efficiency(clearance) *100

        self.openingEdit.setText(str(round(opening, 3)))
        self.areaEdit.setText(str(round(area, 3)))
        self.efficiencyEdit.setText(str(round(efficiency, 3)))

    def modify_openaccel(self, plot, points):
        point = points[0]
        index = np.where(np.all(self.openaccel_skeleton[:, :2] == np.array([point.pos().x(), point.pos().y()]), axis=1))
        weight = self.openaccel_skeleton[index, 2][0,0]
        dialog = PointDialog(point, weight)
        if dialog.exec() == QDialog.Accepted:
            new_x, new_y, new_z = dialog.get_coordinates()
            self.openaccel_skeleton[index] = np.array([new_x, new_y, new_z])
            self.plot_skeleton()

    def modify_closeaccel(self, plot, points):
        point = points[0]
        index = np.where(np.all(self.closeaccel_skeleton[:, :2] == np.array([point.pos().x(), point.pos().y()]), axis=1))
        weight = self.closeaccel_skeleton[index, 2]
        dialog = PointDialog(point, weight)
        if dialog.exec() == QDialog.Accepted:
            new_x, new_y, new_z = dialog.get_coordinates()
            self.closeaccel_skeleton[index] = np.array[new_x, new_y, new_z]
            self.plot_skeleton()

    def modify_openspeed(self, plot, points):
        point = points[0]
        index = np.where(np.all(self.openspeed_skeleton == np.array([point.pos().x(), point.pos().y()]), axis=1))
        dialog = PointDialog(point)
        if dialog.exec() == QDialog.Accepted:
            new_x, new_y, new_z = dialog.get_coordinates()
            self.openspeed_skeleton[index] = np.array([new_x, new_y])
            self.plot_skeleton()

    def modify_closespeed(self, plot, points):
        point = points[0]
        index = np.where(np.all(self.closespeed_skeleton == np.array([point.pos().x(), point.pos().y()]), axis=1))
        dialog = PointDialog(point)
        if dialog.exec() == QDialog.Accepted:
            new_x, new_y, new_z = dialog.get_coordinates()
            self.closespeed_skeleton[index] = np.array([new_x, new_y])
            self.plot_skeleton()

    def modify_openlift(self, plot, points):
        point = points[0]
        index = np.where(np.all(self.openlift_skeleton == np.array([point.pos().x(), point.pos().y()]), axis=1))
        dialog = PointDialog(point)
        if dialog.exec() == QDialog.Accepted:
            new_x, new_y, new_z = dialog.get_coordinates()
            self.openlift_skeleton[index] = np.array([new_x, new_y])
            self.plot_skeleton()
    
    def modify_closelift(self, plot, points):
        point = points[0]
        index = np.where(np.all(self.closelift_skeleton == np.array([point.pos().x(), point.pos().y()]), axis=1))
        dialog = PointDialog(point)
        if dialog.exec() == QDialog.Accepted:
            new_x, new_y, new_z = dialog.get_coordinates()
            self.closelift_skeleton[index] = np.array([new_x, new_y])
            self.plot_skeleton()

    def modify_joinline(self, line):
        # Prompt the user for a new x position
        new_x, ok = QInputDialog.getDouble(self, "Move Line", "Enter new x position:", line.pos().x())
        if ok:
            # Move the line to the new position
            line.setPos(new_x)

    def plot_optimised_curves(self):
        self.accelCurve.setData(self.angles /unit.DEGREE_TO_RADIAN, self.accel /unit.MICROMETER_TO_METER *unit.DEGREE_TO_RADIAN**2)
        self.speedCurve.setData(self.angles /unit.DEGREE_TO_RADIAN, self.speed /unit.MICROMETER_TO_METER *unit.DEGREE_TO_RADIAN)
        self.liftCurve.setData(self.angles /unit.DEGREE_TO_RADIAN, self.lift /unit.MILLIMETER_TO_METER)

        self.effaccelCurve.setData(self.effective_angles /unit.DEGREE_TO_RADIAN, self.effective_accel /unit.MICROMETER_TO_METER *unit.DEGREE_TO_RADIAN**2)
        self.effspeedCurve.setData(self.effective_angles /unit.DEGREE_TO_RADIAN, self.effective_speed /unit.MICROMETER_TO_METER *unit.DEGREE_TO_RADIAN)
        self.effliftCurve.setData(self.effective_angles /unit.DEGREE_TO_RADIAN, self.effective_lift /unit.MILLIMETER_TO_METER)
    
    def plot_skeleton(self):
        self.plot_skeleton_scatters()
        self.plot_skeleton_curves()

    def plot_skeleton_scatters(self):
        
        self.openaccelScatterPlot.setData(
            self.openaccel_skeleton[:, 0], 
            self.openaccel_skeleton[:, 1]
            )
        
        self.closeaccelScatterPlot.setData(
            self.closeaccel_skeleton[:, 0], 
            self.closeaccel_skeleton[:, 1]
            )
        
        self.openspeedScatterPlot.setData(
            self.openspeed_skeleton[:, 0], 
            self.openspeed_skeleton[:, 1]
            )
        
        self.closespeedScatterPlot.setData(
            self.closespeed_skeleton[:, 0], 
            self.closespeed_skeleton[:, 1]
            )
        
        self.openliftScatterPlot.setData(
            self.openlift_skeleton[:, 0], 
            self.openlift_skeleton[:, 1]
            )
        
        self.closeliftScatterPlot.setData(
            self.closelift_skeleton[:, 0], 
            self.closelift_skeleton[:, 1]
            )
    def plot_skeleton_curves(self):
        self.openaccelCurve.setData(
            self.openaccel_skeleton[:, 0], 
            self.openaccel_skeleton[:, 1]
            )
        
        self.closeaccelCurve.setData(
            self.closeaccel_skeleton[:, 0], 
            self.closeaccel_skeleton[:, 1]
            )
        
        self.openspeedCurve.setData(
            self.openspeed_skeleton[:, 0], 
            self.openspeed_skeleton[:, 1]
            )
        
        self.closespeedCurve.setData(
            self.closespeed_skeleton[:, 0], 
            self.closespeed_skeleton[:, 1]
            )
        
        self.openliftCurve.setData(
            self.openlift_skeleton[:, 0], 
            self.openlift_skeleton[:, 1]
            )
        
        self.closeliftCurve.setData(
            self.closelift_skeleton[:, 0], 
            self.closelift_skeleton[:, 1]
            )
        
    def reset_view(self):
        self.accelPlotWidget.setXRange(*self.angle_range)
        self.speedPlotWidget.setXRange(*self.angle_range)
        self.liftPlotWidget.setXRange(*self.angle_range)

        self.accelPlotWidget.setYRange(*self.accel_range)
        self.speedPlotWidget.setYRange(*self.speed_range)
        self.liftPlotWidget.setYRange(*self.lift_range)

    def show_accel(self): 
        self.stackedWidget.setCurrentWidget(self.accelPage)
        
    def show_speed(self):
        self.stackedWidget.setCurrentWidget(self.speedPage)

    def show_lift(self):
        self.stackedWidget.setCurrentWidget(self.liftPage)

    def init_accel(self):
        openaccel_skeleton = np.round(
            np.column_stack((
                (self.opening.squelette_acceleration[:,0] + self.opening.ac_fin_rampe) /unit.DEGREE_TO_RADIAN, 
                self.opening.squelette_acceleration[:,1] /unit.MICROMETER_TO_METER*unit.DEGREE_TO_RADIAN**2, 
                self.opening.squelette_acceleration[:,2]
                )), 
                3
                )
        
        closeaccel_skeleton = np.round(
            np.column_stack((
                (self.laws.dac_leveemax_ouverture + self.laws.dac_leveemax_fermeture - self.opening.squelette_acceleration[:,0] - self.closing.ac_fin_rampe) /unit.DEGREE_TO_RADIAN, 
                self.closing.squelette_acceleration[:,1] /unit.MICROMETER_TO_METER*unit.DEGREE_TO_RADIAN**2, 
                self.opening.squelette_acceleration[:,2]
                )), 
                3
                )

        return openaccel_skeleton, np.flip(closeaccel_skeleton, axis = 0)
            
    def init_speed(self):
        openspeed_skeleton = np.round(
            np.column_stack((
                (self.opening.squelette_vitesse[:,0]) /unit.DEGREE_TO_RADIAN, 
                self.opening.squelette_vitesse[:,1] /unit.MICROMETER_TO_METER*unit.DEGREE_TO_RADIAN
                )), 
                3
                )
        
        closespeed_skeleton = np.round(
            np.column_stack((
                (self.laws.dac_leveemax_ouverture + self.laws.dac_leveemax_fermeture - self.opening.squelette_vitesse[:,0]) /unit.DEGREE_TO_RADIAN, 
                -self.closing.squelette_vitesse[:,1] /unit.MICROMETER_TO_METER*unit.DEGREE_TO_RADIAN
                )), 
                3
                )

        return openspeed_skeleton, np.flip(closespeed_skeleton, axis = 0)
        
    def init_lift(self):
        openlift_skeleton = np.round(
            np.column_stack((
                (self.opening.squelette_levee[:,0]) /unit.DEGREE_TO_RADIAN, 
                self.opening.squelette_levee[:,1] /unit.MILLIMETER_TO_METER
                )), 
                3
                )
        
        closelift_skeleton = np.round(
            np.column_stack((
                (self.laws.dac_leveemax_ouverture + self.laws.dac_leveemax_fermeture - self.opening.squelette_levee[:,0]) /unit.DEGREE_TO_RADIAN, 
                self.closing.squelette_levee[:,1] /unit.MILLIMETER_TO_METER
                )), 
                3
                )

        return openlift_skeleton, np.flip(closelift_skeleton, axis = 0)

    