from GameFiles.ScriptsForGame import set_matrix, get_squares, change_colors, construct_matrix

#property, приватные поля, матрица 4х4, маппер, сохранение
class game:



    def __init__(self, **kwargs):
        self.__difficulties = ['easy', 'hard', 'medium']
        self.__squares = get_squares()
        if kwargs.get('args') == None:

            self.__matrix = set_matrix()

            self._game_ended = False

            self.__difficulty = kwargs.get('difficulty')
            self.__turns_left = self.get_turns_number()
        else:
            self.__difficulty = kwargs.get('args').get('difficulty')
            self._game_ended = kwargs.get('args').get('game_ended')
            self.__turns_count = self.get_turns_number()
            self.__turns_left = kwargs.get('args').get('turns_left')

            self.__matrix = construct_matrix(kwargs.get('args').get('COLORS'))


    def get_turns_number(self):
       return self.__difficulty * 25 if self.__difficulty > 0 else - 1

    @property
    def get_difficulty(self):
        return self.__difficulty

    @property
    def get_turns_left(self):
        return self.__turns_left if self.__turns_left >= 0 else -1


    @property
    def get_win_info(self):
        return self.__check_game_won()

    @property
    def get_loss_info(self):
        return self.__check_game_lost()


    def click(self, index):
        self.__change_colors(index)
        self.__turns_left -= 1
        self._game_ended = self.__check_game_ended()


    @property
    def is_game_ended(self):
        return self._game_ended

    @property
    def get_matrix(self):
        return self.__matrix

    def __check_game_ended(self):
        return self.__check_game_won() or self.__check_game_lost()


    def __check_game_lost(self):
        return self.__turns_left == 0



    def __check_game_won(self):
       # win = True
        for i in range(len(self.__squares)):
            COLORS = self.collect_colors_in_square(i)
            if len(set(COLORS)) != 1:
                return False
                # win = False
                # break
        return True

    @property
    def get_difficulty_name(self):
        return self.__difficulties[self.__difficulty]



    def get_square_by_index(self, index):
        return self.__squares[index]


    def collect_colors_in_square(self, index):
        return [self.__matrix[x[0]][x[1]] for x in self.__squares[index]]


    def __change_colors(self,index):
        #COLORS = [self.martix[x[0]][x[1]] for x in self.squares[index]]
        COLORS = change_colors(self.collect_colors_in_square(index))
        i = 0
        for x in self.__squares[index]:
            self.__matrix[x[0]][x[1]] = COLORS[i]
            i += 1


