# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'force_dialog_empty.ui'
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

class Ui_ForceDialog(object):
    def setupUi(self, ForceDialog):
        if not ForceDialog.objectName():
            ForceDialog.setObjectName(u"ForceDialog")
        ForceDialog.resize(1146, 596)
        ForceDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dialogLayout = QVBoxLayout(ForceDialog)
        self.dialogLayout.setObjectName(u"dialogLayout")
        self.mainWidget = QWidget(ForceDialog)
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

        self.limitforceLabel = QLabel(self.parametersWidget)
        self.limitforceLabel.setObjectName(u"limitforceLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.limitforceLabel.sizePolicy().hasHeightForWidth())
        self.limitforceLabel.setSizePolicy(sizePolicy1)

        self.parametersLayout.addWidget(self.limitforceLabel)

        self.limitforceEdit = QLineEdit(self.parametersWidget)
        self.limitforceEdit.setObjectName(u"limitforceEdit")
        sizePolicy.setHeightForWidth(self.limitforceEdit.sizePolicy().hasHeightForWidth())
        self.limitforceEdit.setSizePolicy(sizePolicy)
        self.limitforceEdit.setMaximumSize(QSize(70, 16777215))
        self.limitforceEdit.setSizeIncrement(QSize(0, 0))

        self.parametersLayout.addWidget(self.limitforceEdit, 0, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.parametersLayout.addItem(self.verticalSpacer_5)

        self.speedLabel = QLabel(self.parametersWidget)
        self.speedLabel.setObjectName(u"speedLabel")

        self.parametersLayout.addWidget(self.speedLabel)

        self.speedComboBox = QComboBox(self.parametersWidget)
        self.speedComboBox.addItem("")
        self.speedComboBox.addItem("")
        self.speedComboBox.addItem("")
        self.speedComboBox.addItem("")
        self.speedComboBox.setObjectName(u"speedComboBox")

        self.parametersLayout.addWidget(self.speedComboBox)

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
        self.torquePage = QWidget()
        self.torquePage.setObjectName(u"torquePage")
        self.torqueLayout = QVBoxLayout(self.torquePage)
        self.torqueLayout.setObjectName(u"torqueLayout")
        self.torqueLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.torquePage)

        self.mainLayout.addWidget(self.stackedWidget)


        self.dialogLayout.addWidget(self.mainWidget)

        self.buttonsWidget = QWidget(ForceDialog)
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

        self.torqueButton = QPushButton(self.buttonsWidget)
        self.torqueButton.setObjectName(u"torqueButton")

        self.buttonsLayout.addWidget(self.torqueButton)

        self.horizontalSpacer_1 = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_1)

        self.resetviewButton = QPushButton(self.buttonsWidget)
        self.resetviewButton.setObjectName(u"resetviewButton")

        self.buttonsLayout.addWidget(self.resetviewButton)


        self.dialogLayout.addWidget(self.buttonsWidget)


        self.retranslateUi(ForceDialog)
        self.buttonBox.accepted.connect(ForceDialog.accept)
        self.buttonBox.rejected.connect(ForceDialog.reject)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(ForceDialog)
    # setupUi

    def retranslateUi(self, ForceDialog):
        ForceDialog.setWindowTitle(QCoreApplication.translate("ForceDialog", u"Efforts de Liaison", None))
        self.floatspeedLabel.setText(QCoreApplication.translate("ForceDialog", u"<html><head/><body><p align=\"center\">Affolement <br/>(tr/min)</p></body></html>", None))
        self.usespeedLabel.setText(QCoreApplication.translate("ForceDialog", u"<html><head/><body><p align=\"center\">Regime Utilisation <br/>(tr/min) </p></body></html>", None))
        self.limitforceLabel.setText(QCoreApplication.translate("ForceDialog", u"<html><head/><body><p align=\"center\">Effort Limite <br/>(N) </p></body></html>", None))
        self.speedLabel.setText(QCoreApplication.translate("ForceDialog", u"<html><head/><body><p align=\"center\">Regime</p></body></html>", None))
        self.speedComboBox.setItemText(0, QCoreApplication.translate("ForceDialog", u"Tous", None))
        self.speedComboBox.setItemText(1, QCoreApplication.translate("ForceDialog", u"Statique", None))
        self.speedComboBox.setItemText(2, QCoreApplication.translate("ForceDialog", u"Utilisation", None))
        self.speedComboBox.setItemText(3, QCoreApplication.translate("ForceDialog", u"Affolement", None))

        self.infoLabel.setText(QCoreApplication.translate("ForceDialog", u"<html><head/><body><p align=\"center\">Informations</p></body></html>", None))
        self.infoButton.setText("")
        self.computeButton.setText(QCoreApplication.translate("ForceDialog", u"Calcul", None))
        self.camrockerarmButton.setText(QCoreApplication.translate("ForceDialog", u"Came / Patin", None))
        self.valverockerarmButton.setText(QCoreApplication.translate("ForceDialog", u"Soupape / Patin", None))
        self.camvalveButton.setText(QCoreApplication.translate("ForceDialog", u"Came / Soupape", None))
        self.torqueButton.setText(QCoreApplication.translate("ForceDialog", u"Couple Arbre", None))
        self.resetviewButton.setText(QCoreApplication.translate("ForceDialog", u"Reset View", None))
    # retranslateUi

