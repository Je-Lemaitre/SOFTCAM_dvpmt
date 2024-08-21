# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cam_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit, QToolButton, QVBoxLayout, QWidget

import infrastructure.ui.resources.resources_rc

class Ui_CamDialog(object):
    def setupUi(self, CamDialog):
        if not CamDialog.objectName():
            CamDialog.setObjectName(u"CamDialog")
        CamDialog.resize(652, 321)
        CamDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(CamDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rbWidget = QWidget(CamDialog)
        self.rbWidget.setObjectName(u"rbWidget")
        self.horizontalLayout = QHBoxLayout(self.rbWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rbLabel = QLabel(self.rbWidget)
        self.rbLabel.setObjectName(u"rbLabel")

        self.horizontalLayout.addWidget(self.rbLabel, 0, Qt.AlignRight)

        self.rbEdit = QLineEdit(self.rbWidget)
        self.rbEdit.setObjectName(u"rbEdit")

        self.horizontalLayout.addWidget(self.rbEdit, 0, Qt.AlignHCenter)

        self.rbUnitLabel = QLabel(self.rbWidget)
        self.rbUnitLabel.setObjectName(u"rbUnitLabel")

        self.horizontalLayout.addWidget(self.rbUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.rbWidget)

        self.widthWidget = QWidget(CamDialog)
        self.widthWidget.setObjectName(u"widthWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.widthWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widthLabel = QLabel(self.widthWidget)
        self.widthLabel.setObjectName(u"widthLabel")

        self.horizontalLayout_2.addWidget(self.widthLabel, 0, Qt.AlignRight)

        self.widthEdit = QLineEdit(self.widthWidget)
        self.widthEdit.setObjectName(u"widthEdit")

        self.horizontalLayout_2.addWidget(self.widthEdit, 0, Qt.AlignHCenter)

        self.widthUnitLabel = QLabel(self.widthWidget)
        self.widthUnitLabel.setObjectName(u"widthUnitLabel")

        self.horizontalLayout_2.addWidget(self.widthUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.widthWidget)

        self.inertiaWidget = QWidget(CamDialog)
        self.inertiaWidget.setObjectName(u"inertiaWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.inertiaWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.inertiaLabel = QLabel(self.inertiaWidget)
        self.inertiaLabel.setObjectName(u"inertiaLabel")

        self.horizontalLayout_3.addWidget(self.inertiaLabel, 0, Qt.AlignRight)

        self.inertiaEdit = QLineEdit(self.inertiaWidget)
        self.inertiaEdit.setObjectName(u"inertiaEdit")

        self.horizontalLayout_3.addWidget(self.inertiaEdit, 0, Qt.AlignHCenter)

        self.inertiaUnitLabel = QLabel(self.inertiaWidget)
        self.inertiaUnitLabel.setObjectName(u"inertiaUnitLabel")

        self.horizontalLayout_3.addWidget(self.inertiaUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.inertiaWidget)

        self.youngWidget = QWidget(CamDialog)
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

        self.poissonWidget = QWidget(CamDialog)
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

        self.profileWidget = QWidget(CamDialog)
        self.profileWidget.setObjectName(u"profileWidget")
        self.horizontalLayout_6 = QHBoxLayout(self.profileWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.profileLabel = QLabel(self.profileWidget)
        self.profileLabel.setObjectName(u"profileLabel")

        self.horizontalLayout_6.addWidget(self.profileLabel, 0, Qt.AlignRight)

        self.browseProfileButton = QToolButton(self.profileWidget)
        self.browseProfileButton.setObjectName(u"browseProfileButton")
        self.browseProfileButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u":/icons/icons/folder-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.browseProfileButton.setIcon(icon)
        self.browseProfileButton.setPopupMode(QToolButton.InstantPopup)
        self.browseProfileButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.browseProfileButton.setAutoRaise(False)

        self.horizontalLayout_6.addWidget(self.browseProfileButton, 0, Qt.AlignHCenter)

        self.profileUnitLabel = QLabel(self.profileWidget)
        self.profileUnitLabel.setObjectName(u"profileUnitLabel")

        self.horizontalLayout_6.addWidget(self.profileUnitLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.profileWidget)

        self.buttonBox = QDialogButtonBox(CamDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(CamDialog)
        self.buttonBox.accepted.connect(CamDialog.accept)
        self.buttonBox.rejected.connect(CamDialog.reject)
        self.browseProfileButton.clicked.connect(self.browseProfileButton.update)

        QMetaObject.connectSlotsByName(CamDialog)
    # setupUi

    def retranslateUi(self, CamDialog):
        CamDialog.setWindowTitle(QCoreApplication.translate("CamDialog", u"Dialog", None))
        self.rbLabel.setText(QCoreApplication.translate("CamDialog", u"Rayon de Base", None))
        self.rbEdit.setText(QCoreApplication.translate("CamDialog", u"19", None))
        self.rbUnitLabel.setText(QCoreApplication.translate("CamDialog", u"mm", None))
        self.widthLabel.setText(QCoreApplication.translate("CamDialog", u"Largeur", None))
        self.widthEdit.setText(QCoreApplication.translate("CamDialog", u"8", None))
        self.widthUnitLabel.setText(QCoreApplication.translate("CamDialog", u"mm", None))
        self.inertiaLabel.setText(QCoreApplication.translate("CamDialog", u"Inertie", None))
        self.inertiaEdit.setText(QCoreApplication.translate("CamDialog", u"1000", None))
        self.inertiaUnitLabel.setText(QCoreApplication.translate("CamDialog", u"g.mm\u00b2", None))
        self.youngLabel.setText(QCoreApplication.translate("CamDialog", u"Module de Young", None))
        self.youngEdit.setText(QCoreApplication.translate("CamDialog", u"200", None))
        self.youngUnitLabel.setText(QCoreApplication.translate("CamDialog", u"GPa", None))
        self.poissonLabel.setText(QCoreApplication.translate("CamDialog", u"Coefficient de Poisson", None))
        self.poissonEdit.setText(QCoreApplication.translate("CamDialog", u"0.3", None))
        self.poissonUnitLabel.setText(QCoreApplication.translate("CamDialog", u"Sans Unit\u00e9", None))
        self.profileLabel.setText(QCoreApplication.translate("CamDialog", u"Profil", None))
        self.browseProfileButton.setText(QCoreApplication.translate("CamDialog", u"No File", None))
        self.profileUnitLabel.setText(QCoreApplication.translate("CamDialog", u".txt", None))
    # retranslateUi

