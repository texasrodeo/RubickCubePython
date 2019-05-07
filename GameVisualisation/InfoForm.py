from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.Qt import Qt

class infoForm(QWidget):

    def __init__(self,parent=None):
        super().__init__(parent, Qt.Window)
        self.initUI()


    def initUI(self):
        self.setFixedSize(750, 250)
        str = '<b>Игра "Плоский кубик Рубика" </b> <br>Цель игры - получить на конца' \
              ' плоских гранях кубика Рубика квадраты одинакового цвета </br>' \
              ' <br> В зависимости от уровня сложности у игрока будет разного количество ходов на прохождение игры</br>' \
              '<br>Грань вращается по часовой стрелке на 90 градусов</br>' \
              '<br>Удачи!</br>'
        self.label = QLabel(str, self)
        self.label.setStyleSheet("QWidget {color: black; background-color: wheat; font-size: 15px}")
        self.label.setFixedSize(750, 250)

