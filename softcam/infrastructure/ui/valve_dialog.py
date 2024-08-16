# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'valve_dialog.ui'
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

class Ui_SoupapeDialog(object):
    def setupUi(self, SoupapeDialog):
        if not SoupapeDialog.objectName():
            SoupapeDialog.setObjectName(u"SoupapeDialog")
        SoupapeDialog.resize(436, 387)
        SoupapeDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(SoupapeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.msoupWidget = QWidget(SoupapeDialog)
        self.msoupWidget.setObjectName(u"msoupWidget")
        self.horizontalLayout = QHBoxLayout(self.msoupWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.msoupLabel = QLabel(self.msoupWidget)
        self.msoupLabel.setObjectName(u"msoupLabel")

        self.horizontalLayout.addWidget(self.msoupLabel, 0, Qt.AlignRight)

        self.msoupEdit = QLineEdit(self.msoupWidget)
        self.msoupEdit.setObjectName(u"msoupEdit")

        self.horizontalLayout.addWidget(self.msoupEdit, 0, Qt.AlignHCenter)

        self.msoupUnitLabel = QLabel(self.msoupWidget)
        self.msoupUnitLabel.setObjectName(u"msoupUnitLabel")

        self.horizontalLayout.addWidget(self.msoupUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.msoupWidget)

        self.mcoupelleWidget = QWidget(SoupapeDialog)
        self.mcoupelleWidget.setObjectName(u"mcoupelleWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.mcoupelleWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mcoupelleLabel = QLabel(self.mcoupelleWidget)
        self.mcoupelleLabel.setObjectName(u"mcoupelleLabel")

        self.horizontalLayout_2.addWidget(self.mcoupelleLabel, 0, Qt.AlignRight)

        self.mcoupelleEdit = QLineEdit(self.mcoupelleWidget)
        self.mcoupelleEdit.setObjectName(u"mcoupelleEdit")

        self.horizontalLayout_2.addWidget(self.mcoupelleEdit, 0, Qt.AlignHCenter)

        self.mcoupelleUnitLabel = QLabel(self.mcoupelleWidget)
        self.mcoupelleUnitLabel.setObjectName(u"mcoupelleUnitLabel")

        self.horizontalLayout_2.addWidget(self.mcoupelleUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.mcoupelleWidget)

        self.rsWidget = QWidget(SoupapeDialog)
        self.rsWidget.setObjectName(u"rsWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.rsWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rsLabel = QLabel(self.rsWidget)
        self.rsLabel.setObjectName(u"rsLabel")

        self.horizontalLayout_3.addWidget(self.rsLabel, 0, Qt.AlignRight)

        self.rsEdit = QLineEdit(self.rsWidget)
        self.rsEdit.setObjectName(u"rsEdit")

        self.horizontalLayout_3.addWidget(self.rsEdit, 0, Qt.AlignHCenter)

        self.rsUnitLabel = QLabel(self.rsWidget)
        self.rsUnitLabel.setObjectName(u"rsUnitLabel")

        self.horizontalLayout_3.addWidget(self.rsUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.rsWidget)

        self.dsoupWidget = QWidget(SoupapeDialog)
        self.dsoupWidget.setObjectName(u"dsoupWidget")
        self.horizontalLayout_7 = QHBoxLayout(self.dsoupWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.dsoupLabel = QLabel(self.dsoupWidget)
        self.dsoupLabel.setObjectName(u"dsoupLabel")

        self.horizontalLayout_7.addWidget(self.dsoupLabel, 0, Qt.AlignRight)

        self.dsoupEdit = QLineEdit(self.dsoupWidget)
        self.dsoupEdit.setObjectName(u"dsoupEdit")

        self.horizontalLayout_7.addWidget(self.dsoupEdit, 0, Qt.AlignHCenter)

        self.dsoupUnitLabel = QLabel(self.dsoupWidget)
        self.dsoupUnitLabel.setObjectName(u"dsoupUnitLabel")

        self.horizontalLayout_7.addWidget(self.dsoupUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.dsoupWidget)

        self.youngWidget = QWidget(SoupapeDialog)
        self.youngWidget.setObjectName(u"youngWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.youngWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.youngLabel = QLabel(self.youngWidget)
        self.youngLabel.setObjectName(u"youngLabel")

        self.horizontalLayout_4.addWidget(self.youngLabel, 0, Qt.AlignRight)

        self.youngEdit = QLineEdit(self.youngWidget)
        self.youngEdit.setObjectName(u"youngEdit")

        self.horizontalLayout_4.addWidget(self.youngEdit, 0, Qt.AlignHCenter)

        self.youngUnitLabel = QLabel(self.youngWidget)
        self.youngUnitLabel.setObjectName(u"youngUnitLabel")

        self.horizontalLayout_4.addWidget(self.youngUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.youngWidget)

        self.poissonWidget = QWidget(SoupapeDialog)
        self.poissonWidget.setObjectName(u"poissonWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.poissonWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.poissonLabel = QLabel(self.poissonWidget)
        self.poissonLabel.setObjectName(u"poissonLabel")

        self.horizontalLayout_5.addWidget(self.poissonLabel, 0, Qt.AlignRight)

        self.poissonEdit = QLineEdit(self.poissonWidget)
        self.poissonEdit.setObjectName(u"poissonEdit")

        self.horizontalLayout_5.addWidget(self.poissonEdit, 0, Qt.AlignHCenter)

        self.poissonUnitLabel = QLabel(self.poissonWidget)
        self.poissonUnitLabel.setObjectName(u"poissonUnitLabel")

        self.horizontalLayout_5.addWidget(self.poissonUnitLabel)


        self.verticalLayout.addWidget(self.poissonWidget)

        self.buttonBox = QDialogButtonBox(SoupapeDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SoupapeDialog)
        self.buttonBox.accepted.connect(SoupapeDialog.accept)
        self.buttonBox.rejected.connect(SoupapeDialog.reject)

        QMetaObject.connectSlotsByName(SoupapeDialog)
    # setupUi

    def retranslateUi(self, SoupapeDialog):
        SoupapeDialog.setWindowTitle(QCoreApplication.translate("SoupapeDialog", u"Soupape", None))
        self.msoupLabel.setText(QCoreApplication.translate("SoupapeDialog", u"Masse Soupape", None))
        self.msoupEdit.setText(QCoreApplication.translate("SoupapeDialog", u"43.5", None))
        self.msoupUnitLabel.setText(QCoreApplication.translate("SoupapeDialog", u"g", None))
        self.mcoupelleLabel.setText(QCoreApplication.translate("SoupapeDialog", u"Masse Coupelle", None))
        self.mcoupelleEdit.setText(QCoreApplication.translate("SoupapeDialog", u"5.5", None))
        self.mcoupelleUnitLabel.setText(QCoreApplication.translate("SoupapeDialog", u"g", None))
        self.rsLabel.setText(QCoreApplication.translate("SoupapeDialog", u"Rayon de Courbure", None))
        self.rsEdit.setText(QCoreApplication.translate("SoupapeDialog", u"inf", None))
        self.rsUnitLabel.setText(QCoreApplication.translate("SoupapeDialog", u"mm", None))
        self.dsoupLabel.setText(QCoreApplication.translate("SoupapeDialog", u"Diam\u00e8tre Soupape", None))
        self.dsoupEdit.setText(QCoreApplication.translate("SoupapeDialog", u"6", None))
        self.dsoupUnitLabel.setText(QCoreApplication.translate("SoupapeDialog", u"mm", None))
        self.youngLabel.setText(QCoreApplication.translate("SoupapeDialog", u"Module de Young", None))
        self.youngEdit.setText(QCoreApplication.translate("SoupapeDialog", u"200", None))
        self.youngUnitLabel.setText(QCoreApplication.translate("SoupapeDialog", u"GPa", None))
        self.poissonLabel.setText(QCoreApplication.translate("SoupapeDialog", u"Coefficient de Poisson", None))
        self.poissonEdit.setText(QCoreApplication.translate("SoupapeDialog", u"0.3", None))
        self.poissonUnitLabel.setText(QCoreApplication.translate("SoupapeDialog", u"Sans Unit\u00e9", None))
    # retranslateUi

