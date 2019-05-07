from PyQt5.QtWidgets import QLabel, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from GameVisualisation.LabelForLegend import myLabel
from GameVisualisation.Field import field

class playingField(QWidget):



    def __init__(self, game):
        super().__init__()

        self.initUI(game)

    def initUI(self, game):

        self.setFixedSize(800, 600)
        self.place_image()
        self.parse_game(game)
        self.place_turns_label()
        self.change_turns_count(game.get_turns_left)
        self.place_difficulty(game)


    def parse_game(self, game):
        self.field = field(game, self)
        self.field.turns_left[int].connect(self.change_turns_count)
        self.field.move(self.rect().center().x() - self.field.width()/2, self.rect().center().y() - self.field.height()/2)

    def place_image(self):
        pixmap = QPixmap('GameVisualisation/resources/image_pygame.jpg')
        label = QLabel(self)
        label.resize(self.width(), self.height())
        label.setPixmap(pixmap)

    def place_difficulty(self, game):
        self.label_diff = myLabel(self)
        self.label_diff.set_text_color("White")
        self.label_diff.setFont(QFont("Times", 14, QFont.StyleItalic))
        self.label_diff.setText("level: " + game.get_difficulty_name)
        self.label_diff.resize(self.label_diff.sizeHint())


    def place_turns_label(self):
        self.label_turns = myLabel(self)
        self.label_turns.set_text_color("White")
        self.label_turns.setFont(QFont("Times", 14, QFont.StyleItalic))
        self.label_turns.move(0, 30)
       # self.label_turns.resize(self.label_turns.sizeHint())

    #
    def change_turns_count(self, value):
        if value < 0:
            value = 'infinity'
        self.label_turns.setText("turns left: " + str(value))