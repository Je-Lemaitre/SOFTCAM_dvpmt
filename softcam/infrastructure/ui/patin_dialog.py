# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patin_dialog.ui'
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

class Ui_PatinDialog(object):
    def setupUi(self, PatinDialog):
        if not PatinDialog.objectName():
            PatinDialog.setObjectName(u"PatinDialog")
        PatinDialog.resize(652, 411)
        PatinDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(PatinDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rpWidget = QWidget(PatinDialog)
        self.rpWidget.setObjectName(u"rpWidget")
        self.horizontalLayout = QHBoxLayout(self.rpWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rpLabel = QLabel(self.rpWidget)
        self.rpLabel.setObjectName(u"rpLabel")

        self.horizontalLayout.addWidget(self.rpLabel, 0, Qt.AlignRight)

        self.rpEdit = QLineEdit(self.rpWidget)
        self.rpEdit.setObjectName(u"rpEdit")

        self.horizontalLayout.addWidget(self.rpEdit, 0, Qt.AlignHCenter)

        self.rpUnitLabel = QLabel(self.rpWidget)
        self.rpUnitLabel.setObjectName(u"rpUnitLabel")

        self.horizontalLayout.addWidget(self.rpUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.rpWidget)

        self.widthWidget = QWidget(PatinDialog)
        self.widthWidget.setObjectName(u"widthWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.widthWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widthLabel = QLabel(self.widthWidget)
        self.widthLabel.setObjectName(u"widthLabel")

        self.horizontalLayout_4.addWidget(self.widthLabel, 0, Qt.AlignRight)

        self.widthEdit = QLineEdit(self.widthWidget)
        self.widthEdit.setObjectName(u"widthEdit")

        self.horizontalLayout_4.addWidget(self.widthEdit, 0, Qt.AlignHCenter)

        self.widthUnitLabel = QLabel(self.widthWidget)
        self.widthUnitLabel.setObjectName(u"widthUnitLabel")

        self.horizontalLayout_4.addWidget(self.widthUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.widthWidget)

        self.youngWidget = QWidget(PatinDialog)
        self.youngWidget.setObjectName(u"youngWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.youngWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.youngLabel = QLabel(self.youngWidget)
        self.youngLabel.setObjectName(u"youngLabel")

        self.horizontalLayout_2.addWidget(self.youngLabel, 0, Qt.AlignRight)

        self.youngEdit = QLineEdit(self.youngWidget)
        self.youngEdit.setObjectName(u"youngEdit")

        self.horizontalLayout_2.addWidget(self.youngEdit, 0, Qt.AlignHCenter)

        self.youngUnitLabel = QLabel(self.youngWidget)
        self.youngUnitLabel.setObjectName(u"youngUnitLabel")

        self.horizontalLayout_2.addWidget(self.youngUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.youngWidget)

        self.poissonWidget = QWidget(PatinDialog)
        self.poissonWidget.setObjectName(u"poissonWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.poissonWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.poissonLabel = QLabel(self.poissonWidget)
        self.poissonLabel.setObjectName(u"poissonLabel")

        self.horizontalLayout_3.addWidget(self.poissonLabel, 0, Qt.AlignRight)

        self.poissonEdit = QLineEdit(self.poissonWidget)
        self.poissonEdit.setObjectName(u"poissonEdit")

        self.horizontalLayout_3.addWidget(self.poissonEdit, 0, Qt.AlignHCenter)

        self.poissonEmptyWidget = QWidget(self.poissonWidget)
        self.poissonEmptyWidget.setObjectName(u"poissonEmptyWidget")

        self.horizontalLayout_3.addWidget(self.poissonEmptyWidget, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.poissonWidget)

        self.buttonBox = QDialogButtonBox(PatinDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(PatinDialog)
        self.buttonBox.accepted.connect(PatinDialog.accept)
        self.buttonBox.rejected.connect(PatinDialog.reject)

        QMetaObject.connectSlotsByName(PatinDialog)
    # setupUi

    def retranslateUi(self, PatinDialog):
        PatinDialog.setWindowTitle(QCoreApplication.translate("PatinDialog", u"Patin", None))
        self.rpLabel.setText(QCoreApplication.translate("PatinDialog", u"Rayon de Courbure", None))
        self.rpEdit.setText(QCoreApplication.translate("PatinDialog", u"27", None))
        self.rpUnitLabel.setText(QCoreApplication.translate("PatinDialog", u"mm", None))
        self.widthLabel.setText(QCoreApplication.translate("PatinDialog", u"Largeur", None))
        self.widthEdit.setText(QCoreApplication.translate("PatinDialog", u"6", None))
        self.widthUnitLabel.setText(QCoreApplication.translate("PatinDialog", u"mm", None))
        self.youngLabel.setText(QCoreApplication.translate("PatinDialog", u"Module de Young", None))
        self.youngEdit.setText(QCoreApplication.translate("PatinDialog", u"210", None))
        self.youngUnitLabel.setText(QCoreApplication.translate("PatinDialog", u"GPa", None))
        self.poissonLabel.setText(QCoreApplication.translate("PatinDialog", u"Coefficient de Poisson", None))
        self.poissonEdit.setText(QCoreApplication.translate("PatinDialog", u"0.3", None))
    # retranslateUi

