# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 705)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/icons/oreca-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionOpenCameDialog = QAction(MainWindow)
        self.actionOpenCameDialog.setObjectName(u"actionOpenCameDialog")
        self.actionOpenCameDialog.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenuContainer = QFrame(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setAutoFillBackground(False)
        self.leftMenuContainer.setStyleSheet(u"background-color: rgb(17, 48, 83);")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.homeButton = QPushButton(self.leftMenuContainer)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setStyleSheet(u"background-color: rgb(17, 48, 83);")
        icon1 = QIcon()
        iconThemeName = u"applications-science"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u":/icons/icons/oreca-logo_star.png", QSize(), QIcon.Normal, QIcon.Off)

        self.homeButton.setIcon(icon1)
        self.homeButton.setIconSize(QSize(40, 40))

        self.verticalLayout.addWidget(self.homeButton)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.newButton = QPushButton(self.leftMenuContainer)
        self.newButton.setObjectName(u"newButton")
        self.newButton.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/plus-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newButton.setIcon(icon2)
        self.newButton.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.newButton)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.openButton = QPushButton(self.leftMenuContainer)
        self.openButton.setObjectName(u"openButton")
        self.openButton.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/folder-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.openButton.setIcon(icon3)
        self.openButton.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.openButton)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.saveButton = QPushButton(self.leftMenuContainer)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/save-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon4)
        self.saveButton.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.saveButton)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.exportButton = QPushButton(self.leftMenuContainer)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/table-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exportButton.setIcon(icon5)
        self.exportButton.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.exportButton)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.helpButton = QPushButton(self.leftMenuContainer)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setStyleSheet(u"background-color: rgb(223, 223, 223);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/info-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpButton.setIcon(icon6)
        self.helpButton.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.helpButton)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.mainContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lawsDefinitionContainer = QFrame(self.mainContainer)
        self.lawsDefinitionContainer.setObjectName(u"lawsDefinitionContainer")
        self.lawsDefinitionContainer.setStyleSheet(u"border-color: rgb(17, 48, 83);\n"
"background-color: rgb(223, 223, 223);")
        self.lawsDefinitionContainer.setFrameShape(QFrame.StyledPanel)
        self.lawsDefinitionContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.lawsDefinitionContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lawsDefinitionLabel = QLabel(self.lawsDefinitionContainer)
        self.lawsDefinitionLabel.setObjectName(u"lawsDefinitionLabel")
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(True)
        self.lawsDefinitionLabel.setFont(font)

        self.verticalLayout_6.addWidget(self.lawsDefinitionLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.lawsDefinitionSubContainer = QWidget(self.lawsDefinitionContainer)
        self.lawsDefinitionSubContainer.setObjectName(u"lawsDefinitionSubContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.lawsDefinitionSubContainer.sizePolicy().hasHeightForWidth())
        self.lawsDefinitionSubContainer.setSizePolicy(sizePolicy2)
        self.gridLayout_7 = QGridLayout(self.lawsDefinitionSubContainer)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_3 = QPushButton(self.lawsDefinitionSubContainer)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.pushButton_3, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.lawsDefinitionSubContainer)


        self.gridLayout.addWidget(self.lawsDefinitionContainer, 0, 1, 1, 1)

        self.systemDefinitionFrame = QFrame(self.mainContainer)
        self.systemDefinitionFrame.setObjectName(u"systemDefinitionFrame")
        self.systemDefinitionFrame.setStyleSheet(u"border-color: rgb(17, 48, 83);\n"
"background-color: rgb(223, 223, 223);")
        self.systemDefinitionFrame.setFrameShape(QFrame.StyledPanel)
        self.systemDefinitionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.systemDefinitionFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.systemDefinitionLabel = QLabel(self.systemDefinitionFrame)
        self.systemDefinitionLabel.setObjectName(u"systemDefinitionLabel")
        self.systemDefinitionLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.systemDefinitionLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.partsSubContainer = QWidget(self.systemDefinitionFrame)
        self.partsSubContainer.setObjectName(u"partsSubContainer")
        sizePolicy2.setHeightForWidth(self.partsSubContainer.sizePolicy().hasHeightForWidth())
        self.partsSubContainer.setSizePolicy(sizePolicy2)
        self.gridLayout_2 = QGridLayout(self.partsSubContainer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.valveButton = QPushButton(self.partsSubContainer)
        self.valveButton.setObjectName(u"valveButton")
        self.valveButton.setFont(font1)
        self.valveButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.valveButton, 0, 0, 1, 1)

        self.springButton = QPushButton(self.partsSubContainer)
        self.springButton.setObjectName(u"springButton")
        self.springButton.setFont(font1)
        self.springButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.springButton, 0, 1, 1, 1)

        self.camButton = QPushButton(self.partsSubContainer)
        self.camButton.setObjectName(u"camButton")
        self.camButton.setFont(font1)
        self.camButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.camButton, 1, 0, 1, 1)

        self.rockerArmButton = QPushButton(self.partsSubContainer)
        self.rockerArmButton.setObjectName(u"rockerArmButton")
        self.rockerArmButton.setFont(font1)
        self.rockerArmButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.rockerArmButton, 1, 1, 1, 1)

        self.assemblyButton = QPushButton(self.partsSubContainer)
        self.assemblyButton.setObjectName(u"assemblyButton")
        self.assemblyButton.setFont(font1)
        self.assemblyButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.assemblyButton, 2, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.partsSubContainer)


        self.gridLayout.addWidget(self.systemDefinitionFrame, 0, 0, 1, 1)

        self.mecanicContainer = QFrame(self.mainContainer)
        self.mecanicContainer.setObjectName(u"mecanicContainer")
        self.mecanicContainer.setStyleSheet(u"border-color: rgb(17, 48, 83);\n"
"background-color: rgb(223, 223, 223);")
        self.mecanicContainer.setFrameShape(QFrame.StyledPanel)
        self.mecanicContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.mecanicContainer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.mecanicLabel = QLabel(self.mecanicContainer)
        self.mecanicLabel.setObjectName(u"mecanicLabel")
        self.mecanicLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.mecanicLabel, 0, Qt.AlignHCenter)

        self.mecanicSubContainer = QWidget(self.mecanicContainer)
        self.mecanicSubContainer.setObjectName(u"mecanicSubContainer")
        sizePolicy2.setHeightForWidth(self.mecanicSubContainer.sizePolicy().hasHeightForWidth())
        self.mecanicSubContainer.setSizePolicy(sizePolicy2)
        self.gridLayout_6 = QGridLayout(self.mecanicSubContainer)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.anglesVerificationButton = QPushButton(self.mecanicSubContainer)
        self.anglesVerificationButton.setObjectName(u"anglesVerificationButton")
        self.anglesVerificationButton.setFont(font1)
        self.anglesVerificationButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.anglesVerificationButton, 0, 0, 1, 1)

        self.animationButton = QPushButton(self.mecanicSubContainer)
        self.animationButton.setObjectName(u"animationButton")
        self.animationButton.setFont(font1)
        self.animationButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.animationButton, 0, 1, 1, 1)

        self.spdButton = QPushButton(self.mecanicSubContainer)
        self.spdButton.setObjectName(u"spdButton")
        self.spdButton.setFont(font1)
        self.spdButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.spdButton, 1, 0, 1, 1)

        self.hertzPressureButton = QPushButton(self.mecanicSubContainer)
        self.hertzPressureButton.setObjectName(u"hertzPressureButton")
        self.hertzPressureButton.setFont(font1)
        self.hertzPressureButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.hertzPressureButton, 1, 1, 1, 1)

        self.pvButton = QPushButton(self.mecanicSubContainer)
        self.pvButton.setObjectName(u"pvButton")
        self.pvButton.setFont(font1)
        self.pvButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.pvButton, 2, 0, 1, 1)

        self.oilThicknessButton = QPushButton(self.mecanicSubContainer)
        self.oilThicknessButton.setObjectName(u"oilThicknessButton")
        self.oilThicknessButton.setFont(font1)
        self.oilThicknessButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.oilThicknessButton, 2, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.mecanicSubContainer)


        self.gridLayout.addWidget(self.mecanicContainer, 1, 0, 1, 1)

        self.settingsFrame = QFrame(self.mainContainer)
        self.settingsFrame.setObjectName(u"settingsFrame")
        self.settingsFrame.setStyleSheet(u"border-color: rgb(17, 48, 83);\n"
"background-color: rgb(223, 223, 223);")
        self.settingsFrame.setFrameShape(QFrame.StyledPanel)
        self.settingsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.settingsFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.optionButton = QPushButton(self.settingsFrame)
        self.optionButton.setObjectName(u"optionButton")
        self.optionButton.setFont(font1)
        self.optionButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.optionButton, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.settingsFrame, 2, 1, 1, 1)

        self.manufacturingFrame = QFrame(self.mainContainer)
        self.manufacturingFrame.setObjectName(u"manufacturingFrame")
        self.manufacturingFrame.setStyleSheet(u"border-color: rgb(17, 48, 83);\n"
"background-color: rgb(223, 223, 223);")
        self.manufacturingFrame.setFrameShape(QFrame.StyledPanel)
        self.manufacturingFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.manufacturingFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.manufacturingLabel = QLabel(self.manufacturingFrame)
        self.manufacturingLabel.setObjectName(u"manufacturingLabel")
        self.manufacturingLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.manufacturingLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.manufacturingSubContainer = QWidget(self.manufacturingFrame)
        self.manufacturingSubContainer.setObjectName(u"manufacturingSubContainer")
        sizePolicy2.setHeightForWidth(self.manufacturingSubContainer.sizePolicy().hasHeightForWidth())
        self.manufacturingSubContainer.setSizePolicy(sizePolicy2)
        self.gridLayout_4 = QGridLayout(self.manufacturingSubContainer)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton = QPushButton(self.manufacturingSubContainer)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.manufacturingSubContainer)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.pushButton_2, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.manufacturingSubContainer)


        self.gridLayout.addWidget(self.manufacturingFrame, 1, 1, 1, 1)

        self.frame = QFrame(self.mainContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-color: rgb(17, 48, 83);\n"
"background-color: rgb(223, 223, 223);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_5)


        self.verticalLayout_3.addWidget(self.widget)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpenCameDialog.setText(QCoreApplication.translate("MainWindow", u"OpenCameDialog", None))
        self.homeButton.setText("")
        self.newButton.setText("")
        self.openButton.setText("")
        self.saveButton.setText("")
        self.exportButton.setText("")
        self.helpButton.setText("")
        self.lawsDefinitionLabel.setText(QCoreApplication.translate("MainWindow", u"Lois de Distribution", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Acceleration", None))
        self.systemDefinitionLabel.setText(QCoreApplication.translate("MainWindow", u"Syst\u00e8me de Distribution", None))
        self.valveButton.setText(QCoreApplication.translate("MainWindow", u"Soupape", None))
        self.springButton.setText(QCoreApplication.translate("MainWindow", u"Ressort", None))
        self.camButton.setText(QCoreApplication.translate("MainWindow", u"Came", None))
        self.rockerArmButton.setText(QCoreApplication.translate("MainWindow", u"Linguet", None))
        self.assemblyButton.setText(QCoreApplication.translate("MainWindow", u"Assemblage", None))
        self.mecanicLabel.setText(QCoreApplication.translate("MainWindow", u"V\u00e9rification Cin\u00e9matique et M\u00e9canique", None))
        self.anglesVerificationButton.setText(QCoreApplication.translate("MainWindow", u"Angles Limites", None))
        self.animationButton.setText(QCoreApplication.translate("MainWindow", u"Visualisation", None))
        self.spdButton.setText(QCoreApplication.translate("MainWindow", u"Vitesses de Balayage", None))
        self.hertzPressureButton.setText(QCoreApplication.translate("MainWindow", u"Pressions de Hertz", None))
        self.pvButton.setText(QCoreApplication.translate("MainWindow", u"Coefficient de Grippage", None))
        self.oilThicknessButton.setText(QCoreApplication.translate("MainWindow", u"\u00c9paisseur du Film d'Huile", None))
        self.optionButton.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.manufacturingLabel.setText(QCoreApplication.translate("MainWindow", u"Fabrication", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Rayon de Courbure", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Roller", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Comparer", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Charger \u00c9tude Ant\u00e9rieure", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Comparer", None))
    # retranslateUi




