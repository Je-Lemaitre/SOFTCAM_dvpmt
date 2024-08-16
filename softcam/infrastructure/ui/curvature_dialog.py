# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'curvature_dialog_empty.ui'
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

class Ui_CurvatureDialog(object):
    def setupUi(self, CurvatureDialog):
        if not CurvatureDialog.objectName():
            CurvatureDialog.setObjectName(u"CurvatureDialog")
        CurvatureDialog.resize(1146, 596)
        CurvatureDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dialogLayout = QVBoxLayout(CurvatureDialog)
        self.dialogLayout.setObjectName(u"dialogLayout")
        self.mainWidget = QWidget(CurvatureDialog)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainLayout = QHBoxLayout(self.mainWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.parametersWidget = QWidget(self.mainWidget)
        self.parametersWidget.setObjectName(u"parametersWidget")
        self.parametersLayout = QVBoxLayout(self.parametersWidget)
        self.parametersLayout.setObjectName(u"parametersLayout")
        self.parametersLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.parametersLayout.addItem(self.verticalSpacer_2)

        self.limitradiusLabel = QLabel(self.parametersWidget)
        self.limitradiusLabel.setObjectName(u"limitradiusLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.limitradiusLabel.sizePolicy().hasHeightForWidth())
        self.limitradiusLabel.setSizePolicy(sizePolicy)

        self.parametersLayout.addWidget(self.limitradiusLabel)

        self.limitradiusEdit = QLineEdit(self.parametersWidget)
        self.limitradiusEdit.setObjectName(u"limitradiusEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.limitradiusEdit.sizePolicy().hasHeightForWidth())
        self.limitradiusEdit.setSizePolicy(sizePolicy1)
        self.limitradiusEdit.setMaximumSize(QSize(70, 16777215))
        self.limitradiusEdit.setSizeIncrement(QSize(0, 0))

        self.parametersLayout.addWidget(self.limitradiusEdit, 0, Qt.AlignHCenter)

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
        self.curvaturePage = QWidget()
        self.curvaturePage.setObjectName(u"curvaturePage")
        sizePolicy3.setHeightForWidth(self.curvaturePage.sizePolicy().hasHeightForWidth())
        self.curvaturePage.setSizePolicy(sizePolicy3)
        self.curvatureLayout = QVBoxLayout(self.curvaturePage)
        self.curvatureLayout.setObjectName(u"curvatureLayout")
        self.curvatureLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.curvaturePage)

        self.mainLayout.addWidget(self.stackedWidget)


        self.dialogLayout.addWidget(self.mainWidget)

        self.buttonsWidget = QWidget(CurvatureDialog)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.buttonsLayout = QHBoxLayout(self.buttonsWidget)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonBox = QDialogButtonBox(self.buttonsWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.buttonsLayout.addWidget(self.buttonBox)

        self.horizontalSpacer_4 = QSpacerItem(1000, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_4)

        self.computeButton = QPushButton(self.buttonsWidget)
        self.computeButton.setObjectName(u"computeButton")

        self.buttonsLayout.addWidget(self.computeButton)

        self.horizontalSpacer_1 = QSpacerItem(1000, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_1)

        self.resetviewButton = QPushButton(self.buttonsWidget)
        self.resetviewButton.setObjectName(u"resetviewButton")

        self.buttonsLayout.addWidget(self.resetviewButton)


        self.dialogLayout.addWidget(self.buttonsWidget)


        self.retranslateUi(CurvatureDialog)
        self.populateUi()
        self.buttonBox.accepted.connect(CurvatureDialog.accept)
        self.buttonBox.rejected.connect(CurvatureDialog.reject)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CurvatureDialog)
    # setupUi

    def retranslateUi(self, CurvatureDialog):
        CurvatureDialog.setWindowTitle(QCoreApplication.translate("CurvatureDialog", u"Rayon de Courbure", None))
        self.limitradiusLabel.setText(QCoreApplication.translate("CurvatureDialog", u"<html><head/><body><p align=\"center\">Diam\u00e8tre Meule <br/> de Taillage <br/>(mm) </p></body></html>", None))
        self.infoLabel.setText(QCoreApplication.translate("CurvatureDialog", u"<html><head/><body><p align=\"center\">Informations</p></body></html>", None))
        self.infoButton.setText("")
        self.computeButton.setText(QCoreApplication.translate("CurvatureDialog", u"Calcul", None))
        self.resetviewButton.setText(QCoreApplication.translate("CurvatureDialog", u"Reset View", None))
    # retranslateUi

    def populateUi(self):
        self.curvaturePlotWidget = pg.PlotWidget(title="Rayon de Courbure de la Came en Fonction de son Angle Polaire")
        self.curvaturePlotWidget.setXRange(0, 200)
        self.curvaturePlotWidget.setYRange(-200, 200)
        self.curvaturePlotWidget.setLabel("bottom", "Angle Polaire", units="°")
        self.curvaturePlotWidget.setLabel("left", "Rayon de Courbure", units="mm")
        self.curvaturePlotWidget.setAspectLocked(False)
        self.curvaturePlotWidget.showGrid(x=True, y=True)
        self.curvatureLayout.addWidget(self.curvaturePlotWidget)
        self.curvatureCurve = pg.PlotDataItem(pen='b')
        self.curvaturePlotWidget.addItem(self.curvatureCurve)
        self.curvaturePlotWidget.setBackground('w')


