from PyQt4 import QtGui
from PyQt4 import QtCore

class MerchantGUI(QtGui.QWidget):
    def __init__(self, controller, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.status = QtGui.QLabel()
        self.status.setWordWrap(True)
        self.status.setMinimumHeight(60)
        self.status.setMinimumWidth(400)
        self.status.setText("System ready.")

        self.rate = QtGui.QLabel()
        self.rate.setText("Current exchange rate: ...        ")

        init_demo = QtGui.QPushButton("Init demo")
        self.connect(init_demo, QtCore.SIGNAL('clicked()'), self.init_demo_on_clicked)

        fullscreen = QtGui.QPushButton("Toggle fullscreen")
        self.connect(fullscreen, QtCore.SIGNAL('clicked()'), self.fullscreen_on_clicked)

        hbox1 = QtGui.QHBoxLayout()
        hbox1.addWidget(init_demo)
        hbox1.addWidget(fullscreen)

        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addWidget(self.rate)
        vbox.addWidget(self.status)

        self.setLayout(vbox)
        self.setWindowTitle('Point of Sale System - Backend')

    def fullscreen_on_clicked(self):
        self.controller.toggle_fullscreen_mode()

    def init_demo_on_clicked(self):
        self.controller.init_demo()

    def update_status(self, message):
        self.status.setText(message)

    def update_exchange_rate(self, rate):
        self.rate.setText("Current exchange rate: %f USD" % rate)

    def closeEvent(self, event):
        event.accept()
        QtGui.QApplication.exit()
