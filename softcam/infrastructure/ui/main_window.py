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
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import infrastructure.ui.resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1248, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/icons/oreca-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
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
        self.lawsFrame = QFrame(self.mainContainer)
        self.lawsFrame.setObjectName(u"lawsFrame")
        self.lawsFrame.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 240, 240);")
        self.lawsFrame.setFrameShape(QFrame.StyledPanel)
        self.lawsFrame.setFrameShadow(QFrame.Raised)
        self.lawsLayout = QVBoxLayout(self.lawsFrame)
        self.lawsLayout.setObjectName(u"lawsLayout")
        self.lawsLabel = QLabel(self.lawsFrame)
        self.lawsLabel.setObjectName(u"lawsLabel")
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(True)
        self.lawsLabel.setFont(font)

        self.lawsLayout.addWidget(self.lawsLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.lawsSubContainer = QWidget(self.lawsFrame)
        self.lawsSubContainer.setObjectName(u"lawsSubContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.lawsSubContainer.sizePolicy().hasHeightForWidth())
        self.lawsSubContainer.setSizePolicy(sizePolicy2)
        self.lawsSubLayout = QGridLayout(self.lawsSubContainer)
        self.lawsSubLayout.setObjectName(u"lawsSubLayout")
        self.lawsButton = QPushButton(self.lawsSubContainer)
        self.lawsButton.setObjectName(u"lawsButton")
        sizePolicy.setHeightForWidth(self.lawsButton.sizePolicy().hasHeightForWidth())
        self.lawsButton.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.lawsButton.setFont(font1)
        self.lawsButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.lawsSubLayout.addWidget(self.lawsButton, 0, 0, 1, 1)


        self.lawsLayout.addWidget(self.lawsSubContainer)


        self.gridLayout.addWidget(self.lawsFrame, 0, 1, 1, 1)

        self.assemblyFrame = QFrame(self.mainContainer)
        self.assemblyFrame.setObjectName(u"assemblyFrame")
        self.assemblyFrame.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 240, 240);")
        self.assemblyFrame.setFrameShape(QFrame.StyledPanel)
        self.assemblyFrame.setFrameShadow(QFrame.Raised)
        self.assemblyLayout = QVBoxLayout(self.assemblyFrame)
        self.assemblyLayout.setObjectName(u"assemblyLayout")
        self.assemblyDefinitionLabel = QLabel(self.assemblyFrame)
        self.assemblyDefinitionLabel.setObjectName(u"assemblyDefinitionLabel")
        self.assemblyDefinitionLabel.setFont(font)

        self.assemblyLayout.addWidget(self.assemblyDefinitionLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.assemblySubContainer = QWidget(self.assemblyFrame)
        self.assemblySubContainer.setObjectName(u"assemblySubContainer")
        sizePolicy2.setHeightForWidth(self.assemblySubContainer.sizePolicy().hasHeightForWidth())
        self.assemblySubContainer.setSizePolicy(sizePolicy2)
        self.assemblySubLayout = QVBoxLayout(self.assemblySubContainer)
        self.assemblySubLayout.setObjectName(u"assemblySubLayout")
        self.assemblyButton = QPushButton(self.assemblySubContainer)
        self.assemblyButton.setObjectName(u"assemblyButton")
        sizePolicy.setHeightForWidth(self.assemblyButton.sizePolicy().hasHeightForWidth())
        self.assemblyButton.setSizePolicy(sizePolicy)
        self.assemblyButton.setFont(font1)
        self.assemblyButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.assemblySubLayout.addWidget(self.assemblyButton)


        self.assemblyLayout.addWidget(self.assemblySubContainer)


        self.gridLayout.addWidget(self.assemblyFrame, 0, 0, 1, 1)

        self.mechanicContainer = QFrame(self.mainContainer)
        self.mechanicContainer.setObjectName(u"mechanicContainer")
        self.mechanicContainer.setStyleSheet(u"border-color: rgb(17, 48, 83);\n"
"background-color: rgb(240, 240, 240);")
        self.mechanicContainer.setFrameShape(QFrame.StyledPanel)
        self.mechanicContainer.setFrameShadow(QFrame.Raised)
        self.mechanicLayout = QVBoxLayout(self.mechanicContainer)
        self.mechanicLayout.setObjectName(u"mechanicLayout")
        self.mechanicLabel = QLabel(self.mechanicContainer)
        self.mechanicLabel.setObjectName(u"mechanicLabel")
        self.mechanicLabel.setFont(font)

        self.mechanicLayout.addWidget(self.mechanicLabel, 0, Qt.AlignHCenter)

        self.mechanicSubContainer = QWidget(self.mechanicContainer)
        self.mechanicSubContainer.setObjectName(u"mechanicSubContainer")
        sizePolicy2.setHeightForWidth(self.mechanicSubContainer.sizePolicy().hasHeightForWidth())
        self.mechanicSubContainer.setSizePolicy(sizePolicy2)
        self.mechanicSubLayout = QGridLayout(self.mechanicSubContainer)
        self.mechanicSubLayout.setObjectName(u"mechanicSubLayout")
        self.pvButton = QPushButton(self.mechanicSubContainer)
        self.pvButton.setObjectName(u"pvButton")
        sizePolicy.setHeightForWidth(self.pvButton.sizePolicy().hasHeightForWidth())
        self.pvButton.setSizePolicy(sizePolicy)
        self.pvButton.setFont(font1)
        self.pvButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.mechanicSubLayout.addWidget(self.pvButton, 5, 0, 1, 1)

        self.verificationButton = QPushButton(self.mechanicSubContainer)
        self.verificationButton.setObjectName(u"verificationButton")
        sizePolicy.setHeightForWidth(self.verificationButton.sizePolicy().hasHeightForWidth())
        self.verificationButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(13)
        font2.setBold(False)
        self.verificationButton.setFont(font2)
        self.verificationButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")

        self.mechanicSubLayout.addWidget(self.verificationButton, 1, 1, 1, 1)

        self.hertzButton = QPushButton(self.mechanicSubContainer)
        self.hertzButton.setObjectName(u"hertzButton")
        sizePolicy.setHeightForWidth(self.hertzButton.sizePolicy().hasHeightForWidth())
        self.hertzButton.setSizePolicy(sizePolicy)
        self.hertzButton.setFont(font1)
        self.hertzButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.mechanicSubLayout.addWidget(self.hertzButton, 4, 1, 1, 1)

        self.animationButton = QPushButton(self.mechanicSubContainer)
        self.animationButton.setObjectName(u"animationButton")
        sizePolicy.setHeightForWidth(self.animationButton.sizePolicy().hasHeightForWidth())
        self.animationButton.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.animationButton.setFont(font3)
        self.animationButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")

        self.mechanicSubLayout.addWidget(self.animationButton, 1, 0, 1, 1)

        self.lubricationButton = QPushButton(self.mechanicSubContainer)
        self.lubricationButton.setObjectName(u"lubricationButton")
        sizePolicy.setHeightForWidth(self.lubricationButton.sizePolicy().hasHeightForWidth())
        self.lubricationButton.setSizePolicy(sizePolicy)
        self.lubricationButton.setFont(font1)
        self.lubricationButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.mechanicSubLayout.addWidget(self.lubricationButton, 5, 1, 1, 1)

        self.forceButton = QPushButton(self.mechanicSubContainer)
        self.forceButton.setObjectName(u"forceButton")
        self.forceButton.setFont(font2)
        self.forceButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 119, 217);")

        self.mechanicSubLayout.addWidget(self.forceButton, 4, 0, 1, 1)

        self.contactposButton = QPushButton(self.mechanicSubContainer)
        self.contactposButton.setObjectName(u"contactposButton")
        sizePolicy.setHeightForWidth(self.contactposButton.sizePolicy().hasHeightForWidth())
        self.contactposButton.setSizePolicy(sizePolicy)
        self.contactposButton.setFont(font3)
        self.contactposButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.mechanicSubLayout.addWidget(self.contactposButton, 2, 0, 1, 1)

        self.slidingspeedButton = QPushButton(self.mechanicSubContainer)
        self.slidingspeedButton.setObjectName(u"slidingspeedButton")
        sizePolicy.setHeightForWidth(self.slidingspeedButton.sizePolicy().hasHeightForWidth())
        self.slidingspeedButton.setSizePolicy(sizePolicy)
        self.slidingspeedButton.setFont(font3)
        self.slidingspeedButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.mechanicSubLayout.addWidget(self.slidingspeedButton, 2, 1, 1, 1)


        self.mechanicLayout.addWidget(self.mechanicSubContainer)


        self.gridLayout.addWidget(self.mechanicContainer, 1, 0, 1, 1)

        self.settingsFrame = QFrame(self.mainContainer)
        self.settingsFrame.setObjectName(u"settingsFrame")
        self.settingsFrame.setStyleSheet(u"border-color: rgb(17, 48, 83);\n"
"background-color: rgb(240, 240, 240);")
        self.settingsFrame.setFrameShape(QFrame.StyledPanel)
        self.settingsFrame.setFrameShadow(QFrame.Raised)
        self.settingsLayout = QGridLayout(self.settingsFrame)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.optionButton = QPushButton(self.settingsFrame)
        self.optionButton.setObjectName(u"optionButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.optionButton.sizePolicy().hasHeightForWidth())
        self.optionButton.setSizePolicy(sizePolicy3)
        self.optionButton.setFont(font1)
        self.optionButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.settingsLayout.addWidget(self.optionButton, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.settingsFrame, 2, 1, 1, 1)

        self.manufacturingFrame = QFrame(self.mainContainer)
        self.manufacturingFrame.setObjectName(u"manufacturingFrame")
        self.manufacturingFrame.setStyleSheet(u"border-color: rgb(17, 48, 83);\n"
"background-color: rgb(240, 240, 240);")
        self.manufacturingFrame.setFrameShape(QFrame.StyledPanel)
        self.manufacturingFrame.setFrameShadow(QFrame.Raised)
        self.manufacturingLayout = QVBoxLayout(self.manufacturingFrame)
        self.manufacturingLayout.setObjectName(u"manufacturingLayout")
        self.manufacturingLabel = QLabel(self.manufacturingFrame)
        self.manufacturingLabel.setObjectName(u"manufacturingLabel")
        self.manufacturingLabel.setFont(font)

        self.manufacturingLayout.addWidget(self.manufacturingLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.manufacturingSubContainer = QWidget(self.manufacturingFrame)
        self.manufacturingSubContainer.setObjectName(u"manufacturingSubContainer")
        sizePolicy2.setHeightForWidth(self.manufacturingSubContainer.sizePolicy().hasHeightForWidth())
        self.manufacturingSubContainer.setSizePolicy(sizePolicy2)
        self.manufacturingSubLayout = QGridLayout(self.manufacturingSubContainer)
        self.manufacturingSubLayout.setObjectName(u"manufacturingSubLayout")
        self.curvatureButton = QPushButton(self.manufacturingSubContainer)
        self.curvatureButton.setObjectName(u"curvatureButton")
        sizePolicy.setHeightForWidth(self.curvatureButton.sizePolicy().hasHeightForWidth())
        self.curvatureButton.setSizePolicy(sizePolicy)
        self.curvatureButton.setFont(font1)
        self.curvatureButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.manufacturingSubLayout.addWidget(self.curvatureButton, 0, 0, 1, 1)

        self.rollerButton = QPushButton(self.manufacturingSubContainer)
        self.rollerButton.setObjectName(u"rollerButton")
        sizePolicy.setHeightForWidth(self.rollerButton.sizePolicy().hasHeightForWidth())
        self.rollerButton.setSizePolicy(sizePolicy)
        self.rollerButton.setFont(font1)
        self.rollerButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.manufacturingSubLayout.addWidget(self.rollerButton, 0, 1, 1, 1)


        self.manufacturingLayout.addWidget(self.manufacturingSubContainer)


        self.gridLayout.addWidget(self.manufacturingFrame, 1, 1, 1, 1)

        self.compareFrame = QFrame(self.mainContainer)
        self.compareFrame.setObjectName(u"compareFrame")
        self.compareFrame.setStyleSheet(u"border-color: rgb(17, 48, 83);\n"
"background-color: rgb(240, 240, 240);")
        self.compareFrame.setFrameShape(QFrame.StyledPanel)
        self.compareFrame.setFrameShadow(QFrame.Raised)
        self.compareLayout = QVBoxLayout(self.compareFrame)
        self.compareLayout.setObjectName(u"compareLayout")
        self.compareLabel = QLabel(self.compareFrame)
        self.compareLabel.setObjectName(u"compareLabel")
        self.compareLabel.setFont(font)

        self.compareLayout.addWidget(self.compareLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.compareWidget = QWidget(self.compareFrame)
        self.compareWidget.setObjectName(u"compareWidget")
        sizePolicy2.setHeightForWidth(self.compareWidget.sizePolicy().hasHeightForWidth())
        self.compareWidget.setSizePolicy(sizePolicy2)
        self.compareSubLayout = QHBoxLayout(self.compareWidget)
        self.compareSubLayout.setObjectName(u"compareSubLayout")
        self.loadStudyButton = QPushButton(self.compareWidget)
        self.loadStudyButton.setObjectName(u"loadStudyButton")
        sizePolicy3.setHeightForWidth(self.loadStudyButton.sizePolicy().hasHeightForWidth())
        self.loadStudyButton.setSizePolicy(sizePolicy3)
        self.loadStudyButton.setFont(font1)
        self.loadStudyButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.compareSubLayout.addWidget(self.loadStudyButton)

        self.compareButton = QPushButton(self.compareWidget)
        self.compareButton.setObjectName(u"compareButton")
        sizePolicy3.setHeightForWidth(self.compareButton.sizePolicy().hasHeightForWidth())
        self.compareButton.setSizePolicy(sizePolicy3)
        self.compareButton.setFont(font1)
        self.compareButton.setStyleSheet(u"background-color: rgb(0, 119, 217);\n"
"color: rgb(255, 255, 255);")

        self.compareSubLayout.addWidget(self.compareButton)


        self.compareLayout.addWidget(self.compareWidget)


        self.gridLayout.addWidget(self.compareFrame, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SOTCAM - Accueil", None))
        self.actionOpenCameDialog.setText(QCoreApplication.translate("MainWindow", u"OpenCameDialog", None))
        self.homeButton.setText("")
        self.newButton.setText("")
        self.openButton.setText("")
        self.saveButton.setText("")
        self.exportButton.setText("")
        self.helpButton.setText("")
        self.lawsLabel.setText(QCoreApplication.translate("MainWindow", u"Lois de Distribution", None))
        self.lawsButton.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er Lois", None))
        self.assemblyDefinitionLabel.setText(QCoreApplication.translate("MainWindow", u"Syst\u00e8me de Distribution", None))
        self.assemblyButton.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9er Assemblage", None))
        self.mechanicLabel.setText(QCoreApplication.translate("MainWindow", u"M\u00e9canique", None))
        self.pvButton.setText(QCoreApplication.translate("MainWindow", u"Coefficient de Grippage", None))
        self.verificationButton.setText(QCoreApplication.translate("MainWindow", u"V\u00e9rifications M\u00e9caniques", None))
        self.hertzButton.setText(QCoreApplication.translate("MainWindow", u"Pressions de Hertz", None))
        self.animationButton.setText(QCoreApplication.translate("MainWindow", u"Visualisation Cin\u00e9matique", None))
        self.lubricationButton.setText(QCoreApplication.translate("MainWindow", u"\u00c9paisseur du Film d'Huile", None))
        self.forceButton.setText(QCoreApplication.translate("MainWindow", u"Efforts Syst\u00e8me", None))
        self.contactposButton.setText(QCoreApplication.translate("MainWindow", u"Position Contact", None))
        self.slidingspeedButton.setText(QCoreApplication.translate("MainWindow", u"Vitesses de Balayage", None))
        self.optionButton.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.manufacturingLabel.setText(QCoreApplication.translate("MainWindow", u"Fabrication", None))
        self.curvatureButton.setText(QCoreApplication.translate("MainWindow", u"Rayon de Courbure", None))
        self.rollerButton.setText(QCoreApplication.translate("MainWindow", u"Roller", None))
        self.compareLabel.setText(QCoreApplication.translate("MainWindow", u"Comparer", None))
        self.loadStudyButton.setText(QCoreApplication.translate("MainWindow", u"Charger \u00c9tude Ant\u00e9rieure", None))
        self.compareButton.setText(QCoreApplication.translate("MainWindow", u"Comparer", None))
    # retranslateUi

