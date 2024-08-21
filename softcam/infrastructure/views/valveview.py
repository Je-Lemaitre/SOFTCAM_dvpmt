import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from PySide6.QtWidgets import QDialog

import domain.services.unitees as unit

from infrastructure.ui.valve_dialog import Ui_SoupapeDialog
from infrastructure.controllers.controller import Controller

class SoupapeDialog(QDialog, Ui_SoupapeDialog):
    def __init__(self, controller : Controller):
        super(SoupapeDialog, self).__init__()

        self.controller = controller
        self.valve = controller.current_study.assemblage.soupape

        self.setupUi(self)

        self.msoupEdit.setText(str(round(self.valve.masse_soupape /unit.GRAMM_TO_KILOGRAMM, 3)))
        self.mcoupelleEdit.setText(str(round(self.valve.masse_coupelle /unit.GRAMM_TO_KILOGRAMM, 3)))
        self.dsoupEdit.setText(str(round(self.valve.diametre_soupape /unit.MILLIMETER_TO_METER, 3)))
        self.youngEdit.setText(str(round(self.valve.module_young /unit.GIGAPASCAL_TO_PASCAL, 3)))
        self.poissonEdit.setText(str(self.valve.coefficient_poisson))

    def accept(self):
        masse_soupape = float(self.msoupEdit.text()) *unit.GRAMM_TO_KILOGRAMM
        masse_coupelle = float(self.mcoupelleEdit.text()) *unit.GRAMM_TO_KILOGRAMM
        diametre_soupape = float(self.dsoupEdit.text()) *unit.MILLIMETER_TO_METER 
        module_young = float(self.youngEdit.text()) *unit.GIGAPASCAL_TO_PASCAL
        coefficient_poisson = float(self.poissonEdit.text())

        self.controller.update_valve(
            masse_soupape=masse_soupape,
            masse_coupelle=masse_coupelle,
            diametre_soupape=diametre_soupape,
            poussoir=None,
            module_young=module_young,
            coefficient_poisson=coefficient_poisson
        )

        super().accept()