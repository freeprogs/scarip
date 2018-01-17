# -*- coding: utf-8 -*-

# This file is a part of __PROGRAM_NAME__ __PROGRAM_VERSION__
#
# This file installs __PROGRAM_NAME__ in the operating system, cleans
# temporary files and directory in the project.
#
# __PROGRAM_COPYRIGHT__ __PROGRAM_AUTHOR__ __PROGRAM_AUTHOR_EMAIL__
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(805, 270, 81, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutContolButtons = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutContolButtons.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayoutContolButtons.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutContolButtons.setObjectName("verticalLayoutContolButtons")
        self.pushButtonControlButtonsScan = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonControlButtonsScan.setObjectName("pushButtonControlButtonsScan")
        self.verticalLayoutContolButtons.addWidget(self.pushButtonControlButtonsScan)
        self.pushButtonControlButtonsCancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonControlButtonsCancel.setObjectName("pushButtonControlButtonsCancel")
        self.verticalLayoutContolButtons.addWidget(self.pushButtonControlButtonsCancel)
        self.pushButtonControlButtonsQuit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonControlButtonsQuit.setObjectName("pushButtonControlButtonsQuit")
        self.verticalLayoutContolButtons.addWidget(self.pushButtonControlButtonsQuit)
        self.scrollAreaLog = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaLog.setGeometry(QtCore.QRect(10, 270, 781, 231))
        self.scrollAreaLog.setWidgetResizable(True)
        self.scrollAreaLog.setObjectName("scrollAreaLog")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 777, 227))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaLog.setWidget(self.scrollAreaWidgetContents)
        self.groupBoxPorts = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxPorts.setGeometry(QtCore.QRect(560, 10, 331, 241))
        self.groupBoxPorts.setObjectName("groupBoxPorts")
        self.labelPortsFirst = QtWidgets.QLabel(self.groupBoxPorts)
        self.labelPortsFirst.setGeometry(QtCore.QRect(30, 60, 64, 15))
        self.labelPortsFirst.setObjectName("labelPortsFirst")
        self.labelPortsLast = QtWidgets.QLabel(self.groupBoxPorts)
        self.labelPortsLast.setGeometry(QtCore.QRect(30, 150, 64, 15))
        self.labelPortsLast.setObjectName("labelPortsLast")
        self.spinBoxPortsFirst = QtWidgets.QSpinBox(self.groupBoxPorts)
        self.spinBoxPortsFirst.setGeometry(QtCore.QRect(30, 80, 71, 29))
        self.spinBoxPortsFirst.setObjectName("spinBoxPortsFirst")
        self.pushButtonPortsClear = QtWidgets.QPushButton(self.groupBoxPorts)
        self.pushButtonPortsClear.setGeometry(QtCore.QRect(120, 170, 84, 31))
        self.pushButtonPortsClear.setObjectName("pushButtonPortsClear")
        self.spinBoxPortsLast = QtWidgets.QSpinBox(self.groupBoxPorts)
        self.spinBoxPortsLast.setGeometry(QtCore.QRect(30, 170, 71, 29))
        self.spinBoxPortsLast.setObjectName("spinBoxPortsLast")
        self.pushButtonPortsCopy = QtWidgets.QPushButton(self.groupBoxPorts)
        self.pushButtonPortsCopy.setGeometry(QtCore.QRect(120, 80, 81, 31))
        self.pushButtonPortsCopy.setObjectName("pushButtonPortsCopy")
        self.checkBoxPortsEnabled = QtWidgets.QCheckBox(self.groupBoxPorts)
        self.checkBoxPortsEnabled.setGeometry(QtCore.QRect(220, 90, 93, 20))
        self.checkBoxPortsEnabled.setObjectName("checkBoxPortsEnabled")
        self.groupBoxIPRange = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxIPRange.setGeometry(QtCore.QRect(10, 10, 541, 241))
        self.groupBoxIPRange.setObjectName("groupBoxIPRange")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBoxIPRange)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 70, 271, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutIPRangeFirst = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayoutIPRangeFirst.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutIPRangeFirst.setObjectName("horizontalLayoutIPRangeFirst")
        self.spinBoxIPRangeFirst1 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxIPRangeFirst1.setObjectName("spinBoxIPRangeFirst1")
        self.horizontalLayoutIPRangeFirst.addWidget(self.spinBoxIPRangeFirst1)
        self.spinBoxIPRangeFirst2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxIPRangeFirst2.setObjectName("spinBoxIPRangeFirst2")
        self.horizontalLayoutIPRangeFirst.addWidget(self.spinBoxIPRangeFirst2)
        self.spinBoxIPRangeFirst3 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxIPRangeFirst3.setObjectName("spinBoxIPRangeFirst3")
        self.horizontalLayoutIPRangeFirst.addWidget(self.spinBoxIPRangeFirst3)
        self.spinBoxIPRangeFirst4 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxIPRangeFirst4.setObjectName("spinBoxIPRangeFirst4")
        self.horizontalLayoutIPRangeFirst.addWidget(self.spinBoxIPRangeFirst4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxIPRange)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 160, 271, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayoutIPRangeLast = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayoutIPRangeLast.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutIPRangeLast.setObjectName("horizontalLayoutIPRangeLast")
        self.spinBoxIPRangeLast1 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBoxIPRangeLast1.setObjectName("spinBoxIPRangeLast1")
        self.horizontalLayoutIPRangeLast.addWidget(self.spinBoxIPRangeLast1)
        self.spinBoxIPRangeLast2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBoxIPRangeLast2.setObjectName("spinBoxIPRangeLast2")
        self.horizontalLayoutIPRangeLast.addWidget(self.spinBoxIPRangeLast2)
        self.spinBoxIPRangeLast3 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBoxIPRangeLast3.setObjectName("spinBoxIPRangeLast3")
        self.horizontalLayoutIPRangeLast.addWidget(self.spinBoxIPRangeLast3)
        self.spinBoxIPRangeLast4 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBoxIPRangeLast4.setObjectName("spinBoxIPRangeLast4")
        self.horizontalLayoutIPRangeLast.addWidget(self.spinBoxIPRangeLast4)
        self.labelIPRangeFirst = QtWidgets.QLabel(self.groupBoxIPRange)
        self.labelIPRangeFirst.setGeometry(QtCore.QRect(40, 50, 64, 15))
        self.labelIPRangeFirst.setObjectName("labelIPRangeFirst")
        self.labelIPRangeLast = QtWidgets.QLabel(self.groupBoxIPRange)
        self.labelIPRangeLast.setGeometry(QtCore.QRect(40, 140, 64, 15))
        self.labelIPRangeLast.setObjectName("labelIPRangeLast")
        self.pushButtonIPRangeCopy = QtWidgets.QPushButton(self.groupBoxIPRange)
        self.pushButtonIPRangeCopy.setGeometry(QtCore.QRect(330, 80, 81, 31))
        self.pushButtonIPRangeCopy.setObjectName("pushButtonIPRangeCopy")
        self.pushButtonIPRangeClear = QtWidgets.QPushButton(self.groupBoxIPRange)
        self.pushButtonIPRangeClear.setGeometry(QtCore.QRect(330, 170, 84, 31))
        self.pushButtonIPRangeClear.setObjectName("pushButtonIPRangeClear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 27))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scanner"))
        self.pushButtonControlButtonsScan.setText(_translate("MainWindow", "Scan"))
        self.pushButtonControlButtonsCancel.setText(_translate("MainWindow", "Cancel"))
        self.pushButtonControlButtonsQuit.setText(_translate("MainWindow", "Quit"))
        self.groupBoxPorts.setTitle(_translate("MainWindow", "Ports"))
        self.labelPortsFirst.setText(_translate("MainWindow", "First"))
        self.labelPortsLast.setText(_translate("MainWindow", "Last"))
        self.pushButtonPortsClear.setText(_translate("MainWindow", "Clear"))
        self.pushButtonPortsCopy.setText(_translate("MainWindow", "Copy"))
        self.checkBoxPortsEnabled.setText(_translate("MainWindow", "Enabled"))
        self.groupBoxIPRange.setTitle(_translate("MainWindow", "IP Range"))
        self.labelIPRangeFirst.setText(_translate("MainWindow", "First"))
        self.labelIPRangeLast.setText(_translate("MainWindow", "Last"))
        self.pushButtonIPRangeCopy.setText(_translate("MainWindow", "Copy"))
        self.pushButtonIPRangeClear.setText(_translate("MainWindow", "Clear"))
        self.menuAbout.setTitle(_translate("MainWindow", "He&lp"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))

