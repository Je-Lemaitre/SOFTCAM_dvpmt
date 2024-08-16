# This Python file uses the following encoding: utf-8
import sys
sys.path.append("c:/Users/stagiaire.be/Documents/SOFTCAM_dvpmt/softcam")
import os

from PySide6.QtWidgets import QApplication
from infrastructure.views.mainview import MainView

if __name__ == "__main__":
    main_path = os.path.realpath(__file__)
    soft_path = os.path.dirname(main_path)
    sys.path.append(soft_path)

    app = QApplication(sys.argv)
    window = MainView(soft_path = soft_path)
    window.show()
    sys.exit(app.exec())



