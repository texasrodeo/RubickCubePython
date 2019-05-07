from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton
from  PyQt5.QtCore import Qt, pyqtSignal


class settingsForm(QWidget):

    difficulty_to_send = pyqtSignal(int)

    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(parent, Qt.Window)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Choose difficulty")
        self.setFixedSize(250, 150)
        self.__set_buttons()
        self.rbEasy = QRadioButton(self)
        self.rbEasy.setText("Easy (turns count = infinty)")
        self.rbEasy.setChecked(True)
        self.rbEasy.resize(self.rbEasy.sizeHint())
        self.rbHard = QRadioButton(self)
        self.rbHard.setText("Hard (turns count = 25)")
        self.rbHard.resize(self.rbHard.sizeHint())
        self.rbSemi = QRadioButton(self)
        self.rbSemi.setText("Semi (turns count = 50 )")
        self.rbSemi.resize(self.rbSemi.sizeHint())

        self.rbEasy.move(20, 20)
        self.rbSemi.move(20, 40)
        self.rbHard.move(20, 60)




    def __set_buttons(self):
        self.OKbtn = QPushButton("Start", self)
        self.OKbtn.clicked.connect(self.__confirm_changes)

        self.OKbtn.move(100, 100)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.OKbtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def __confirm_changes(self):
        if self.rbEasy.isChecked():
           self.difficulty_to_send.emit(0)
        elif self.rbSemi.isChecked():
            self.difficulty_to_send.emit(2)
        elif self.rbHard.isChecked():
            self.difficulty_to_send.emit(1)
        self.close()