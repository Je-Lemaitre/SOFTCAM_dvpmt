# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'roller_dialog_empty.ui'
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

class Ui_RollerDialog(object):
    def setupUi(self, RollerDialog):
        if not RollerDialog.objectName():
            RollerDialog.setObjectName(u"RollerDialog")
        RollerDialog.resize(1146, 596)
        RollerDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.rollerLayout = QVBoxLayout(RollerDialog)
        self.rollerLayout.setObjectName(u"rollerLayout")
        self.mainWidget = QWidget(RollerDialog)
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

        self.rollerradiusLabel = QLabel(self.parametersWidget)
        self.rollerradiusLabel.setObjectName(u"rollerradiusLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rollerradiusLabel.sizePolicy().hasHeightForWidth())
        self.rollerradiusLabel.setSizePolicy(sizePolicy)

        self.parametersLayout.addWidget(self.rollerradiusLabel)

        self.rollerradiusEdit = QLineEdit(self.parametersWidget)
        self.rollerradiusEdit.setObjectName(u"rollerradiusEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rollerradiusEdit.sizePolicy().hasHeightForWidth())
        self.rollerradiusEdit.setSizePolicy(sizePolicy1)
        self.rollerradiusEdit.setMaximumSize(QSize(70, 16777215))
        self.rollerradiusEdit.setSizeIncrement(QSize(0, 0))

        self.parametersLayout.addWidget(self.rollerradiusEdit, 0, Qt.AlignHCenter)

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
        self.displacementPage = QWidget()
        self.displacementPage.setObjectName(u"displacementPage")
        sizePolicy3.setHeightForWidth(self.displacementPage.sizePolicy().hasHeightForWidth())
        self.displacementPage.setSizePolicy(sizePolicy3)
        self.displacementLayout = QVBoxLayout(self.displacementPage)
        self.displacementLayout.setObjectName(u"displacementLayout")
        self.displacementLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.displacementPage)

        self.mainLayout.addWidget(self.stackedWidget)


        self.rollerLayout.addWidget(self.mainWidget)

        self.buttonsWidget = QWidget(RollerDialog)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.buttonsLayout = QHBoxLayout(self.buttonsWidget)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonBox = QDialogButtonBox(self.buttonsWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonsLayout.addWidget(self.buttonBox)

        self.horizontalSpacer_4 = QSpacerItem(500, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_4)

        self.computeButton = QPushButton(self.buttonsWidget)
        self.computeButton.setObjectName(u"computeButton")

        self.buttonsLayout.addWidget(self.computeButton)

        self.horizontalSpacer = QSpacerItem(500, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer)

        self.resetviewButton = QPushButton(self.buttonsWidget)
        self.resetviewButton.setObjectName(u"resetviewButton")

        self.buttonsLayout.addWidget(self.resetviewButton)


        self.rollerLayout.addWidget(self.buttonsWidget)


        self.retranslateUi(RollerDialog)
        self.populateUi()
        self.buttonBox.accepted.connect(RollerDialog.accept)
        self.buttonBox.rejected.connect(RollerDialog.reject)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RollerDialog)
    # setupUi

    def retranslateUi(self, RollerDialog):
        RollerDialog.setWindowTitle(QCoreApplication.translate("RollerDialog", u"V\u00e9rification Pression de Hertz", None))
        self.rollerradiusLabel.setText(QCoreApplication.translate("RollerDialog", u"<html><head/><body><p align=\"center\">Rayon <br/> Roller (mm) </p></body></html>", None))
        self.infoLabel.setText(QCoreApplication.translate("RollerDialog", u"<html><head/><body><p align=\"center\">Informations</p></body></html>", None))
        self.infoButton.setText("")
        self.computeButton.setText(QCoreApplication.translate("RollerDialog", u"Calcul", None))
        self.resetviewButton.setText(QCoreApplication.translate("RollerDialog", u"Reset View", None))
    # retranslateUi

    def populateUi(self):
        self.displacementPlotWidget = pg.PlotWidget(title="Déplacement Roller en Fonction de l'Angle de Rotation de la Came")
        self.displacementPlotWidget.setXRange(0, 200)
        self.displacementPlotWidget.setYRange(0, 40)
        self.displacementPlotWidget.setLabel("bottom", "Angle de Rotation", units="°")
        self.displacementPlotWidget.setLabel("left", "Déplacement", units="mm")
        self.displacementPlotWidget.setAspectLocked(False)
        self.displacementPlotWidget.showGrid(x=True, y=True)
        self.displacementLayout.addWidget(self.displacementPlotWidget)
        self.displacementCurve = pg.PlotDataItem(pen='b')
        self.displacementPlotWidget.addItem(self.displacementCurve)
        self.displacementPlotWidget.setBackground('w')

