# This Python file uses the following encoding: utf-8
import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")
import os

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
import domain.services.unitees as unit
from infrastructure.ui.rockerarm_asmb_dialog import Ui_RockerArmAssemblyDialog
from infrastructure.views.valveview import SoupapeDialog
from infrastructure.views.springview import RessortDialog
from infrastructure.views.camview import CamDialog
from infrastructure.views.rockerarmview import LinguetDialog
import infrastructure.ui.displayutilities as disputil
from infrastructure.controllers.controller import Controller

class RockerArmAssemblyDialog(QDialog, Ui_RockerArmAssemblyDialog):
    def __init__(self, controller : Controller):
        super(RockerArmAssemblyDialog, self).__init__()

        self.controller = controller
        self.assembly = controller.current_study.assemblage

        self.setupUi(self)
        
        ## Affichage Complémentaire
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)

        ylMathLabel = disputil.create_latex(r"$y_{\!_{L}}$", scale = 1)
        self.ylLayout.insertWidget(0, ylMathLabel)
        zlMathLabel = disputil.create_latex(r"$z_{\!_{L}}$", scale = 1)
        self.zlLayout.insertWidget(0, zlMathLabel)
        ycMathLabel = disputil.create_latex(r"$y_{\!_{C}}$", scale = 1)
        self.ycLayout.insertWidget(0, ycMathLabel)
        zcMathLabel = disputil.create_latex(r"$z_{\!_{C}}$", scale = 1)
        self.zcLayout.insertWidget(0, zcMathLabel)
        gammaMathLabel = disputil.create_latex(r"$\gamma_{\!_{0}}$", scale = 1)
        self.gammaLayout.insertWidget(0, gammaMathLabel)
        alphaMathLabel = disputil.create_latex(r"$\alpha$", scale = 1)
        self.alphaLayout.insertWidget(0, alphaMathLabel)

        infrastructure_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(infrastructure_path)
        scheme_path = os.path.join(infrastructure_path, "ui", "resources", "img", "kinematic_diagram.svg")
        kinematicScheme = disputil.SvgWidget(scheme_path)
        self.kinematicSchemeLayout.addWidget(kinematicScheme)

        ## Laision View/Model
        sensrot = self.assembly.sens_rotation_came
        if sensrot == -1 :
            self.sensrotComboBox.setCurrentText("Horaire")
        else :
            self.sensrotComboBox.setCurrentText("Anti-horaire")
        self.ylEdit.setText(str(round(self.assembly.coords_levier[1] /unit.MILLIMETER_TO_METER, 3)))
        self.zlEdit.setText(str(round(self.assembly.coords_levier[2] /unit.MILLIMETER_TO_METER, 3)))
        self.ycEdit.setText(str(round(self.assembly.coords_came[1] /unit.MILLIMETER_TO_METER, 3)))
        self.zcEdit.setText(str(round(self.assembly.coords_came[2] /unit.MILLIMETER_TO_METER, 3)))
        self.gammaEdit.setText(str(round(self.assembly.angle_leviercame_init /unit.DEGREE_TO_RADIAN, 3)))
        self.alphaEdit.setText(str(round(self.assembly.inclinaison_soupape /unit.DEGREE_TO_RADIAN, 3)))
        
        self.valveButton.clicked.connect(self.open_valve_dialog)
        self.springButton.clicked.connect(self.open_spring_dialog)
        self.rockerarmButton.clicked.connect(self.open_rockerarm_dialog)
        self.camButton.clicked.connect(self.open_cam_dialog)
    
    def accept(self):
        sensrot = self.sensrotComboBox.currentText()
        if sensrot == "Horaire" :
            sens_rotation_came = -1
        else :
            sens_rotation_came = 1
        coords_levier = [0.0, float(self.ylEdit.text()) *unit.MILLIMETER_TO_METER, float(self.zlEdit.text()) *unit.MILLIMETER_TO_METER]
        coords_came = [0.0, float(self.ycEdit.text()) *unit.MILLIMETER_TO_METER, float(self.zcEdit.text()) *unit.MILLIMETER_TO_METER]
        angle_leviercame_init = float(self.gammaEdit.text()) *unit.DEGREE_TO_RADIAN
        inclinaison_soupape = float(self.alphaEdit.text()) *unit.DEGREE_TO_RADIAN

        self.controller.update_rockerarmassembly(
            sens_rotation_came = sens_rotation_came, 
            coords_levier = coords_levier, 
            coords_came = coords_came, 
            angle_leviercame_init = angle_leviercame_init, 
            inclinaison_soupape = inclinaison_soupape
            )

        super().accept()

    def open_valve_dialog(self):
        soupape_dialog = SoupapeDialog(controller = self.controller)
        soupape_dialog.exec()

    def open_spring_dialog(self):
        ressort_dialog = RessortDialog(controller = self.controller)
        ressort_dialog.exec()

    def open_rockerarm_dialog(self):
        linguet_dialog = LinguetDialog(controller = self.controller)
        linguet_dialog.exec()
    
    def open_cam_dialog(self):
        cam_dialog = CamDialog(controller = self.controller)
        cam_dialog.exec()

class FlatTappetAssemblyDialog(QDialog):
    def __init__(self, controller : Controller):
        super(FlatTappetAssemblyDialog, self).__init__()
        self.controller = controller
        self.assembly = controller.current_study.assemblage

class RollerTappetAssemblyDialog(QDialog):
    def __init__(self, controller : Controller):
        super(RollerTappetAssemblyDialog, self).__init__()
        self.controller = controller
        self.assembly = controller.current_study.assemblage