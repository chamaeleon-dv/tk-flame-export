# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'submit_dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_SubmitDialog(object):
    def setupUi(self, SubmitDialog):
        SubmitDialog.setObjectName("SubmitDialog")
        SubmitDialog.resize(487, 594)
        self.verticalLayout = QtGui.QVBoxLayout(SubmitDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(SubmitDialog)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/tk-flame-export/ui_splash.png"))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(SubmitDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.shotgun_sequencename = QtGui.QPlainTextEdit(SubmitDialog)
        self.shotgun_sequencename.setMinimumSize(QtCore.QSize(0, 25))
        self.shotgun_sequencename.setMaximumSize(QtCore.QSize(16777215, 25))
        self.shotgun_sequencename.setObjectName("shotgun_sequencename")
        self.verticalLayout.addWidget(self.shotgun_sequencename)
        self.label_4 = QtGui.QLabel(SubmitDialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comments = QtGui.QPlainTextEdit(SubmitDialog)
        self.comments.setMinimumSize(QtCore.QSize(300, 100))
        self.comments.setObjectName("comments")
        self.verticalLayout.addWidget(self.comments)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(SubmitDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.export_presets = QtGui.QComboBox(SubmitDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_presets.sizePolicy().hasHeightForWidth())
        self.export_presets.setSizePolicy(sizePolicy)
        self.export_presets.setObjectName("export_presets")
        self.horizontalLayout_2.addWidget(self.export_presets)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(368, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel = QtGui.QPushButton(SubmitDialog)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.submit = QtGui.QPushButton(SubmitDialog)
        self.submit.setObjectName("submit")
        self.horizontalLayout.addWidget(self.submit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SubmitDialog)
        QtCore.QMetaObject.connectSlotsByName(SubmitDialog)

    def retranslateUi(self, SubmitDialog):
        SubmitDialog.setWindowTitle(QtGui.QApplication.translate("SubmitDialog", "Submit to Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SubmitDialog", "Connect to following Sequence in Shotgun:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SubmitDialog", "Comment:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SubmitDialog", "Use Export Preset", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("SubmitDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.submit.setText(QtGui.QApplication.translate("SubmitDialog", "Submit to Shotgun", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
