import random as rnd

def change_colors(COLORS):
    return COLORS[-1:] + COLORS[:-1]

def get_random_COLORS():
    COLORS = ["red", "yellow", "green", "blue"]
    for i in range(4):
        a = rnd.randint(0, 3)
        b = rnd.randint(0, 3)
        COLORS[a], COLORS[b] = COLORS[b], COLORS[a]
        return COLORS


def set_matrix():
        matrix = [set_row() for i in range(4)]
        # matrix = [set_row() if i not in [1,3,5] else ['grey' for k in range(7)] for i in range(7)]
        # for i in range(7):
        #     if i in [0,1,5,6]:
        #         matrix[3][i] = 'black'
        #         matrix[i][3] = 'black'
        return matrix

def set_row():
        COLORS = get_random_COLORS()
        return [COLORS[i] for i in range(4)]
       # return [COLORS[i//2]  if i in [0,2,4,6] else 'grey' for i in range(7)]

def get_squares():
    return [get_square(i) for i in range(5)]

def get_square(index):
    #return [[index, index], [index, index + 1], [index + 1, index+1], [index + 1, index]]
    if index == 0: return [[0,0],[0,1],[1,1],[1,0]]
    elif index == 1 : return [[0,2],[0,3],[1,3],[1,2]]
    elif index == 4 : return [[1,1],[1,2],[2,2],[2,1]]
    elif index == 2 : return [[2,0],[2,1],[3,1],[3,0]]
    elif index == 3 : return [[2,2],[2,3],[3,3],[3,2]]


def construct_matrix(COLORS):
    index = 0
    matrix = [[None] *4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = COLORS[index]
            index+=1
    return matrix