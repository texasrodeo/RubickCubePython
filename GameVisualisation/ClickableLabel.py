from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel

class clackableLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent = None):
        QLabel.__init__(self, parent)
        self.color = None

    def set_back_color(self, color):
        self.color = color
        self.setStyleSheet('background-color: ' + color)

    def get_color(self):
        return self.color

    def mousePressEvent(self, QMouseEvent):
             self.clicked.emit()
            # QLabel.mousePressEvent(self, QMouseEvent)

