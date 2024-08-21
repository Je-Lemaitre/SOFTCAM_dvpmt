import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from PySide6.QtWidgets import QMainWindow, QDialog, QFileDialog

from infrastructure.ui.main_window import Ui_MainWindow
from infrastructure.ui.newstudy_dialog import Ui_NewStudyDialog
from infrastructure.views.assemblyview import RockerArmAssemblyDialog, FlatTappetAssemblyDialog, RollerTappetAssemblyDialog
from infrastructure.views.lawsview import LoisDialog
from infrastructure.views.visuview import VisuDialog
from infrastructure.views.contactposview import ContactPosDialog
from infrastructure.views.slidingspeedview import SlidingSpeedDialog
from infrastructure.views.forceview import ForceDialog
from infrastructure.views.hertzview import HertzDialog
from infrastructure.views.pvview import PVDialog
from infrastructure.views.lubricationview import LubricationDialog
from infrastructure.views.curvatureview import CurvatureDialog
from infrastructure.views.rollerview import RollerDialog
from infrastructure.repositories.json_repository import JSONRepository
from infrastructure.controllers.controller import Controller

class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self, soft_path):
        super(MainView, self).__init__()

        # Initialisation repository et controller
        self.soft_path = soft_path
        study_init_path = os.path.join(self.soft_path, "infrastructure", "data", "rockerarm_study_init.json")
        repository = JSONRepository(study_init_path)
        self.controller = Controller(repository)
        self.study_name = "new_study"
        self.assembly_type = "Linguet / Basculeur"
        self.step_time = 0.001

        # Initialisation of Window
        self.setupUi(self)

        self.newButton.clicked.connect(self.create_study)
        self.openButton.clicked.connect(self.open_study)
        self.saveButton.clicked.connect(self.save_study)
        self.exportButton.clicked.connect(self.export_study)
        self.helpButton.clicked.connect(self.open_documentation)

        self.assemblyButton.clicked.connect(self.open_asmb_dialog)
        self.lawsButton.clicked.connect(self.open_laws_widget)

        self.animationButton.clicked.connect(self.open_visu_dialog)
        self.verificationButton.clicked.connect(self.mechanical_verification)
        self.contactposButton.clicked.connect(self.open_contactpos_dialog)
        self.slidingspeedButton.clicked.connect(self.open_slidingspeed_dialog)
        self.forceButton.clicked.connect(self.open_force_dialog)
        self.hertzButton.clicked.connect(self.open_hertz_dialog)
        self.pvButton.clicked.connect(self.open_pv_dialog)
        self.lubricationButton.clicked.connect(self.open_lubrication_dialog)

        self.curvatureButton.clicked.connect(self.open_curvature_dialog)
        self.rollerButton.clicked.connect(self.open_roller_dialog)
        
    def open_roller_dialog(self):
        roller_dialog = RollerDialog(self.controller)
        roller_dialog.exec()
    def open_curvature_dialog(self):
        curvature_dialog = CurvatureDialog(self.controller)
        curvature_dialog.exec()

    def open_lubrication_dialog(self):
        lubrication_dialog = LubricationDialog(self.controller)
        lubrication_dialog.exec()
    def open_pv_dialog(self):
        pv_dialog = PVDialog(self.controller)
        pv_dialog.exec()
    def open_hertz_dialog(self):
        hertz_dialog = HertzDialog(controller = self.controller)
        hertz_dialog.exec()
    def open_force_dialog(self):
        force_dialog = ForceDialog(self.controller)
        force_dialog.exec()
    def open_slidingspeed_dialog(self):
        slidingspeed_dialog = SlidingSpeedDialog(self.controller)
        slidingspeed_dialog.exec()  
    def open_contactpos_dialog(self):
        contactpos_dialog = ContactPosDialog(self.controller)
        contactpos_dialog.exec()
    def mechanical_verification(self):
        pass
    def open_visu_dialog(self):
        visu_dialog = VisuDialog(controller = self.controller)
        visu_dialog.exec()
    
    def open_laws_widget(self):
        lois_widget = LoisDialog(controller = self.controller)
        lois_widget.exec()
    
    def open_asmb_dialog(self):
        if self.controller.current_study is None :
            raise PermissionError("Veuillez créer une nouvelle étude avant de définir l'assemblage !")
        elif self.controller.current_study.type_assemblage == "Linguet / Basculeur" :
            assembly_dialog = RockerArmAssemblyDialog(controller = self.controller)
        elif self.controller.current_study.type_assemblage == "Attaque Directe" :
            assembly_dialog = RollerTappetAssemblyDialog(controller = self.controller)
        assembly_dialog.exec()

    def create_study(self):
        newstudy_dialog = NewStudyDialog(self)
        newstudy_dialog.exec()
        if self.assembly_type == "Linguet / Basculeur" :
            self.controller.update_study_path(os.path.join(self.soft_path, "infrastructure", "data", "rockerarm_study_init.json"))
        elif self.assembly_type == "Attaque Directe" :
            self.controller.update_study_path(os.path.join(self.soft_path, "infrastructure", "data", "tappet_study_init.json"))
        self.controller.create_study(self.study_name, self.assembly_type, self.step_time)
        self.study_name = self.controller.current_study.nom
    def open_study(self):
        filebrowser_dialog = QFileDialog()
        file = filebrowser_dialog.getOpenFileName(filter = 'JSON Files (*.json)')
        if open_path := file[0]:
            self.controller.update_study_path(open_path)
            self.controller.load_study()
            self.study_name = self.controller.current_study.nom
    def save_study(self):
        filebrowser_dialog = QFileDialog()
        file = filebrowser_dialog.getSaveFileName(dir = f"{self.study_name}.json", filter = 'JSON Files (*.json)')
        if save_path := file[0]:
            self.controller.update_study_path(save_path)
            self.controller.save_study()
    def export_study(self):
        pass
    def open_documentation(self):
        pass

class NewStudyDialog(QDialog, Ui_NewStudyDialog) :
    def __init__(self, parent : MainView = None) :
        super(NewStudyDialog, self).__init__(parent)
        
        self.setupUi(self)

        self.studynameEdit.setText(self.parent().study_name)
        self.assemblytypeComboBox.setCurrentText(self.parent().assembly_type)
        self.steptimeEdit.setText(str(self.parent().step_time))

    def accept(self):
        self.parent().study_name = "_".join(self.studynameEdit.text().split(" "))
        self.parent().assembly_type = self.assemblytypeComboBox.currentText()
        self.parent().step_time = float(self.steptimeEdit.text())
        
        super().accept()