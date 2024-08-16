# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newstudy_dialog.ui'
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
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_NewStudyDialog(object):
    def setupUi(self, NewStudyDialog):
        if not NewStudyDialog.objectName():
            NewStudyDialog.setObjectName(u"NewStudyDialog")
        NewStudyDialog.resize(318, 240)
        NewStudyDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.mainLayout = QVBoxLayout(NewStudyDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.valuesWidget = QWidget(NewStudyDialog)
        self.valuesWidget.setObjectName(u"valuesWidget")
        self.valuesLayout = QGridLayout(self.valuesWidget)
        self.valuesLayout.setObjectName(u"valuesLayout")
        self.studynameUnitLabel = QLabel(self.valuesWidget)
        self.studynameUnitLabel.setObjectName(u"studynameUnitLabel")

        self.valuesLayout.addWidget(self.studynameUnitLabel, 0, 2, 1, 1)

        self.steptimeEdit = QLineEdit(self.valuesWidget)
        self.steptimeEdit.setObjectName(u"steptimeEdit")

        self.valuesLayout.addWidget(self.steptimeEdit, 2, 1, 1, 1)

        self.steptimeLabel = QLabel(self.valuesWidget)
        self.steptimeLabel.setObjectName(u"steptimeLabel")

        self.valuesLayout.addWidget(self.steptimeLabel, 2, 0, 1, 1)

        self.studynameLabel = QLabel(self.valuesWidget)
        self.studynameLabel.setObjectName(u"studynameLabel")

        self.valuesLayout.addWidget(self.studynameLabel, 0, 0, 1, 1)

        self.studynameEdit = QLineEdit(self.valuesWidget)
        self.studynameEdit.setObjectName(u"studynameEdit")

        self.valuesLayout.addWidget(self.studynameEdit, 0, 1, 1, 1)

        self.steptimeUnitLabel = QLabel(self.valuesWidget)
        self.steptimeUnitLabel.setObjectName(u"steptimeUnitLabel")

        self.valuesLayout.addWidget(self.steptimeUnitLabel, 2, 2, 1, 1)

        self.assemblytypeLabel = QLabel(self.valuesWidget)
        self.assemblytypeLabel.setObjectName(u"assemblytypeLabel")

        self.valuesLayout.addWidget(self.assemblytypeLabel, 1, 0, 1, 1)

        self.assemblytypeComboBox = QComboBox(self.valuesWidget)
        self.assemblytypeComboBox.addItem("")
        self.assemblytypeComboBox.addItem("")
        self.assemblytypeComboBox.setObjectName(u"assemblytypeComboBox")

        self.valuesLayout.addWidget(self.assemblytypeComboBox, 1, 1, 1, 1)


        self.mainLayout.addWidget(self.valuesWidget)

        self.buttonBox = QDialogButtonBox(NewStudyDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.mainLayout.addWidget(self.buttonBox)


        self.retranslateUi(NewStudyDialog)
        self.buttonBox.accepted.connect(NewStudyDialog.accept)
        self.buttonBox.rejected.connect(NewStudyDialog.reject)

        QMetaObject.connectSlotsByName(NewStudyDialog)
    # setupUi

    def retranslateUi(self, NewStudyDialog):
        NewStudyDialog.setWindowTitle(QCoreApplication.translate("NewStudyDialog", u"Dialog", None))
        self.studynameUnitLabel.setText("")
        self.steptimeEdit.setText(QCoreApplication.translate("NewStudyDialog", u"0.001", None))
        self.steptimeLabel.setText(QCoreApplication.translate("NewStudyDialog", u"<html><head/><body><p align=\"right\">Pas d'Int\u00e9gration</p></body></html>", None))
        self.studynameLabel.setText(QCoreApplication.translate("NewStudyDialog", u"<html><head/><body><p align=\"right\">Nom de l'\u00e9tude</p></body></html>", None))
        self.studynameEdit.setText(QCoreApplication.translate("NewStudyDialog", u"new_study", None))
        self.steptimeUnitLabel.setText(QCoreApplication.translate("NewStudyDialog", u"secondes", None))
        self.assemblytypeLabel.setText(QCoreApplication.translate("NewStudyDialog", u"<html><head/><body><p align=\"right\">Type</p></body></html>", None))
        self.assemblytypeComboBox.setItemText(0, QCoreApplication.translate("NewStudyDialog", u"Linguet / Basculeur", None))
        self.assemblytypeComboBox.setItemText(1, QCoreApplication.translate("NewStudyDialog", u"Attaque Directe", None))

        self.assemblytypeComboBox.setCurrentText(QCoreApplication.translate("NewStudyDialog", u"Linguet / Basculeur", None))
    # retranslateUi

