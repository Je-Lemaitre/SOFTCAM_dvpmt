# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contactpos_dialog_empty.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import infrastructure.ui.resources.resources_rc
import pyqtgraph as pg

class Ui_ContactPosDialog(object):
    def setupUi(self, ContactPosDialog):
        if not ContactPosDialog.objectName():
            ContactPosDialog.setObjectName(u"ContactPosDialog")
        ContactPosDialog.resize(1146, 596)
        ContactPosDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dialogLayout = QVBoxLayout(ContactPosDialog)
        self.dialogLayout.setObjectName(u"dialogLayout")
        self.mainWidget = QWidget(ContactPosDialog)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainLayout = QHBoxLayout(self.mainWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.parametersWidget = QWidget(self.mainWidget)
        self.parametersWidget.setObjectName(u"parametersWidget")
        self.parametersLayout = QVBoxLayout(self.parametersWidget)
        self.parametersLayout.setObjectName(u"parametersLayout")
        self.parametersLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.parametersLayout.addItem(self.verticalSpacer_4)

        self.poslimitLabel = QLabel(self.parametersWidget)
        self.poslimitLabel.setObjectName(u"poslimitLabel")

        self.parametersLayout.addWidget(self.poslimitLabel)

        self.poslimitEdit = QLineEdit(self.parametersWidget)
        self.poslimitEdit.setObjectName(u"poslimitEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.poslimitEdit.sizePolicy().hasHeightForWidth())
        self.poslimitEdit.setSizePolicy(sizePolicy)
        self.poslimitEdit.setMaximumSize(QSize(70, 16777215))

        self.parametersLayout.addWidget(self.poslimitEdit, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.parametersLayout.addItem(self.verticalSpacer_3)

        self.neglimitLabel = QLabel(self.parametersWidget)
        self.neglimitLabel.setObjectName(u"neglimitLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.neglimitLabel.sizePolicy().hasHeightForWidth())
        self.neglimitLabel.setSizePolicy(sizePolicy1)

        self.parametersLayout.addWidget(self.neglimitLabel)

        self.neglimitEdit = QLineEdit(self.parametersWidget)
        self.neglimitEdit.setObjectName(u"neglimitEdit")
        sizePolicy.setHeightForWidth(self.neglimitEdit.sizePolicy().hasHeightForWidth())
        self.neglimitEdit.setSizePolicy(sizePolicy)
        self.neglimitEdit.setMaximumSize(QSize(70, 16777215))
        self.neglimitEdit.setSizeIncrement(QSize(0, 0))

        self.parametersLayout.addWidget(self.neglimitEdit, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.parametersLayout.addItem(self.verticalSpacer)

        self.infoLabel = QLabel(self.parametersWidget)
        self.infoLabel.setObjectName(u"infoLabel")

        self.parametersLayout.addWidget(self.infoLabel, 0, Qt.AlignHCenter)

        self.infoButton = QPushButton(self.parametersWidget)
        self.infoButton.setObjectName(u"infoButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.infoButton.sizePolicy().hasHeightForWidth())
        self.infoButton.setSizePolicy(sizePolicy2)
        self.infoButton.setMaximumSize(QSize(30, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/icons/info-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoButton.setIcon(icon)

        self.parametersLayout.addWidget(self.infoButton, 0, Qt.AlignHCenter)


        self.mainLayout.addWidget(self.parametersWidget, 0, Qt.AlignLeft)

        self.stackedWidget = QStackedWidget(self.mainWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.stackedWidget.setFrameShadow(QFrame.Sunken)
        self.camrockerarmPage = QWidget()
        self.camrockerarmPage.setObjectName(u"camrockerarmPage")
        sizePolicy3.setHeightForWidth(self.camrockerarmPage.sizePolicy().hasHeightForWidth())
        self.camrockerarmPage.setSizePolicy(sizePolicy3)
        self.camrockerarmLayout = QVBoxLayout(self.camrockerarmPage)
        self.camrockerarmLayout.setObjectName(u"camrockerarmLayout")
        self.camrockerarmLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.camrockerarmPage)
        self.valverockerarmPage = QWidget()
        self.valverockerarmPage.setObjectName(u"valverockerarmPage")
        sizePolicy3.setHeightForWidth(self.valverockerarmPage.sizePolicy().hasHeightForWidth())
        self.valverockerarmPage.setSizePolicy(sizePolicy3)
        self.valverockerarmLayout = QVBoxLayout(self.valverockerarmPage)
        self.valverockerarmLayout.setObjectName(u"valverockerarmLayout")
        self.valverockerarmLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.valverockerarmPage)
        self.camvalvePage = QWidget()
        self.camvalvePage.setObjectName(u"camvalvePage")
        sizePolicy3.setHeightForWidth(self.camvalvePage.sizePolicy().hasHeightForWidth())
        self.camvalvePage.setSizePolicy(sizePolicy3)
        self.camvalveLayout = QVBoxLayout(self.camvalvePage)
        self.camvalveLayout.setObjectName(u"camvalveLayout")
        self.camvalveLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.camvalvePage)

        self.mainLayout.addWidget(self.stackedWidget)


        self.dialogLayout.addWidget(self.mainWidget)

        self.buttonsWidget = QWidget(ContactPosDialog)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.buttonsLayout = QHBoxLayout(self.buttonsWidget)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonBox = QDialogButtonBox(self.buttonsWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonsLayout.addWidget(self.buttonBox)

        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_4)

        self.computeButton = QPushButton(self.buttonsWidget)
        self.computeButton.setObjectName(u"computeButton")

        self.buttonsLayout.addWidget(self.computeButton)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer)

        self.camrockerarmButton = QPushButton(self.buttonsWidget)
        self.camrockerarmButton.setObjectName(u"camrockerarmButton")

        self.buttonsLayout.addWidget(self.camrockerarmButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_3)

        self.valverockerarmButton = QPushButton(self.buttonsWidget)
        self.valverockerarmButton.setObjectName(u"valverockerarmButton")

        self.buttonsLayout.addWidget(self.valverockerarmButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_2)

        self.camvalveButton = QPushButton(self.buttonsWidget)
        self.camvalveButton.setObjectName(u"camvalveButton")

        self.buttonsLayout.addWidget(self.camvalveButton)

        self.horizontalSpacer_1 = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_1)

        self.resetviewButton = QPushButton(self.buttonsWidget)
        self.resetviewButton.setObjectName(u"resetviewButton")

        self.buttonsLayout.addWidget(self.resetviewButton)


        self.dialogLayout.addWidget(self.buttonsWidget)


        self.retranslateUi(ContactPosDialog)
        self.populateUi()
        self.buttonBox.accepted.connect(ContactPosDialog.accept)
        self.buttonBox.rejected.connect(ContactPosDialog.reject)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(ContactPosDialog)
    # setupUi

    def retranslateUi(self, ContactPosDialog):
        ContactPosDialog.setWindowTitle(QCoreApplication.translate("ContactPosDialog", u"Position des Points de Contact", None))
        self.poslimitLabel.setText(QCoreApplication.translate("ContactPosDialog", u"<html><head/><body><p align=\"center\">Angle Limite <br/> Anti-Horaire (\u00b0) </p></body></html>", None))
        self.neglimitLabel.setText(QCoreApplication.translate("ContactPosDialog", u"<html><head/><body><p align=\"center\">Angle Limite <br/> Horaire (\u00b0) </p></body></html>", None))
        self.infoLabel.setText(QCoreApplication.translate("ContactPosDialog", u"<html><head/><body><p align=\"center\">Informations</p></body></html>", None))
        self.infoButton.setText("")
        self.computeButton.setText(QCoreApplication.translate("ContactPosDialog", u"Calcul", None))
        self.camrockerarmButton.setText(QCoreApplication.translate("ContactPosDialog", u"Came / Patin", None))
        self.valverockerarmButton.setText(QCoreApplication.translate("ContactPosDialog", u"Soupape / Patin", None))
        self.camvalveButton.setText(QCoreApplication.translate("ContactPosDialog", u"Came / Soupape", None))
        self.resetviewButton.setText(QCoreApplication.translate("ContactPosDialog", u"Reset View", None))
    # retranslateUi

    def populateUi(self):
        self.camrockerarmPlotWidget = pg.PlotWidget(title="Contact Came/Patin")
        self.camrockerarmPlotWidget.setXRange(0, 200)
        self.camrockerarmPlotWidget.setYRange(-40, 40)
        self.camrockerarmPlotWidget.setLabel("bottom", "Angle de Rotation de la Came", units="°")
        self.camrockerarmPlotWidget.setLabel("left", "Angle Position Point de Contact", units="°")
        self.camrockerarmPlotWidget.setAspectLocked(False)
        self.camrockerarmPlotWidget.showGrid(x=True, y=True)
        self.camrockerarmLayout.addWidget(self.camrockerarmPlotWidget)
        self.camrockerarmCurve = pg.PlotDataItem(pen='b')
        self.camrockerarmPlotWidget.addItem(self.camrockerarmCurve)
        self.camrockerarmPlotWidget.setBackground('w')

        self.valverockerarmPlotWidget = pg.PlotWidget(title="Contact Soupape/Patin")
        self.valverockerarmPlotWidget.setXRange(0, 200)
        self.valverockerarmPlotWidget.setYRange(-40, 40)
        self.valverockerarmPlotWidget.setLabel("bottom", "Angle de Rotation de la Came", units="°")
        self.valverockerarmPlotWidget.setLabel("left", "Distance", units="mm")
        self.valverockerarmPlotWidget.setAspectLocked(False)
        self.valverockerarmPlotWidget.showGrid(x=True, y=True)
        self.valverockerarmLayout.addWidget(self.valverockerarmPlotWidget)
        self.valverockerarmCurve = pg.PlotDataItem(pen='b')
        self.valverockerarmPlotWidget.addItem(self.valverockerarmCurve)
        self.valverockerarmPlotWidget.setBackground('w')

        self.camvalvePlotWidget = pg.PlotWidget(title="Contact Came/Soupape")
        self.camvalvePlotWidget.setXRange(0, 200)
        self.camvalvePlotWidget.setYRange(-40, 40)
        self.camvalvePlotWidget.setLabel("bottom", "Angle de Rotation de la Came", units="°")
        self.camvalvePlotWidget.setLabel("left", "Angle Position Point de Contact", units="°")
        self.camvalvePlotWidget.setAspectLocked(False)
        self.camvalvePlotWidget.showGrid(x=True, y=True)
        self.camvalveLayout.addWidget(self.camvalvePlotWidget)
        self.camvalveCurve = pg.PlotDataItem(pen='b')
        self.camvalvePlotWidget.addItem(self.camvalveCurve)
        self.camvalvePlotWidget.setBackground('w')

