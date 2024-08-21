import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from PySide6.QtWidgets import QApplication

from infrastructure.views.mainview import MainView

if __name__ == "__main__":
    main_path = os.path.realpath(__file__)
    soft_path = os.path.dirname(main_path) #Chemin absolu dossier contenant l'application
    sys.path.append(soft_path) #Ajoute le chemin au path pour que l'ordinateur puisse automatique chercher des dossier à l'intérieur.

    app = QApplication(sys.argv) #Création de l'application.
    window = MainView(soft_path = soft_path) #Création de la page principale.
    window.show() #Affichage de la page d'accueil.
    sys.exit(app.exec()) #Commande pour que l'application s'exécute.



