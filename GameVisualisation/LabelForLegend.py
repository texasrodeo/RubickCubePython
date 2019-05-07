from PyQt5.QtWidgets import QLabel

class myLabel(QLabel):


    def __init__(self, parent=None):
        QLabel.__init__(self, parent)



    def set_text_color(self, color):
        self.setStyleSheet('color: ' + color)