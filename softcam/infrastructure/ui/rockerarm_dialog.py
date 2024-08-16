# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rockerarm_dialog.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import infrastructure.ui.resources.resources_rc

class Ui_LinguetDialog(object):
    def setupUi(self, LinguetDialog):
        if not LinguetDialog.objectName():
            LinguetDialog.setObjectName(u"LinguetDialog")
        LinguetDialog.resize(652, 387)
        LinguetDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(LinguetDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.massWidget = QWidget(LinguetDialog)
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

        self.inertiaWidget = QWidget(LinguetDialog)
        self.inertiaWidget.setObjectName(u"inertiaWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.inertiaWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.inertiaLabel = QLabel(self.inertiaWidget)
        self.inertiaLabel.setObjectName(u"inertiaLabel")

        self.horizontalLayout_4.addWidget(self.inertiaLabel, 0, Qt.AlignRight)

        self.inertiaEdit = QLineEdit(self.inertiaWidget)
        self.inertiaEdit.setObjectName(u"inertiaEdit")

        self.horizontalLayout_4.addWidget(self.inertiaEdit, 0, Qt.AlignHCenter)

        self.inertiaUnitLabel = QLabel(self.inertiaWidget)
        self.inertiaUnitLabel.setObjectName(u"inertiaUnitLabel")

        self.horizontalLayout_4.addWidget(self.inertiaUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.inertiaWidget)

        self.lengthWidget = QWidget(LinguetDialog)
        self.lengthWidget.setObjectName(u"lengthWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.lengthWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lengthLabel = QLabel(self.lengthWidget)
        self.lengthLabel.setObjectName(u"lengthLabel")

        self.horizontalLayout_2.addWidget(self.lengthLabel, 0, Qt.AlignRight)

        self.lengthEdit = QLineEdit(self.lengthWidget)
        self.lengthEdit.setObjectName(u"lengthEdit")

        self.horizontalLayout_2.addWidget(self.lengthEdit, 0, Qt.AlignHCenter)

        self.lengthUnitLabel = QLabel(self.lengthWidget)
        self.lengthUnitLabel.setObjectName(u"lengthUnitLabel")

        self.horizontalLayout_2.addWidget(self.lengthUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.lengthWidget)

        self.createpcWidget = QWidget(LinguetDialog)
        self.createpcWidget.setObjectName(u"createpcWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.createpcWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.createpcLabel = QLabel(self.createpcWidget)
        self.createpcLabel.setObjectName(u"createpcLabel")

        self.horizontalLayout_5.addWidget(self.createpcLabel, 0, Qt.AlignRight)

        self.createpcButton = QPushButton(self.createpcWidget)
        self.createpcButton.setObjectName(u"createpcButton")
        self.createpcButton.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.createpcButton, 0, Qt.AlignHCenter)

        self.createpcEmptyWidget = QWidget(self.createpcWidget)
        self.createpcEmptyWidget.setObjectName(u"createpcEmptyWidget")

        self.horizontalLayout_5.addWidget(self.createpcEmptyWidget, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.createpcWidget)

        self.createpsWidget = QWidget(LinguetDialog)
        self.createpsWidget.setObjectName(u"createpsWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.createpsWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.createpsLabel = QLabel(self.createpsWidget)
        self.createpsLabel.setObjectName(u"createpsLabel")

        self.horizontalLayout_3.addWidget(self.createpsLabel, 0, Qt.AlignRight)

        self.createpsButton = QPushButton(self.createpsWidget)
        self.createpsButton.setObjectName(u"createpsButton")
        self.createpsButton.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.createpsButton, 0, Qt.AlignHCenter)

        self.createpsEmptyWidget = QWidget(self.createpsWidget)
        self.createpsEmptyWidget.setObjectName(u"createpsEmptyWidget")

        self.horizontalLayout_3.addWidget(self.createpsEmptyWidget, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.createpsWidget)

        self.buttonBox = QDialogButtonBox(LinguetDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(LinguetDialog)
        self.buttonBox.accepted.connect(LinguetDialog.accept)
        self.buttonBox.rejected.connect(LinguetDialog.reject)

        QMetaObject.connectSlotsByName(LinguetDialog)
    # setupUi

    def retranslateUi(self, LinguetDialog):
        LinguetDialog.setWindowTitle(QCoreApplication.translate("LinguetDialog", u"Linguet", None))
        self.massLabel.setText(QCoreApplication.translate("LinguetDialog", u"Masse", None))
        self.massEdit.setText(QCoreApplication.translate("LinguetDialog", u"70", None))
        self.massUnitLabel.setText(QCoreApplication.translate("LinguetDialog", u"g", None))
        self.inertiaLabel.setText(QCoreApplication.translate("LinguetDialog", u"Inertie", None))
        self.inertiaEdit.setText(QCoreApplication.translate("LinguetDialog", u"9000", None))
        self.inertiaUnitLabel.setText(QCoreApplication.translate("LinguetDialog", u"g.mm\u00b2", None))
        self.lengthLabel.setText(QCoreApplication.translate("LinguetDialog", u"Longueur", None))
        self.lengthEdit.setText(QCoreApplication.translate("LinguetDialog", u"36.8", None))
        self.lengthUnitLabel.setText(QCoreApplication.translate("LinguetDialog", u"mm", None))
        self.createpcLabel.setText(QCoreApplication.translate("LinguetDialog", u"Patin C\u00f4t\u00e9 Came", None))
        self.createpcButton.setText(QCoreApplication.translate("LinguetDialog", u"Cr\u00e9er Patin", None))
        self.createpsLabel.setText(QCoreApplication.translate("LinguetDialog", u"Patin C\u00f4t\u00e9 Soupape", None))
        self.createpsButton.setText(QCoreApplication.translate("LinguetDialog", u"Cr\u00e9er Patin", None))
    # retranslateUi

