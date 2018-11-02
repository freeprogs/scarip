#!/usr/bin/env python3

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

import sys
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QDesktopWidget,
                             QMessageBox)
from mainwindow import Ui_MainWindow

from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QStatusTipEvent


class App(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setup_ui()
        self.center()
        self.show()

    def center(self):
        rect = self.frameGeometry()
        best_position = QDesktopWidget().availableGeometry().center()
        rect.moveCenter(best_position)
        self.move(rect.topLeft())

    def setup_ui(self):
        self.setup_ui_menu()
        self.setup_ui_statusbar()
        self.setup_ui_control_buttons()
        self.setup_ui_iprange_frame()
        self.setup_ui_ports_frame()

    def setup_ui_menu(self):
        self.actionAbout.triggered.connect(self.print_about)

    def setup_ui_statusbar(self):
        self.statusbar.showMessage('Ready for scan')

    def setup_ui_control_buttons(self):
        self.pushButtonControlButtonsScan.clicked.connect(self.onScanButtonClicked)
        self.pushButtonControlButtonsCancel.clicked.connect(self.onCancelButtonClicked)
        self.pushButtonControlButtonsQuit.clicked.connect(self.onQuitButtonClicked)

    def setup_ui_iprange_frame(self):
        self.pushButtonIPRangeCopy.clicked.connect(self.onIPRangeCopyButtonClicked)
        self.pushButtonIPRangeClear.clicked.connect(self.onIPRangeClearButtonClicked)

    def setup_ui_ports_frame(self):
        self.checkBoxPortsEnabled.setChecked(True)
        self.checkBoxPortsEnabled.stateChanged.connect(self.onTogglePorts)
        self.pushButtonPortsCopy.clicked.connect(self.onPortsCopyButtonClicked)
        self.pushButtonPortsClear.clicked.connect(self.onPortsClearButtonClicked)

    def event(self, e):
        if e.type() == QEvent.StatusTip:
            if e.tip() == '':
                e = QStatusTipEvent(self.statusbar.currentMessage())
        return super().event(e)

    def print_about(self):
        QMessageBox.about(self, 'About', 'This is a scanner.')

    def onScanButtonClicked(self):
        print('scan')

    def onCancelButtonClicked(self):
        print('cancel')

    def onQuitButtonClicked(self):
        self.close()

    def onIPRangeCopyButtonClicked(self):
        self.spinBoxIPRangeLast1.setValue(self.spinBoxIPRangeFirst1.value())
        self.spinBoxIPRangeLast2.setValue(self.spinBoxIPRangeFirst2.value())
        self.spinBoxIPRangeLast3.setValue(self.spinBoxIPRangeFirst3.value())
        self.spinBoxIPRangeLast4.setValue(self.spinBoxIPRangeFirst4.value())

    def onIPRangeClearButtonClicked(self):
        self.spinBoxIPRangeFirst1.setValue(0)
        self.spinBoxIPRangeFirst2.setValue(0)
        self.spinBoxIPRangeFirst3.setValue(0)
        self.spinBoxIPRangeFirst4.setValue(0)
        self.spinBoxIPRangeLast1.setValue(0)
        self.spinBoxIPRangeLast2.setValue(0)
        self.spinBoxIPRangeLast3.setValue(0)
        self.spinBoxIPRangeLast4.setValue(0)

    def onTogglePorts(self):
        if self.checkBoxPortsEnabled.isChecked():
            self.pushButtonPortsClear.setDisabled(False)
            self.pushButtonPortsCopy.setDisabled(False)
            self.labelPortsFirst.setDisabled(False)
            self.spinBoxPortsFirst.setDisabled(False)
            self.labelPortsLast.setDisabled(False)
            self.spinBoxPortsLast.setDisabled(False)
        else:
            self.pushButtonPortsClear.setDisabled(True)
            self.pushButtonPortsCopy.setDisabled(True)
            self.labelPortsFirst.setDisabled(True)
            self.spinBoxPortsFirst.setDisabled(True)
            self.labelPortsLast.setDisabled(True)
            self.spinBoxPortsLast.setDisabled(True)

    def onPortsCopyButtonClicked(self):
        self.spinBoxPortsLast.setValue(self.spinBoxPortsFirst.value())

    def onPortsClearButtonClicked(self):
        self.spinBoxPortsFirst.setValue(0)
        self.spinBoxPortsLast.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
