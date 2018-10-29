# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SystemInfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import queries



class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(469, 208)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MainForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label1 = QtWidgets.QLabel(MainForm)
        self.label1.setObjectName("label1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label1)
        self.ComputerNameQueryPlaceholder = QtWidgets.QLabel(MainForm)
        self.ComputerNameQueryPlaceholder.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ComputerNameQueryPlaceholder.setObjectName("ComputerNameQueryPlaceholder")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ComputerNameQueryPlaceholder)
        self.label2 = QtWidgets.QLabel(MainForm)
        self.label2.setObjectName("label2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.globalid = QtWidgets.QLabel(MainForm)
        self.globalid.setObjectName("globalid")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.globalid)
        self.label3 = QtWidgets.QLabel(MainForm)
        self.label3.setObjectName("label3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label3)
        self.serialnumber = QtWidgets.QLabel(MainForm)
        self.serialnumber.setObjectName("serialnumber")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.serialnumber)
        self.windowsVersion = QtWidgets.QLabel(MainForm)
        self.windowsVersion.setObjectName("windowsVersion")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.windowsVersion)
        self.WindowsVersionValue = QtWidgets.QLabel(MainForm)
        self.WindowsVersionValue.setObjectName("WindowsVersionValue")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.WindowsVersionValue)
        self.monitorInfo = QtWidgets.QLabel(MainForm)
        self.monitorInfo.setObjectName("monitorInfo")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.monitorInfo)
        self.monitor1QueryPlaceholder = QtWidgets.QLabel(MainForm)
        self.monitor1QueryPlaceholder.setWordWrap(True)
        self.monitor1QueryPlaceholder.setObjectName("monitor1QueryPlaceholder")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.monitor1QueryPlaceholder)
        self.monitor2QueryPlaceholder = QtWidgets.QLabel(MainForm)
        self.monitor2QueryPlaceholder.setObjectName("monitor2QueryPlaceholder")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.monitor2QueryPlaceholder)
        self.bitlocker = QtWidgets.QLabel(MainForm)
        self.bitlocker.setObjectName("bitlocker")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.bitlocker)
        self.bitlockerKeyPlaceholder = QtWidgets.QLabel(MainForm)
        self.bitlockerKeyPlaceholder.setObjectName("bitlockerKeyPlaceholder")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.bitlockerKeyPlaceholder)
        self.horizontalLayout.addLayout(self.formLayout)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Information about your computer"))
        self.label1.setText(_translate("MainForm", "Name of Your Computer"))
        self.ComputerNameQueryPlaceholder.setText(_translate("MainForm", queries.platform.node()))
        self.label2.setText(_translate("MainForm", "Your GlobalID"))
        self.globalid.setText(_translate("MainForm", queries.os.getlogin()))
        self.label3.setText(_translate("MainForm", "Laptop serial number"))
        self.serialnumber.setText(_translate("MainForm", queries.win32_bios_serialnumber()))
        self.windowsVersion.setText(_translate("MainForm", "Windows version"))
        self.WindowsVersionValue.setText(_translate("MainForm", "You have Windows " + queries.platform.uname()[2]))
        self.monitorInfo.setText(_translate("MainForm", "Attached Monitors"))
        self.monitor1QueryPlaceholder.setText(_translate("MainForm", queries.run_powershell_script('.\Monitors.ps1', 3)))
        self.monitor2QueryPlaceholder.setText(_translate("MainForm", queries.run_powershell_script('.\Monitors.ps1', 4)))
        self.bitlocker.setText(_translate("MainForm", "Bitlocker Key"))
        self.bitlockerKeyPlaceholder.setText(_translate("MainForm", queries.bitlocker_key(9).lstrip()))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())

