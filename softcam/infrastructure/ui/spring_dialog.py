# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spring_dialog.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)
import infrastructure.ui.resources.resources_rc

class Ui_RessortDialog(object):
    def setupUi(self, RessortDialog):
        if not RessortDialog.objectName():
            RessortDialog.setObjectName(u"RessortDialog")
        RessortDialog.resize(652, 387)
        RessortDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(RessortDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.massWidget = QWidget(RessortDialog)
        self.massWidget.setObjectName(u"massWidget")
        self.horizontalLayout = QHBoxLayout(self.massWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.massLabel = QLabel(self.massWidget)
        self.massLabel.setObjectName(u"massLabel")

        self.horizontalLayout.addWidget(self.massLabel, 0, Qt.AlignRight)

        self.massEdit = QLineEdit(self.massWidget)
        self.massEdit.setObjectName(u"massEdit")

        self.horizontalLayout.addWidget(self.massEdit, 0, Qt.AlignHCenter)

        self.massUnitLabel = QLabel(self.massWidget)
        self.massUnitLabel.setObjectName(u"massUnitLabel")

        self.horizontalLayout.addWidget(self.massUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.massWidget)

        self.stiffnessWidget = QWidget(RessortDialog)
        self.stiffnessWidget.setObjectName(u"stiffnessWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.stiffnessWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stiffnessLabel = QLabel(self.stiffnessWidget)
        self.stiffnessLabel.setObjectName(u"stiffnessLabel")

        self.horizontalLayout_2.addWidget(self.stiffnessLabel, 0, Qt.AlignRight)

        self.stiffnessEdit = QLineEdit(self.stiffnessWidget)
        self.stiffnessEdit.setObjectName(u"stiffnessEdit")

        self.horizontalLayout_2.addWidget(self.stiffnessEdit, 0, Qt.AlignHCenter)

        self.widthUnitLabel = QLabel(self.stiffnessWidget)
        self.widthUnitLabel.setObjectName(u"widthUnitLabel")

        self.horizontalLayout_2.addWidget(self.widthUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.stiffnessWidget)

        self.preloadWidget = QWidget(RessortDialog)
        self.preloadWidget.setObjectName(u"preloadWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.preloadWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.preloadLabel = QLabel(self.preloadWidget)
        self.preloadLabel.setObjectName(u"preloadLabel")

        self.horizontalLayout_3.addWidget(self.preloadLabel, 0, Qt.AlignRight)

        self.preloadEdit = QLineEdit(self.preloadWidget)
        self.preloadEdit.setObjectName(u"preloadEdit")

        self.horizontalLayout_3.addWidget(self.preloadEdit, 0, Qt.AlignHCenter)

        self.preloadUnitLabel = QLabel(self.preloadWidget)
        self.preloadUnitLabel.setObjectName(u"preloadUnitLabel")

        self.horizontalLayout_3.addWidget(self.preloadUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.preloadWidget)

        self.buttonBox = QDialogButtonBox(RessortDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(RessortDialog)
        self.buttonBox.accepted.connect(RessortDialog.accept)
        self.buttonBox.rejected.connect(RessortDialog.reject)

        QMetaObject.connectSlotsByName(RessortDialog)
    # setupUi

    def retranslateUi(self, RessortDialog):
        RessortDialog.setWindowTitle(QCoreApplication.translate("RessortDialog", u"Ressort", None))
        self.massLabel.setText(QCoreApplication.translate("RessortDialog", u"Masse", None))
        self.massEdit.setText(QCoreApplication.translate("RessortDialog", u"27", None))
        self.massUnitLabel.setText(QCoreApplication.translate("RessortDialog", u"g", None))
        self.stiffnessLabel.setText(QCoreApplication.translate("RessortDialog", u"Raideur", None))
        self.stiffnessEdit.setText(QCoreApplication.translate("RessortDialog", u"46.5", None))
        self.widthUnitLabel.setText(QCoreApplication.translate("RessortDialog", u"N/mm", None))
        self.preloadLabel.setText(QCoreApplication.translate("RessortDialog", u"Precharge", None))
        self.preloadEdit.setText(QCoreApplication.translate("RessortDialog", u"240", None))
        self.preloadUnitLabel.setText(QCoreApplication.translate("RessortDialog", u"N", None))
    # retranslateUi

