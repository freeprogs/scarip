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

from PyQt5.QtCore import (QObject,
                          pyqtSignal,
                          QThread,
                          QTimer)

import ipaddress
import subprocess
import re


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
        ip_first = '{}.{}.{}.{}'.format(
            self.spinBoxIPRangeFirst1.value(),
            self.spinBoxIPRangeFirst2.value(),
            self.spinBoxIPRangeFirst3.value(),
            self.spinBoxIPRangeFirst4.value())
        ip_last = '{}.{}.{}.{}'.format(
            self.spinBoxIPRangeLast1.value(),
            self.spinBoxIPRangeLast2.value(),
            self.spinBoxIPRangeLast3.value(),
            self.spinBoxIPRangeLast4.value())
        port_first = self.spinBoxPortsFirst.value()
        port_last = self.spinBoxPortsLast.value()
        if self.checkBoxPortsEnabled.isChecked():
            textfmt = ('Scan from {} to {}'
                       ' with ports from {} to {}')
            text = textfmt.format(
                ip_first,
                ip_last,
                port_first,
                port_last)
        else:
            textfmt = ('Scan from {} to {}'
                       ' ping only')
            text = textfmt.format(
                ip_first,
                ip_last)
        self.textLog.setText(text)

        if self.checkBoxPortsEnabled.isChecked():
            scan_settings = ScanSettings((ip_first, ip_last), (port_first, port_last))
        else:
            scan_settings = ScanSettings((ip_first, ip_last), None)

        self.thread = QThread(self)
        self.worker = ScanTask(scan_settings)
        thread = self.thread
        worker = self.worker
        worker.moveToThread(thread)
        worker.message[str].connect(self.onScanTaskMessageSignal)
        thread.started.connect(worker.process)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        thread.start()

    def onScanTaskMessageSignal(self, text):
        self.textLog.append(text)

    def onCancelButtonClicked(self):
        self.textLog.append('cancel')
        self.worker.terminate()

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


class ScanSettings:

    def __init__(self, ip_range, port_range):
        self.ip_range = ip_range
        self.port_range = port_range

    def get_ip_first(self):
        return self.ip_range and self.ip_range[0]

    def get_ip_last(self):
        return self.ip_range and self.ip_range[1]

    def get_port_first(self):
        return self.port_range and self.port_range[0]

    def get_port_last(self):
        return self.port_range and self.port_range[1]


class ScanTask(QObject):

    message = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, settings):
        super().__init__()
        self.ip_first = ipaddress.IPv4Address(settings.get_ip_first())
        self.ip_last = ipaddress.IPv4Address(settings.get_ip_last())
        self.port_first = settings.get_port_first()
        self.port_last = settings.get_port_last()
        self.pinger = Pinger()
        self.port_scanner = PortScanner()
        self.f_scan_in_process = False

    def process(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.onTimeout)
        self.timer.start(100)

    def onTimeout(self):
        if not self.f_scan_in_process:
            if self.ip_first <= self.ip_last:
                self.f_scan_in_process = True
                self.message.emit('ip ' + str(self.ip_first))
                retc, rets = self.pinger.ping(str(self.ip_first), 1, 3)
                self.message.emit(rets if retc else 'none')
                cur_port = self.port_first
                if retc and cur_port is not None:
                    while cur_port <= self.port_last:
                        self.message.emit('port ' + str(cur_port))
                        ret = self.port_scanner.is_opened(str(self.ip_first), cur_port)
                        self.message.emit('yes' if ret else 'no')
                        cur_port += 1
                self.ip_first += 1
                self.f_scan_in_process = False
            else:
                self.timer.stop()
                self.finished.emit()

    def terminate(self):
        self.pinger.terminate()
        self.port_scanner.terminate()
        self.finished.emit()


class Pinger:

    def __init__(self):
        self.p = None

    def ping(self, address, npackets, timeout):
        retok, ms = False, None
        args = ['ping',
                '-q',
                '-c', str(npackets),
                '-w', str(int(timeout / 1000)),
                address]
        self.p = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        p = self.p
        with p:
            p.wait()
            retok = p.returncode == 0
            if retok:
                stdout = p.communicate()[0].decode('latin1')
                olastline = stdout.splitlines()[-1]
                ms = olastline.rsplit('/')[-3]
        return (retok, ms)

    def terminate(self):
        if self.p is not None:
            self.p.terminate()
            self.p = None


class PortScanner:

    def __init__(self):
        self.p = None

    def is_opened(self, address, port):
        args = ['nmap',
                '-p',
                str(port),
                address]
        self.p = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        p = self.p
        with p:
            p.wait()
            retok = p.returncode == 0
            if retok:
                stdout = p.communicate()[0].decode('latin1')
                pat = r'^{}/tcp +open +\S+$'.format(port)
                mobj = re.search(pat, stdout, flags=re.M)
        return retok and mobj is not None

    def terminate(self):
        if self.p is not None:
            self.p.terminate()
            self.p = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
