# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'option_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)
import infrastructure.ui.resources.resources_rc

class Ui_OptionDialog(object):
    def setupUi(self, OptionDialog):
        if not OptionDialog.objectName():
            OptionDialog.setObjectName(u"OptionDialog")
        OptionDialog.resize(403, 245)
        OptionDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dialogLayout = QVBoxLayout(OptionDialog)
        self.dialogLayout.setObjectName(u"dialogLayout")
        self.formWidget = QWidget(OptionDialog)
        self.formWidget.setObjectName(u"formWidget")
        self.formLayout = QFormLayout(self.formWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.studynameLabel = QLabel(self.formWidget)
        self.studynameLabel.setObjectName(u"studynameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.studynameLabel)

        self.studynameEdit = QLineEdit(self.formWidget)
        self.studynameEdit.setObjectName(u"studynameEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.studynameEdit)

        self.stepangleLabel = QLabel(self.formWidget)
        self.stepangleLabel.setObjectName(u"stepangleLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.stepangleLabel)

        self.stepangleEdit = QLineEdit(self.formWidget)
        self.stepangleEdit.setObjectName(u"stepangleEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.stepangleEdit)

        self.steptimeLabel = QLabel(self.formWidget)
        self.steptimeLabel.setObjectName(u"steptimeLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.steptimeLabel)

        self.steptimeEdit = QLineEdit(self.formWidget)
        self.steptimeEdit.setObjectName(u"steptimeEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.steptimeEdit)

        self.stepdisplayLabel = QLabel(self.formWidget)
        self.stepdisplayLabel.setObjectName(u"stepdisplayLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.stepdisplayLabel)

        self.stepdisplayEdit = QLineEdit(self.formWidget)
        self.stepdisplayEdit.setObjectName(u"stepdisplayEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.stepdisplayEdit)


        self.dialogLayout.addWidget(self.formWidget)

        self.buttonBox = QDialogButtonBox(OptionDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.dialogLayout.addWidget(self.buttonBox)


        self.retranslateUi(OptionDialog)
        self.buttonBox.accepted.connect(OptionDialog.accept)
        self.buttonBox.rejected.connect(OptionDialog.reject)

        QMetaObject.connectSlotsByName(OptionDialog)
    # setupUi

    def retranslateUi(self, OptionDialog):
        OptionDialog.setWindowTitle(QCoreApplication.translate("OptionDialog", u"Options", None))
        self.studynameLabel.setText(QCoreApplication.translate("OptionDialog", u"Nom de l'\u00c9tude", None))
        self.studynameEdit.setText(QCoreApplication.translate("OptionDialog", u"new_study", None))
        self.stepangleLabel.setText(QCoreApplication.translate("OptionDialog", u"Pas Calcul (\u00b0)", None))
        self.stepangleEdit.setText(QCoreApplication.translate("OptionDialog", u"0.01", None))
        self.steptimeLabel.setText(QCoreApplication.translate("OptionDialog", u"Pas Int\u00e9gration Temporelle (ms)", None))
        self.steptimeEdit.setText(QCoreApplication.translate("OptionDialog", u"1", None))
        self.stepdisplayLabel.setText(QCoreApplication.translate("OptionDialog", u"Pas Affichage Graphique (\u00b0)", None))
        self.stepdisplayEdit.setText(QCoreApplication.translate("OptionDialog", u"0.01", None))
    # retranslateUi

