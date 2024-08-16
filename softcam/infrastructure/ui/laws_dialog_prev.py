# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'laws_dialog_empty.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialogButtonBox,
    QFormLayout, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import pyqtgraph as pg

class Ui_LoisDialog(object):
    def setupUi(self, LoisDialog):
        if not LoisDialog.objectName():
            LoisDialog.setObjectName(u"LoisDialog")
        LoisDialog.resize(1146, 596)
        LoisDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dialogLayout = QVBoxLayout(LoisDialog)
        self.dialogLayout.setObjectName(u"dialogLayout")
        self.mainWidget = QWidget(LoisDialog)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainLayout = QHBoxLayout(self.mainWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.valuesWidget = QWidget(self.mainWidget)
        self.valuesWidget.setObjectName(u"valuesWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valuesWidget.sizePolicy().hasHeightForWidth())
        self.valuesWidget.setSizePolicy(sizePolicy)
        self.valuesWidget.setMaximumSize(QSize(16777215, 16777215))
        self.formLayout = QFormLayout(self.valuesWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.accelmaxLabel = QLabel(self.valuesWidget)
        self.accelmaxLabel.setObjectName(u"accelmaxLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.accelmaxLabel)

        self.accelmaxEdit = QLineEdit(self.valuesWidget)
        self.accelmaxEdit.setObjectName(u"accelmaxEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.accelmaxEdit.sizePolicy().hasHeightForWidth())
        self.accelmaxEdit.setSizePolicy(sizePolicy1)
        self.accelmaxEdit.setMinimumSize(QSize(50, 0))
        self.accelmaxEdit.setMaximumSize(QSize(60, 16777215))
        self.accelmaxEdit.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.accelmaxEdit)

        self.floatspeedEdit = QLineEdit(self.valuesWidget)
        self.floatspeedEdit.setObjectName(u"floatspeedEdit")
        self.floatspeedEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.floatspeedEdit.sizePolicy().hasHeightForWidth())
        self.floatspeedEdit.setSizePolicy(sizePolicy1)
        self.floatspeedEdit.setMinimumSize(QSize(50, 0))
        self.floatspeedEdit.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.floatspeedEdit)

        self.floatspeedLabel = QLabel(self.valuesWidget)
        self.floatspeedLabel.setObjectName(u"floatspeedLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.floatspeedLabel)

        self.symmetryLabel = QLabel(self.valuesWidget)
        self.symmetryLabel.setObjectName(u"symmetryLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.symmetryLabel)
        
        self.symmetryCheckBox = QCheckBox(self.valuesWidget)
        self.symmetryCheckBox.setObjectName(u"symmetryCheckBox")
        self.symmetryCheckBox.setChecked(True)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.symmetryCheckBox)

        self.itgstepLabel = QLabel(self.valuesWidget)
        self.itgstepLabel.setObjectName(u"itgstepLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.itgstepLabel)

        self.itgstepEdit = QLineEdit(self.valuesWidget)
        self.itgstepEdit.setObjectName(u"itgstepEdit")
        sizePolicy1.setHeightForWidth(self.itgstepEdit.sizePolicy().hasHeightForWidth())
        self.itgstepEdit.setSizePolicy(sizePolicy1)
        self.itgstepEdit.setMinimumSize(QSize(50, 0))
        self.itgstepEdit.setMaximumSize(QSize(60, 16777215))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.itgstepEdit)


        self.mainLayout.addWidget(self.valuesWidget, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.stackedWidget = QStackedWidget(self.mainWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.stackedWidget.setFrameShadow(QFrame.Sunken)
        self.accelPage = QWidget()
        self.accelPage.setObjectName(u"accelPage")
        sizePolicy2.setHeightForWidth(self.accelPage.sizePolicy().hasHeightForWidth())
        self.accelPage.setSizePolicy(sizePolicy2)
        self.accelLayout = QVBoxLayout(self.accelPage)
        self.accelLayout.setObjectName(u"accelLayout")
        self.accelLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.accelPage)
        self.speedPage = QWidget()
        self.speedPage.setObjectName(u"speedPage")
        sizePolicy2.setHeightForWidth(self.speedPage.sizePolicy().hasHeightForWidth())
        self.speedPage.setSizePolicy(sizePolicy2)
        self.speedLayout = QVBoxLayout(self.speedPage)
        self.speedLayout.setObjectName(u"speedLayout")
        self.speedLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.speedPage)
        self.liftPage = QWidget()
        self.liftPage.setObjectName(u"liftPage")
        sizePolicy2.setHeightForWidth(self.liftPage.sizePolicy().hasHeightForWidth())
        self.liftPage.setSizePolicy(sizePolicy2)
        self.liftLayout = QVBoxLayout(self.liftPage)
        self.liftLayout.setObjectName(u"liftLayout")
        self.liftLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.liftPage)

        self.mainLayout.addWidget(self.stackedWidget)


        self.dialogLayout.addWidget(self.mainWidget)

        self.buttonsWidget = QWidget(LoisDialog)
        self.buttonsWidget.setObjectName(u"buttonsWidget")
        self.horizontalLayout = QHBoxLayout(self.buttonsWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonBox = QDialogButtonBox(self.buttonsWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.accelButton = QPushButton(self.buttonsWidget)
        self.accelButton.setObjectName(u"accelButton")

        self.horizontalLayout.addWidget(self.accelButton)

        self.speedButton = QPushButton(self.buttonsWidget)
        self.speedButton.setObjectName(u"speedButton")

        self.horizontalLayout.addWidget(self.speedButton)

        self.liftButton = QPushButton(self.buttonsWidget)
        self.liftButton.setObjectName(u"liftButton")

        self.horizontalLayout.addWidget(self.liftButton)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.optimisationButton = QPushButton(self.buttonsWidget)
        self.optimisationButton.setObjectName(u"optimisationButton")

        self.horizontalLayout.addWidget(self.optimisationButton)

        self.horizontalSpacer_1 = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_1)

        self.resetviewButton = QPushButton(self.buttonsWidget)
        self.resetviewButton.setObjectName(u"resetviewButton")

        self.horizontalLayout.addWidget(self.resetviewButton)


        self.dialogLayout.addWidget(self.buttonsWidget)


        self.retranslateUi(LoisDialog)
        self.populateUi()
        self.buttonBox.accepted.connect(LoisDialog.accept)
        self.buttonBox.rejected.connect(LoisDialog.reject)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LoisDialog)
    # setupUi

    def retranslateUi(self, LoisDialog):
        LoisDialog.setWindowTitle(QCoreApplication.translate("LoisDialog", u"Définition des Lois", None))
        self.accelmaxLabel.setText(QCoreApplication.translate("LoisDialog", u"<html><head/><body><p>Acc\u00e9l\u00e9ration <br/> maximale <br/> (&mu;m/\u00b0\u00b2 )</p></body></html>", None))
        self.accelmaxEdit.setText(QCoreApplication.translate("LoisDialog", u"7500", None))
        self.floatspeedEdit.setText(QCoreApplication.translate("LoisDialog", u"12000", None))
        self.floatspeedLabel.setText(QCoreApplication.translate("LoisDialog", u"<html><head/><body><p>Affolement <br/>(tr/min)</p></body></html>", None))
        self.symmetryLabel.setText(QCoreApplication.translate("LoisDialog", u"Sym\u00e9trique", None))
        self.symmetryCheckBox.setText("")
        self.itgstepLabel.setText(QCoreApplication.translate("LoisDialog", u"<html><head/><body>Int\u00e9gration <br/> Pas (\u00b0)</body></html>", None))
        self.itgstepEdit.setText(QCoreApplication.translate("LoisDialog", u"0.1", None))
        self.accelButton.setText(QCoreApplication.translate("LoisDialog", u"Acc\u00e9l\u00e9ration", None))
        self.speedButton.setText(QCoreApplication.translate("LoisDialog", u"Vitesse", None))
        self.liftButton.setText(QCoreApplication.translate("LoisDialog", u"Lev\u00e9e", None))
        self.optimisationButton.setText(QCoreApplication.translate("LoisDialog", u"Optimisation", None))
        self.resetviewButton.setText(QCoreApplication.translate("LoisDialog", u"Reset View", None))
    # retranslateUi

    def populateUi(self):

        self.accelPlotWidget = pg.PlotWidget(title="Accélération")
        self.accelPlotWidget.setXRange(0, 200)
        self.accelPlotWidget.setYRange(-10, 40)
        self.accelPlotWidget.setLabel("bottom", "Angle de Rotation de la Came", units="<math> &deg; </math>")
        self.accelPlotWidget.setLabel("left", "Accélération", units="<math> &mu;m / &deg;<sup>2</sup> </math>")
        self.accelPlotWidget.setAspectLocked(False)
        self.accelPlotWidget.showGrid(x=True, y=True)
        self.accelLayout.addWidget(self.accelPlotWidget)
        self.openaccelScatterPlot = pg.ScatterPlotItem(pen=pg.mkPen(None), symbol='o', size=10, brush='r')
        self.closeaccelScatterPlot = pg.ScatterPlotItem(pen=pg.mkPen(None), symbol='o', size=10, brush='g')
        self.openaccelCurve = pg.PlotDataItem(pen='black')
        self.closeaccelCurve = pg.PlotDataItem(pen='black')
        self.accelCurve = pg.PlotDataItem(pen='b')
        self.openaccelCurve.setX(0)
        self.openaccelCurve.setY(0)
        self.accelPlotWidget.addItem(self.openaccelScatterPlot)
        self.accelPlotWidget.addItem(self.closeaccelScatterPlot)
        self.accelPlotWidget.addItem(self.openaccelCurve)
        self.accelPlotWidget.addItem(self.closeaccelCurve)
        self.accelPlotWidget.addItem(self.accelCurve)
        self.accelPlotWidget.setBackground('w')

        self.speedPlotWidget = pg.PlotWidget(title="Vitesse")
        self.speedPlotWidget.setXRange(0, 200)
        self.speedPlotWidget.setYRange(-400, 400)
        self.speedPlotWidget.setLabel("bottom", "Angle de Rotation de la Came", units="<math> &deg; </math>")
        self.speedPlotWidget.setLabel("left", "Vitesse", units = "<math>&mu;m / &deg;</math>")
        self.speedPlotWidget.setAspectLocked(False)
        self.speedPlotWidget.showGrid(x=True, y=True)
        self.speedLayout.addWidget(self.speedPlotWidget)
        self.openspeedScatterPlot = pg.ScatterPlotItem(pen=pg.mkPen(None), symbol='o', size=10, brush='r')
        self.closespeedScatterPlot = pg.ScatterPlotItem(pen=pg.mkPen(None), symbol='o', size=10, brush='g')
        self.openspeedCurve = pg.PlotDataItem(pen='black')
        self.closespeedCurve = pg.PlotDataItem(pen='black')
        self.speedCurve = pg.PlotDataItem(pen='b')
        self.speedPlotWidget.addItem(self.openspeedScatterPlot)
        self.speedPlotWidget.addItem(self.closespeedScatterPlot)
        self.speedPlotWidget.addItem(self.openspeedCurve)
        self.speedPlotWidget.addItem(self.closespeedCurve)
        self.speedPlotWidget.addItem(self.speedCurve)
        self.speedPlotWidget.setBackground('w')

        self.liftPlotWidget = pg.PlotWidget(title="Levee")
        self.liftPlotWidget.setXRange(0, 200)
        self.liftPlotWidget.setYRange(0, 12)
        self.liftPlotWidget.setLabel("bottom", "Angle de Rotation de la Came", units="<math> &deg; </math>")
        self.liftPlotWidget.setLabel("left", "Levée", units="<math> mm </math>")
        self.liftPlotWidget.setAspectLocked(False)
        self.liftPlotWidget.showGrid(x=True, y=True)
        self.liftLayout.addWidget(self.liftPlotWidget)
        self.openliftScatterPlot = pg.ScatterPlotItem(pen=pg.mkPen(None), symbol='o', size=10, brush='r')
        self.closeliftScatterPlot = pg.ScatterPlotItem(pen=pg.mkPen(None), symbol='o', size=10, brush='g')
        self.openliftCurve = pg.PlotDataItem(pen='black')
        self.closeliftCurve = pg.PlotDataItem(pen='black')
        self.liftCurve = pg.PlotDataItem(pen='b')
        self.liftPlotWidget.addItem(self.openliftScatterPlot)
        self.liftPlotWidget.addItem(self.closeliftScatterPlot)
        self.liftPlotWidget.addItem(self.openliftCurve)
        self.liftPlotWidget.addItem(self.closeliftCurve)
        self.liftPlotWidget.addItem(self.liftCurve)
        self.liftPlotWidget.setBackground('w')
    
class Ui_PointDialog(object):
    def setupUi(self, PointDialog):
        layout = QFormLayout(self)

        self.x_input = QLineEdit(str(self.point.pos()[0]))
        self.y_input = QLineEdit(str(self.point.pos()[1]))
        self.z_input = QLineEdit(str(self.weight))

        layout.addRow("Abscisse :", self.x_input)
        layout.addRow("Ordonnée:", self.y_input)
        layout.addRow("Poids:", self.z_input)

        buttonBox = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        buttonBox.addWidget(self.ok_button)
        buttonBox.addWidget(self.cancel_button)

        layout.addRow(buttonBox)

