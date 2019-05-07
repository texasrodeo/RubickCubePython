from PyQt5.QtWidgets import QWidget,QGridLayout, QMessageBox
from PyQt5.QtCore import pyqtSignal, Qt, QSignalMapper, pyqtSlot
from GameVisualisation.ClickableLabel import clackableLabel

class field(QWidget):

    turns_left = pyqtSignal(int)

    def __init__(self,game , parent=None):
        self.game = game
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 400)
        self.end_game = self.game.is_game_ended

        self.grid = self.init_map()
        self.setLayout(self.grid)
        self.set_mapper()

    # def __init_squares(self):
    #     self.squares =
    #
    # def __init_square(self, index):
    #     return [i for i in range(8*index, )]


    @pyqtSlot(int)
    def on_click(self, index):
        if not self.end_game:
            square_num = 0
            # if index in [i for i in range(8)]:
            #     square_num = 0
            # elif index in [i for i in range(8, 16)]:
            #     square_num = 1
            # elif index in [i for i in range(16, 25)]:
            #     square_num = 2
            # elif index in [i for i in range(25, 33)]:
            #     square_num = 3
            # elif index in [i for i in range(33, 41)]:
            #     square_num = 4
            square_num = index
            self.game.click(square_num)
            self.re_paint(square_num)
            self.turns_left.emit(self.game.get_turns_left)
            self.check_game()


    def check_game(self):
        if self.game.is_game_ended:
            self.end_game = True
            if self.game.get_win_info:
                self.msg = self.show_messagebox("You won")
                self.msg.show()
            elif self.game.get_loss_info:
                self.msg = self.show_messagebox("You lost")
                self.msg.show()


    def show_messagebox(self, str):
        msg = QMessageBox()
        msg.setFixedSize(150, 150)
        msg.setText(str)
        msg.setWindowTitle("Game's over")
        return msg

    def re_paint(self, index):
        COLORS = self.game.collect_colors_in_square(index)
        square = self.game.get_square_by_index(index)
        i = 0
        for x in square:
            self.grid.itemAtPosition(x[0]*2, x[1]*2).widget().set_back_color(COLORS[i])
            i += 1


    def set_mapper(self): #сначала в маппер левую верхнюю грань потом правую верхнюю
        #центральную, правую нижнюю, левую нижнюю
        self.smap = QSignalMapper(self)
        i = 0
        i = self.set_mapper_square(0, 3, 0, 3, i)#, [2, 2])
        i = self.set_mapper_square(0, 3, 4, 7, i)#, [2, 4])

        i = self.set_mapper_square(4, 7, 0, 3, i)#, [4, 2])
        i = self.set_mapper_square(4, 7, 4, 7, i)#, [4, 4])
        i = self.set_mapper_square(2, 5, 2, 5, i)
        self.smap.mapped.connect(self.on_click)

    def set_mapper_square(self, left, right, up, down, i):
        for x in range(left,right):
            for k in range(up, down):
                    self.grid.itemAtPosition(x, k).widget().clicked.connect(self.smap.map)
                    self.smap.setMapping(self.grid.itemAtPosition(x, k).widget(), i)
        i += 1
        return i

    def init_map(self):
        grid = QGridLayout()
        grid.setSpacing(0)
        i = 0
        j = 0
        for x in self.__construct_matrix(self.game.get_matrix):
            for k in x:
                l = clackableLabel()
                l.set_back_color(k)
                grid.addWidget(l, i, j)
                j += 1
            i += 1
            j = 0
        return grid

    def __construct_matrix(self, matrix):
        matrix = [self.__set_row(matrix, i) if i not in [1,3,5] else ['grey' for k in range(7)] for i in range(7)]
        for i in range(7):
            if i in [0,1,5,6]:
                matrix[3][i] = 'black'
                matrix[i][3] = 'black'
        return matrix

    def __set_row(self, matrix, j):

        return [matrix[j // 2][i // 2] if i in [0,2,4,6] else 'grey' for i in range(7)]