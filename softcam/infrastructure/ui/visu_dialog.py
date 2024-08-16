# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'visu_dialog_empty.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import pyqtgraph as pg

class Ui_VisuDialog(object):
    def setupUi(self, VisuDialog):
        if not VisuDialog.objectName():
            VisuDialog.setObjectName(u"VisuDialog")
        VisuDialog.resize(1146, 596)
        VisuDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dialogLayout = QVBoxLayout(VisuDialog)
        self.dialogLayout.setObjectName(u"dialogLayout")
        self.mainWidget = QWidget(VisuDialog)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainLayout = QHBoxLayout(self.mainWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.stackedWidget = QStackedWidget(self.mainWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.stackedWidget.setFrameShadow(QFrame.Sunken)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        sizePolicy.setHeightForWidth(self.profilePage.sizePolicy().hasHeightForWidth())
        self.profilePage.setSizePolicy(sizePolicy)
        self.profileLayout = QVBoxLayout(self.profilePage)
        self.profileLayout.setObjectName(u"profileLayout")
        self.profileLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.profilePage)
        self.curvaturePage = QWidget()
        self.curvaturePage.setObjectName(u"curvaturePage")
        sizePolicy.setHeightForWidth(self.curvaturePage.sizePolicy().hasHeightForWidth())
        self.curvaturePage.setSizePolicy(sizePolicy)
        self.curvatureLayout = QVBoxLayout(self.curvaturePage)
        self.curvatureLayout.setObjectName(u"curvatureLayout")
        self.curvatureLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.curvaturePage)
        self.kinematicsPage = QWidget()
        self.kinematicsPage.setObjectName(u"kinematicsPage")
        sizePolicy.setHeightForWidth(self.kinematicsPage.sizePolicy().hasHeightForWidth())
        self.kinematicsPage.setSizePolicy(sizePolicy)
        self.kinematicsLayout = QVBoxLayout(self.kinematicsPage)
        self.kinematicsLayout.setObjectName(u"kinematicsLayout")
        self.kinematicsLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.kinematicsPage)

        self.mainLayout.addWidget(self.stackedWidget)


        self.dialogLayout.addWidget(self.mainWidget)

        self.buttonsWidget = QWidget(VisuDialog)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.buttonsLayout = QHBoxLayout(self.buttonsWidget)
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.displayButton = QPushButton(self.buttonsWidget)
        self.displayButton.setObjectName(u"displayButton")

        self.buttonsLayout.addWidget(self.displayButton)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_4)

        self.precisionLabel = QLabel(self.buttonsWidget)
        self.precisionLabel.setObjectName(u"precisionLabel")

        self.buttonsLayout.addWidget(self.precisionLabel)

        self.precisionEdit = QLineEdit(self.buttonsWidget)
        self.precisionEdit.setObjectName(u"precisionEdit")
        self.precisionEdit.setMinimumSize(QSize(30, 0))
        self.precisionEdit.setMaximumSize(QSize(40, 16777215))

        self.buttonsLayout.addWidget(self.precisionEdit)

        self.precisionUnitLabel = QLabel(self.buttonsWidget)
        self.precisionUnitLabel.setObjectName(u"precisionUnitLabel")

        self.buttonsLayout.addWidget(self.precisionUnitLabel)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer)

        self.profileButton = QPushButton(self.buttonsWidget)
        self.profileButton.setObjectName(u"profileButton")

        self.buttonsLayout.addWidget(self.profileButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_3)

        self.curvatureButton = QPushButton(self.buttonsWidget)
        self.curvatureButton.setObjectName(u"curvatureButton")

        self.buttonsLayout.addWidget(self.curvatureButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_2)

        self.kinematicsButton = QPushButton(self.buttonsWidget)
        self.kinematicsButton.setObjectName(u"kinematicsButton")

        self.buttonsLayout.addWidget(self.kinematicsButton)

        self.horizontalSpacer_1 = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_1)

        self.resetviewButton = QPushButton(self.buttonsWidget)
        self.resetviewButton.setObjectName(u"resetviewButton")

        self.buttonsLayout.addWidget(self.resetviewButton)


        self.dialogLayout.addWidget(self.buttonsWidget)


        self.retranslateUi(VisuDialog)
        self.populateUi()
        
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VisuDialog)
    # setupUi

    def retranslateUi(self, VisuDialog):
        VisuDialog.setWindowTitle(QCoreApplication.translate("VisuDialog", u"Visualisation ", None))
        self.displayButton.setText(QCoreApplication.translate("VisuDialog", u"Affichage", None))
        self.precisionLabel.setText(QCoreApplication.translate("VisuDialog", u"Pr\u00e9cision", None))
        self.precisionEdit.setText(QCoreApplication.translate("VisuDialog", u"0.1", None))
        self.precisionUnitLabel.setText(QCoreApplication.translate("VisuDialog", u"\u00b0", None))
        self.profileButton.setText(QCoreApplication.translate("VisuDialog", u"Profil Came", None))
        self.curvatureButton.setText(QCoreApplication.translate("VisuDialog", u"Rayon de Coubure Came", None))
        self.kinematicsButton.setText(QCoreApplication.translate("VisuDialog", u"Cinematique Syst\u00e8me", None))
        self.resetviewButton.setText(QCoreApplication.translate("VisuDialog", u"Reset View", None))
    # retranslateUi

    def populateUi(self):

        self.profilePlotWidget = pg.PlotWidget(title="Profil de Came")
        self.profilePlotWidget.setAspectLocked(True)
        self.profilePlotWidget.showGrid(x=True, y=True)
        self.profileLayout.addWidget(self.profilePlotWidget)
        self.profileCurve = pg.PlotDataItem(pen='b')
        self.basecircleCurve = pg.PlotDataItem(pen=pg.mkPen(color='g', style=pg.QtCore.Qt.DashLine))
        self.profileCurve.setX(0)
        self.profileCurve.setY(0)
        self.profilePlotWidget.addItem(self.profileCurve)
        self.profilePlotWidget.addItem(self.basecircleCurve)
        self.profilePlotWidget.setBackground('w')

        self.curvaturePlotWidget = pg.PlotWidget(title="Rayon de Courbure")
        self.curvaturePlotWidget.setXRange(0, 180)
        self.curvaturePlotWidget.setYRange(-400, 400)
        self.curvaturePlotWidget.setLabel("bottom", "Angle Polaire", units="deg")
        self.curvaturePlotWidget.setLabel("left", "Rayon de Courbure", units="mm")
        self.curvaturePlotWidget.setAspectLocked(False)
        self.curvaturePlotWidget.showGrid(x=True, y=True)
        self.curvatureLayout.addWidget(self.curvaturePlotWidget)
        self.curvatureCurve = pg.PlotDataItem(pen='b')
        self.curvaturePlotWidget.addItem(self.curvatureCurve)
        self.curvaturePlotWidget.setBackground('w')

        self.kinematicsPlotWidget = pg.PlotWidget(title="Animation Cinématique")
        self.kinematicsPlotWidget.setAspectLocked(True)
        self.kinematicsLayout.addWidget(self.kinematicsPlotWidget)
        self.kinematicsCurve = pg.PlotDataItem(pen='b')
        self.kinematicsPlotWidget.addItem(self.kinematicsCurve)
        self.kinematicsPlotWidget.setBackground('w')

