from enum import Enum


class Result(Enum):
    win_x = 1
    win_o = 2
    not_finished = 3
    draw = 4


class Move(Enum):
    x_win = 1
    o_win = 2
    not_last = 3


class Square:
    def __init__(self, num, col, row):
        self.num = num
        self.col = col
        self.row = row
        self.is_empty = True
        self.char = '_'

    def __repr__(self):
        return self.char

    def set_x(self):
        self.is_empty = False
        self.char = 'x'

    def set_o(self):
        self.is_empty = False
        self.char = 'o'


class Board:
    def __init__(self, side):
        self.length = side
        self.squares = [['x', '_', 'o'], ['_', '_', '_'], ['_', '_', '_']]
        self.score = [[0,0,0],[0,0,0],[0,0,0]]

    def printme(self):
        rowcount = 0
        for i in self.squares:
            rowcount = rowcount + 1
            if rowcount < 10:
                print("Row "+str(rowcount)+" "+str(i))
            else:
                print("Row" + str(rowcount) + " " + str(i))
        columns = "Column:"
        for i in range(1, self.length+1):
            columns = columns+str(i)+", "
        print(columns)

    def eval_rows(self, player):
        for i in range(self.length):
            counter = 0
            for j in range(self.length):
                mark = str(self.squares[i][j])
                if mark == player:
                    counter = counter + 1
            for j in range(self.length):
                mark = str(self.squares[i][j])
                if mark == '_':
                    if counter == 0:
                        self.score[i][j] = self.score[i][j] +5
                    else:
                        self.score[i][j] = self.score[i][j] - 5
        print(self.score)

    def eval_cols(self, player):
        for i in range(self.length):
            counter = 0
            for j in range(self.length):
                mark = str(self.squares[j][i])
                if mark == player:
                    counter = counter + 1
            for j in range(self.length):
                mark = str(self.squares[j][i])
                if mark == '_':
                    if counter == 0:
                        self.score[j][i] = self.score[j][i] + 5
                    else:
                        self.score[j][i] = self.score[j][i] - 5
        print(self.score)

    def eval_diag_l(self, player):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i])
            if mark == player:
                counter = counter + 1
        for i in range(self.length):
            mark = str(self.squares[i][i])
            if mark == '_':
                if counter == 0:
                    self.score[i][i] = self.score[i][i] + 5
                else:
                    self.score[i][i] = self.score[i][i] - 5
        print(self.score)

    def eval_diag_r(self, player):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i * -1 - 1])
            if mark == player:
                counter = counter + 1
        for i in range(self.length):
            mark = str(self.squares[i][i * -1 - 1])
            if mark == '_':
                if counter == 0:
                    self.score[i][i * -1 - 1] = self.score[i][i * -1 - 1] + 5
                else:
                    self.score[i][i * -1 - 1] = self.score[i][i * -1 - 1] - 5
        print(self.score)


def evaluate_move(board, player):
    board.eval_rows(player)
    board.eval_cols(player)
    board.eval_diag_l(player)
    board.eval_diag_r(player)
    print(board.score)

def change(player):
    if player == 'x':
        player = 'o'
    else:
        player = 'x'
    return player

new_board = Board(3)
print("Congratulations! You created " + str(3) + "-sided board, which has " + str(9) + " squares.")
print("See your board below:")
new_board.printme()

score_list = []

evaluate_move(new_board,'x')