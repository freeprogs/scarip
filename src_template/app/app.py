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
        self.actionAbout.triggered.connect(self.print_about)
        self.statusbar.showMessage('Ready for scan')
        self.pushButtonControlButtonsScan.clicked.connect(self.onScanButtonClicked)
        self.pushButtonControlButtonsCancel.clicked.connect(self.onCancelButtonClicked)
        self.pushButtonControlButtonsQuit.clicked.connect(self.onQuitButtonClicked)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
