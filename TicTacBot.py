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
        self.squares = [['_','_','_'], ['_','x','_'], ['x','_','_']]


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


##here new methods
    def rows_to_win(self, player):
        for i in range(self.length):
            counter = 0
            for j in range(self.length):
                mark = str(self.squares[i][j])
                if mark == player:
                    counter = counter + 1
                elif mark == '_':
                    move_tuple = (i + 1, j + 1)
            if counter == int(self.length - 1):
                return move_tuple

    def cols_to_win(self, player):
        for i in range(self.length):
            counter = 0
            for j in range(self.length):
                mark = str(self.squares[j][i])
                if mark == player:
                    counter = counter + 1
                elif mark == '_':
                    move_tuple = (j + 1, i + 1)
            if counter == int(self.length - 1):
                return move_tuple

    def diag_l_to_win(self, player):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i])
            if mark == player:
                counter = counter + 1
            elif mark == '_':
                move_tuple = (i + 1, i + 1)
        if counter == int(self.length - 1):
            return move_tuple

    def diag_r_to_win(self, player):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i * -1 - 1])
            if mark == player:
                counter = counter + 1
            elif mark == '_':
                move_tuple = (i + 1, self.length-i)
        if counter == int(self.length - 1):
            return move_tuple

def enemy(board, player):
    move = board.rows_to_win(player)
    if move:
        return move
    else:
        move = board.cols_to_win(player)
        if move:
            return move
        else:
            move = board.diag_l_to_win(player)
            if move:
                return move
            else:
                move = board.diag_r_to_win(player)
                return move


new_board = Board(3)
print("Congratulations! You created " + str(3) + "-sided board, which has " + str(9) + " squares.")
print("See your board below:")
new_board.printme()

my_move = enemy(new_board,'x')
print(my_move)