# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rockerarm_asmb_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import infrastructure.ui.resources.resources_rc

class Ui_RockerArmAssemblyDialog(object):
    def setupUi(self, RockerArmAssemblyDialog):
        if not RockerArmAssemblyDialog.objectName():
            RockerArmAssemblyDialog.setObjectName(u"RockerArmAssemblyDialog")
        RockerArmAssemblyDialog.resize(1366, 705)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RockerArmAssemblyDialog.sizePolicy().hasHeightForWidth())
        RockerArmAssemblyDialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setHintingPreference(QFont.PreferFullHinting)
        RockerArmAssemblyDialog.setFont(font)
        RockerArmAssemblyDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        RockerArmAssemblyDialog.setSizeGripEnabled(False)
        RockerArmAssemblyDialog.setModal(False)
        self.mainLayout = QHBoxLayout(RockerArmAssemblyDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.definitionWidget = QWidget(RockerArmAssemblyDialog)
        self.definitionWidget.setObjectName(u"definitionWidget")
        self.verticalLayout = QVBoxLayout(self.definitionWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.partsFrame = QFrame(self.definitionWidget)
        self.partsFrame.setObjectName(u"partsFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.partsFrame.sizePolicy().hasHeightForWidth())
        self.partsFrame.setSizePolicy(sizePolicy1)
        self.partsLayout = QVBoxLayout(self.partsFrame)
        self.partsLayout.setSpacing(20)
        self.partsLayout.setObjectName(u"partsLayout")
        self.partsLayout.setContentsMargins(3, 3, 3, 20)
        self.partsLabel = QLabel(self.partsFrame)
        self.partsLabel.setObjectName(u"partsLabel")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.partsLabel.setFont(font1)

        self.partsLayout.addWidget(self.partsLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.valveButton = QPushButton(self.partsFrame)
        self.valveButton.setObjectName(u"valveButton")
        sizePolicy.setHeightForWidth(self.valveButton.sizePolicy().hasHeightForWidth())
        self.valveButton.setSizePolicy(sizePolicy)

        self.partsLayout.addWidget(self.valveButton, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.springButton = QPushButton(self.partsFrame)
        self.springButton.setObjectName(u"springButton")
        sizePolicy.setHeightForWidth(self.springButton.sizePolicy().hasHeightForWidth())
        self.springButton.setSizePolicy(sizePolicy)

        self.partsLayout.addWidget(self.springButton, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.rockerarmButton = QPushButton(self.partsFrame)
        self.rockerarmButton.setObjectName(u"rockerarmButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.rockerarmButton.sizePolicy().hasHeightForWidth())
        self.rockerarmButton.setSizePolicy(sizePolicy2)
        self.rockerarmButton.setMaximumSize(QSize(16777215, 16777215))

        self.partsLayout.addWidget(self.rockerarmButton, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.camButton = QPushButton(self.partsFrame)
        self.camButton.setObjectName(u"camButton")
        sizePolicy.setHeightForWidth(self.camButton.sizePolicy().hasHeightForWidth())
        self.camButton.setSizePolicy(sizePolicy)

        self.partsLayout.addWidget(self.camButton, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout.addWidget(self.partsFrame)

        self.definitionSpacer1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.definitionSpacer1)

        self.asmbValuesFrame = QFrame(self.definitionWidget)
        self.asmbValuesFrame.setObjectName(u"asmbValuesFrame")
        sizePolicy.setHeightForWidth(self.asmbValuesFrame.sizePolicy().hasHeightForWidth())
        self.asmbValuesFrame.setSizePolicy(sizePolicy)
        self.asmbValuesLayout = QVBoxLayout(self.asmbValuesFrame)
        self.asmbValuesLayout.setSpacing(10)
        self.asmbValuesLayout.setObjectName(u"asmbValuesLayout")
        self.asmbValuesLayout.setContentsMargins(3, 20, 3, 3)
        self.asmbValuesLabel = QLabel(self.asmbValuesFrame)
        self.asmbValuesLabel.setObjectName(u"asmbValuesLabel")
        self.asmbValuesLabel.setFont(font1)

        self.asmbValuesLayout.addWidget(self.asmbValuesLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.sensrotWidget = QWidget(self.asmbValuesFrame)
        self.sensrotWidget.setObjectName(u"sensrotWidget")
        self.sensrotLayout = QHBoxLayout(self.sensrotWidget)
        self.sensrotLayout.setObjectName(u"sensrotLayout")
        self.sensrotLabel = QLabel(self.sensrotWidget)
        self.sensrotLabel.setObjectName(u"sensrotLabel")

        self.sensrotLayout.addWidget(self.sensrotLabel)

        self.sensrotComboBox = QComboBox(self.sensrotWidget)
        self.sensrotComboBox.addItem("")
        self.sensrotComboBox.addItem("")
        self.sensrotComboBox.setObjectName(u"sensrotComboBox")

        self.sensrotLayout.addWidget(self.sensrotComboBox)


        self.asmbValuesLayout.addWidget(self.sensrotWidget, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.ylWidget = QWidget(self.asmbValuesFrame)
        self.ylWidget.setObjectName(u"ylWidget")
        self.ylLayout = QHBoxLayout(self.ylWidget)
        self.ylLayout.setObjectName(u"ylLayout")
        self.ylEdit = QLineEdit(self.ylWidget)
        self.ylEdit.setObjectName(u"ylEdit")

        self.ylLayout.addWidget(self.ylEdit, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.ylUnitLabel = QLabel(self.ylWidget)
        self.ylUnitLabel.setObjectName(u"ylUnitLabel")

        self.ylLayout.addWidget(self.ylUnitLabel, 0, Qt.AlignLeft)


        self.asmbValuesLayout.addWidget(self.ylWidget, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.zlWidget = QWidget(self.asmbValuesFrame)
        self.zlWidget.setObjectName(u"zlWidget")
        self.zlLayout = QHBoxLayout(self.zlWidget)
        self.zlLayout.setObjectName(u"zlLayout")
        self.zlEdit = QLineEdit(self.zlWidget)
        self.zlEdit.setObjectName(u"zlEdit")

        self.zlLayout.addWidget(self.zlEdit)

        self.zlUnitLabel = QLabel(self.zlWidget)
        self.zlUnitLabel.setObjectName(u"zlUnitLabel")

        self.zlLayout.addWidget(self.zlUnitLabel)


        self.asmbValuesLayout.addWidget(self.zlWidget, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.ycWidget = QWidget(self.asmbValuesFrame)
        self.ycWidget.setObjectName(u"ycWidget")
        self.ycLayout = QHBoxLayout(self.ycWidget)
        self.ycLayout.setObjectName(u"ycLayout")
        self.ycEdit = QLineEdit(self.ycWidget)
        self.ycEdit.setObjectName(u"ycEdit")

        self.ycLayout.addWidget(self.ycEdit)

        self.ycUnitLabel = QLabel(self.ycWidget)
        self.ycUnitLabel.setObjectName(u"ycUnitLabel")

        self.ycLayout.addWidget(self.ycUnitLabel)


        self.asmbValuesLayout.addWidget(self.ycWidget, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.zcWidget = QWidget(self.asmbValuesFrame)
        self.zcWidget.setObjectName(u"zcWidget")
        self.zcLayout = QHBoxLayout(self.zcWidget)
        self.zcLayout.setObjectName(u"zcLayout")
        self.zcEdit = QLineEdit(self.zcWidget)
        self.zcEdit.setObjectName(u"zcEdit")

        self.zcLayout.addWidget(self.zcEdit)

        self.zcUnitLabel = QLabel(self.zcWidget)
        self.zcUnitLabel.setObjectName(u"zcUnitLabel")

        self.zcLayout.addWidget(self.zcUnitLabel)


        self.asmbValuesLayout.addWidget(self.zcWidget, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.gammaWidget = QWidget(self.asmbValuesFrame)
        self.gammaWidget.setObjectName(u"gammaWidget")
        self.gammaLayout = QHBoxLayout(self.gammaWidget)
        self.gammaLayout.setObjectName(u"gammaLayout")
        self.gammaEdit = QLineEdit(self.gammaWidget)
        self.gammaEdit.setObjectName(u"gammaEdit")

        self.gammaLayout.addWidget(self.gammaEdit)

        self.gammaUnitLabel = QLabel(self.gammaWidget)
        self.gammaUnitLabel.setObjectName(u"gammaUnitLabel")

        self.gammaLayout.addWidget(self.gammaUnitLabel)


        self.asmbValuesLayout.addWidget(self.gammaWidget, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.alphaWidget = QWidget(self.asmbValuesFrame)
        self.alphaWidget.setObjectName(u"alphaWidget")
        self.alphaLayout = QHBoxLayout(self.alphaWidget)
        self.alphaLayout.setObjectName(u"alphaLayout")
        self.alphaEdit = QLineEdit(self.alphaWidget)
        self.alphaEdit.setObjectName(u"alphaEdit")

        self.alphaLayout.addWidget(self.alphaEdit)

        self.alphaUnitLabel = QLabel(self.alphaWidget)
        self.alphaUnitLabel.setObjectName(u"alphaUnitLabel")

        self.alphaLayout.addWidget(self.alphaUnitLabel)


        self.asmbValuesLayout.addWidget(self.alphaWidget, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout.addWidget(self.asmbValuesFrame)

        self.definitionSpacer2 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.definitionSpacer2)

        self.buttonBox = QDialogButtonBox(self.definitionWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.mainLayout.addWidget(self.definitionWidget, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.kinematicSchemeFrame = QFrame(RockerArmAssemblyDialog)
        self.kinematicSchemeFrame.setObjectName(u"kinematicSchemeFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.kinematicSchemeFrame.sizePolicy().hasHeightForWidth())
        self.kinematicSchemeFrame.setSizePolicy(sizePolicy3)
        self.kinematicSchemeFrame.setFrameShape(QFrame.StyledPanel)
        self.kinematicSchemeFrame.setFrameShadow(QFrame.Raised)
        self.kinematicSchemeLayout = QGridLayout(self.kinematicSchemeFrame)
        self.kinematicSchemeLayout.setSpacing(0)
        self.kinematicSchemeLayout.setObjectName(u"kinematicSchemeLayout")
        self.kinematicSchemeLayout.setContentsMargins(3, 3, 3, 3)

        self.mainLayout.addWidget(self.kinematicSchemeFrame)


        self.retranslateUi(RockerArmAssemblyDialog)
        self.buttonBox.accepted.connect(RockerArmAssemblyDialog.accept)
        self.buttonBox.rejected.connect(RockerArmAssemblyDialog.reject)

        QMetaObject.connectSlotsByName(RockerArmAssemblyDialog)
    # setupUi

    def retranslateUi(self, RockerArmAssemblyDialog):
        RockerArmAssemblyDialog.setWindowTitle(QCoreApplication.translate("RockerArmAssemblyDialog", u"Syst\u00e8me \u00e0 Linguet", None))
        self.partsLabel.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"D\u00e9finition des pi\u00e8ces", None))
        self.valveButton.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"Soupape", None))
        self.springButton.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"Ressort", None))
        self.rockerarmButton.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"Linguet", None))
        self.camButton.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"Came", None))
        self.asmbValuesLabel.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"D\u00e9finition de l'assemblage", None))
        self.sensrotLabel.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"Sens de rotation", None))
        self.sensrotComboBox.setItemText(0, QCoreApplication.translate("RockerArmAssemblyDialog", u"Horaire", None))
        self.sensrotComboBox.setItemText(1, QCoreApplication.translate("RockerArmAssemblyDialog", u"Anti-horaire", None))

        self.ylEdit.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"35.66", None))
        self.ylUnitLabel.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"mm", None))
        self.zlEdit.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"5.412", None))
        self.zlUnitLabel.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"mm", None))
        self.ycEdit.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"14.21", None))
        self.ycUnitLabel.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"mm", None))
        self.zcEdit.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"31.712", None))
        self.zcUnitLabel.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"mm", None))
        self.gammaEdit.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"84.689", None))
        self.gammaUnitLabel.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"deg", None))
        self.alphaEdit.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"0", None))
        self.alphaUnitLabel.setText(QCoreApplication.translate("RockerArmAssemblyDialog", u"deg", None))
    # retranslateUi

