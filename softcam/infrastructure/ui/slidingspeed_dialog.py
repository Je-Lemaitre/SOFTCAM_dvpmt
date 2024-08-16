# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'slidingspeed_dialog_empty.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import infrastructure.ui.resources.resources_rc
import pyqtgraph as pg

class Ui_SlidingSpeedDialog(object):
    def setupUi(self, SlidingSpeedDialog):
        if not SlidingSpeedDialog.objectName():
            SlidingSpeedDialog.setObjectName(u"SlidingSpeedDialog")
        SlidingSpeedDialog.resize(1146, 596)
        SlidingSpeedDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dialogLayout = QVBoxLayout(SlidingSpeedDialog)
        self.dialogLayout.setObjectName(u"dialogLayout")
        self.mainWidget = QWidget(SlidingSpeedDialog)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainLayout = QHBoxLayout(self.mainWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.parametersWidget = QWidget(self.mainWidget)
        self.parametersWidget.setObjectName(u"parametersWidget")
        self.parametersLayout = QVBoxLayout(self.parametersWidget)
        self.parametersLayout.setObjectName(u"parametersLayout")
        self.parametersLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.parametersLayout.addItem(self.verticalSpacer_2)

        self.floatspeedLabel = QLabel(self.parametersWidget)
        self.floatspeedLabel.setObjectName(u"floatspeedLabel")

        self.parametersLayout.addWidget(self.floatspeedLabel, 0, Qt.AlignHCenter)

        self.floatspeedEdit = QLineEdit(self.parametersWidget)
        self.floatspeedEdit.setObjectName(u"floatspeedEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.floatspeedEdit.sizePolicy().hasHeightForWidth())
        self.floatspeedEdit.setSizePolicy(sizePolicy)
        self.floatspeedEdit.setMaximumSize(QSize(70, 16777215))
        self.floatspeedEdit.setReadOnly(True)

        self.parametersLayout.addWidget(self.floatspeedEdit, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.parametersLayout.addItem(self.verticalSpacer_4)

        self.usespeedLabel = QLabel(self.parametersWidget)
        self.usespeedLabel.setObjectName(u"usespeedLabel")

        self.parametersLayout.addWidget(self.usespeedLabel)

        self.usespeedEdit = QLineEdit(self.parametersWidget)
        self.usespeedEdit.setObjectName(u"usespeedEdit")
        sizePolicy.setHeightForWidth(self.usespeedEdit.sizePolicy().hasHeightForWidth())
        self.usespeedEdit.setSizePolicy(sizePolicy)
        self.usespeedEdit.setMaximumSize(QSize(70, 16777215))

        self.parametersLayout.addWidget(self.usespeedEdit, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.parametersLayout.addItem(self.verticalSpacer_3)

        self.limitspeedLabel = QLabel(self.parametersWidget)
        self.limitspeedLabel.setObjectName(u"limitspeedLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.limitspeedLabel.sizePolicy().hasHeightForWidth())
        self.limitspeedLabel.setSizePolicy(sizePolicy1)

        self.parametersLayout.addWidget(self.limitspeedLabel)

        self.limitspeedEdit = QLineEdit(self.parametersWidget)
        self.limitspeedEdit.setObjectName(u"limitspeedEdit")
        sizePolicy.setHeightForWidth(self.limitspeedEdit.sizePolicy().hasHeightForWidth())
        self.limitspeedEdit.setSizePolicy(sizePolicy)
        self.limitspeedEdit.setMaximumSize(QSize(70, 16777215))
        self.limitspeedEdit.setSizeIncrement(QSize(0, 0))

        self.parametersLayout.addWidget(self.limitspeedEdit, 0, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.parametersLayout.addItem(self.verticalSpacer_5)

        self.contactLabel = QLabel(self.parametersWidget)
        self.contactLabel.setObjectName(u"contactLabel")

        self.parametersLayout.addWidget(self.contactLabel)

        self.contactComboBox = QComboBox(self.parametersWidget)
        self.contactComboBox.addItem("")
        self.contactComboBox.addItem("")
        self.contactComboBox.addItem("")
        self.contactComboBox.setObjectName(u"contactComboBox")

        self.parametersLayout.addWidget(self.contactComboBox)

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
        self.usespeedPage = QWidget()
        self.usespeedPage.setObjectName(u"usespeedPage")
        sizePolicy3.setHeightForWidth(self.usespeedPage.sizePolicy().hasHeightForWidth())
        self.usespeedPage.setSizePolicy(sizePolicy3)
        self.usespeedLayout = QVBoxLayout(self.usespeedPage)
        self.usespeedLayout.setObjectName(u"usespeedLayout")
        self.usespeedLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.usespeedPage)
        self.floatspeedPage = QWidget()
        self.floatspeedPage.setObjectName(u"floatspeedPage")
        sizePolicy3.setHeightForWidth(self.floatspeedPage.sizePolicy().hasHeightForWidth())
        self.floatspeedPage.setSizePolicy(sizePolicy3)
        self.floatspeedLayout = QVBoxLayout(self.floatspeedPage)
        self.floatspeedLayout.setObjectName(u"floatspeedLayout")
        self.floatspeedLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.floatspeedPage)

        self.mainLayout.addWidget(self.stackedWidget)


        self.dialogLayout.addWidget(self.mainWidget)

        self.buttonsWidget = QWidget(SlidingSpeedDialog)
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

        self.usespeedButton = QPushButton(self.buttonsWidget)
        self.usespeedButton.setObjectName(u"usespeedButton")

        self.buttonsLayout.addWidget(self.usespeedButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_2)

        self.floatspeedButton = QPushButton(self.buttonsWidget)
        self.floatspeedButton.setObjectName(u"floatspeedButton")

        self.buttonsLayout.addWidget(self.floatspeedButton)

        self.horizontalSpacer_1 = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_1)

        self.resetviewButton = QPushButton(self.buttonsWidget)
        self.resetviewButton.setObjectName(u"resetviewButton")

        self.buttonsLayout.addWidget(self.resetviewButton)


        self.dialogLayout.addWidget(self.buttonsWidget)


        self.retranslateUi(SlidingSpeedDialog)
        self.populateUi()
        self.buttonBox.accepted.connect(SlidingSpeedDialog.accept)
        self.buttonBox.rejected.connect(SlidingSpeedDialog.reject)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(SlidingSpeedDialog)
    # setupUi

    def retranslateUi(self, SlidingSpeedDialog):
        SlidingSpeedDialog.setWindowTitle(QCoreApplication.translate("SlidingSpeedDialog", u"Vitesses de Balayage", None))
        self.floatspeedLabel.setText(QCoreApplication.translate("SlidingSpeedDialog", u"<html><head/><body><p align=\"center\">Affolement <br/>(tr/min)</p></body></html>", None))
        self.usespeedLabel.setText(QCoreApplication.translate("SlidingSpeedDialog", u"<html><head/><body><p align=\"center\">Regime Utilisation <br/>(tr/min) </p></body></html>", None))
        self.limitspeedLabel.setText(QCoreApplication.translate("SlidingSpeedDialog", u"<html><head/><body><p align=\"center\">Vitesse Limite <br/>(mm/s) </p></body></html>", None))
        self.limitspeedEdit.setText("")
        self.contactLabel.setText(QCoreApplication.translate("SlidingSpeedDialog", u"<html><head/><body><p align=\"center\">Contact</p></body></html>", None))
        self.contactComboBox.setItemText(0, QCoreApplication.translate("SlidingSpeedDialog", u"Came/Soupape", None))
        self.contactComboBox.setItemText(1, QCoreApplication.translate("SlidingSpeedDialog", u"Came/Patin", None))
        self.contactComboBox.setItemText(2, QCoreApplication.translate("SlidingSpeedDialog", u"Soupape/Patin", None))

        self.infoLabel.setText(QCoreApplication.translate("SlidingSpeedDialog", u"<html><head/><body><p align=\"center\">Informations</p></body></html>", None))
        self.infoButton.setText("")
        self.computeButton.setText(QCoreApplication.translate("SlidingSpeedDialog", u"Calcul", None))
        self.usespeedButton.setText(QCoreApplication.translate("SlidingSpeedDialog", u"Regime Utilisation", None))
        self.floatspeedButton.setText(QCoreApplication.translate("SlidingSpeedDialog", u"Affolement", None))
        self.resetviewButton.setText(QCoreApplication.translate("SlidingSpeedDialog", u"Reset View", None))
    # retranslateUi

    def populateUi(self):

        self.usespeedPlotWidget = pg.PlotWidget(title="Régime d'utilisation")
        self.usespeedPlotWidget.setXRange(0, 200)
        self.usespeedPlotWidget.setYRange(-20, 20)
        self.usespeedPlotWidget.setLabel("bottom", "Angle Rotation Came", units="°")
        self.usespeedPlotWidget.setLabel("left", "Vitesse de Glissement", units="m/s")
        self.usespeedPlotWidget.setAspectLocked(False)
        self.usespeedPlotWidget.showGrid(x=True, y=True)
        self.usespeedLayout.addWidget(self.usespeedPlotWidget)
        self.contact1_usespeedCurve = pg.PlotDataItem(pen=pg.mkPen(color='b', width=2))
        self.usespeedPlotWidget.addItem(self.contact1_usespeedCurve)
        self.contact2_usespeedCurve = pg.PlotDataItem(pen=pg.mkPen(color='g', width=2))
        self.usespeedPlotWidget.addItem(self.contact2_usespeedCurve)
        self.usespeedPlotWidget.setBackground('w')

        self.floatspeedPlotWidget = pg.PlotWidget(title="Régime d'affolement")
        self.floatspeedPlotWidget.setXRange(0, 200)
        self.floatspeedPlotWidget.setYRange(-20, 20)
        self.floatspeedPlotWidget.setLabel("bottom", "Angle Rotation Came", units="°")
        self.floatspeedPlotWidget.setLabel("left", "Vitesse de Glissement", units="m/s")
        self.floatspeedPlotWidget.setAspectLocked(False)
        self.floatspeedPlotWidget.showGrid(x=True, y=True)
        self.floatspeedLayout.addWidget(self.floatspeedPlotWidget)
        self.contact1_floatspeedCurve = pg.PlotDataItem(pen=pg.mkPen(color='b', width=2))
        self.floatspeedPlotWidget.addItem(self.contact1_floatspeedCurve)
        self.contact2_floatspeedCurve = pg.PlotDataItem(pen=pg.mkPen(color='g', width=2))
        self.floatspeedPlotWidget.addItem(self.contact2_floatspeedCurve)
        self.floatspeedPlotWidget.setBackground('w')


