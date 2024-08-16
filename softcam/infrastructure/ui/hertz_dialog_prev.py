# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hertz_dialog_empty.ui'
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

class Ui_HertzDialog(object):
    def setupUi(self, HertzDialog):
        if not HertzDialog.objectName():
            HertzDialog.setObjectName(u"HertzDialog")
        HertzDialog.resize(1146, 596)
        HertzDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dialogLayout = QVBoxLayout(HertzDialog)
        self.dialogLayout.setObjectName(u"dialogLayout")
        self.mainWidget = QWidget(HertzDialog)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainLayout = QHBoxLayout(self.mainWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.parametersWidget = QWidget(self.mainWidget)
        self.parametersWidget.setObjectName(u"parametersWidget")
        self.parametersLayout = QVBoxLayout(self.parametersWidget)
        self.parametersLayout.setObjectName(u"parametersLayout")
        self.parametersLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

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

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.parametersLayout.addItem(self.verticalSpacer_3)

        self.limitpressureLabel = QLabel(self.parametersWidget)
        self.limitpressureLabel.setObjectName(u"limitpressureLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.limitpressureLabel.sizePolicy().hasHeightForWidth())
        self.limitpressureLabel.setSizePolicy(sizePolicy1)

        self.parametersLayout.addWidget(self.limitpressureLabel)

        self.limitpressureEdit = QLineEdit(self.parametersWidget)
        self.limitpressureEdit.setObjectName(u"limitpressureEdit")
        sizePolicy.setHeightForWidth(self.limitpressureEdit.sizePolicy().hasHeightForWidth())
        self.limitpressureEdit.setSizePolicy(sizePolicy)
        self.limitpressureEdit.setMaximumSize(QSize(70, 16777215))
        self.limitpressureEdit.setSizeIncrement(QSize(0, 0))

        self.parametersLayout.addWidget(self.limitpressureEdit, 0, Qt.AlignHCenter)

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
        self.staticPage = QWidget()
        self.staticPage.setObjectName(u"staticPage")
        sizePolicy3.setHeightForWidth(self.staticPage.sizePolicy().hasHeightForWidth())
        self.staticPage.setSizePolicy(sizePolicy3)
        self.staticLayout = QVBoxLayout(self.staticPage)
        self.staticLayout.setObjectName(u"staticLayout")
        self.staticLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.staticPage)
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

        self.buttonsWidget = QWidget(HertzDialog)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.buttonsLayout = QHBoxLayout(self.buttonsWidget)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonBox = QDialogButtonBox(self.buttonsWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonsLayout.addWidget(self.buttonBox)

        self.horizontalSpacer_4 = QSpacerItem(60, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_4)

        self.computeButton = QPushButton(self.buttonsWidget)
        self.computeButton.setObjectName(u"computeButton")

        self.buttonsLayout.addWidget(self.computeButton)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer)

        self.staticButton = QPushButton(self.buttonsWidget)
        self.staticButton.setObjectName(u"staticButton")

        self.buttonsLayout.addWidget(self.staticButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_3)

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


        self.retranslateUi(HertzDialog)
        self.populateUi()
        self.buttonBox.accepted.connect(HertzDialog.accept)
        self.buttonBox.rejected.connect(HertzDialog.reject)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(HertzDialog)
    # setupUi

    def retranslateUi(self, HertzDialog):
        HertzDialog.setWindowTitle(QCoreApplication.translate("HertzDialog", u"V\u00e9rification Pression de Hertz", None))
        self.floatspeedLabel.setText(QCoreApplication.translate("HertzDialog", u"<html><head/><body><p align=\"center\">Affolement <br/>(tr/min)</p></body></html>", None))
        self.usespeedLabel.setText(QCoreApplication.translate("HertzDialog", u"<html><head/><body><p align=\"center\">Regime Utilisation <br/>(tr/min) </p></body></html>", None))
        self.limitpressureLabel.setText(QCoreApplication.translate("HertzDialog", u"<html><head/><body><p align=\"center\">Pression Limite <br/>(MPa) </p></body></html>", None))
        self.infoLabel.setText(QCoreApplication.translate("HertzDialog", u"<html><head/><body><p align=\"center\">Informations</p></body></html>", None))
        self.infoButton.setText("")
        self.computeButton.setText(QCoreApplication.translate("HertzDialog", u"Calcul", None))
        self.staticButton.setText(QCoreApplication.translate("HertzDialog", u"Statique", None))
        self.usespeedButton.setText(QCoreApplication.translate("HertzDialog", u"Regime Utilisation", None))
        self.floatspeedButton.setText(QCoreApplication.translate("HertzDialog", u"Affolement", None))
        self.resetviewButton.setText(QCoreApplication.translate("HertzDialog", u"Reset View", None))
    # retranslateUi

    def populateUi(self):
        self.staticPlotWidget = pg.PlotWidget(title="Régime nul")
        self.staticPlotWidget.setXRange(0, 200)
        self.staticPlotWidget.setYRange(-10, 40)
        self.staticPlotWidget.setLabel("bottom", "Angle Rotation Came", units="°")
        self.staticPlotWidget.setLabel("left", "Pression de Hertz", units="MPa")
        self.staticPlotWidget.setAspectLocked(False)
        self.staticPlotWidget.showGrid(x=True, y=True)
        self.staticLayout.addWidget(self.staticPlotWidget)
        self.staticCurve = pg.PlotDataItem(pen='b')
        self.staticPlotWidget.addItem(self.staticCurve)
        self.staticPlotWidget.setBackground('w')

        self.usespeedPlotWidget = pg.PlotWidget(title="Régime d'utilisation")
        self.usespeedPlotWidget.setXRange(0, 200)
        self.usespeedPlotWidget.setYRange(-400, 400)
        self.usespeedPlotWidget.setLabel("bottom", "Angle Rotation Came", units="°")
        self.usespeedPlotWidget.setLabel("left", "Pression de Hertz", units="MPa")
        self.usespeedPlotWidget.setAspectLocked(False)
        self.usespeedPlotWidget.showGrid(x=True, y=True)
        self.usespeedLayout.addWidget(self.usespeedPlotWidget)
        self.usespeedCurve = pg.PlotDataItem(pen='b')
        self.usespeedPlotWidget.addItem(self.usespeedCurve)
        self.usespeedPlotWidget.setBackground('w')

        self.floatspeedPlotWidget = pg.PlotWidget(title="Régime d'affolement")
        self.floatspeedPlotWidget.setXRange(0, 200)
        self.floatspeedPlotWidget.setYRange(0, 12)
        self.floatspeedPlotWidget.setLabel("bottom", "Angle Rotation Came", units="°")
        self.floatspeedPlotWidget.setLabel("left", "Pression de Hertz", units="MPa")
        self.floatspeedPlotWidget.setAspectLocked(False)
        self.floatspeedPlotWidget.showGrid(x=True, y=True)
        self.floatspeedLayout.addWidget(self.floatspeedPlotWidget)
        self.floatspeedCurve = pg.PlotDataItem(pen='b')
        self.floatspeedPlotWidget.addItem(self.floatspeedCurve)
        self.floatspeedPlotWidget.setBackground('w')

