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
        self.squares = [['_', 'x', '_'], ['_', 'x', 'x'], ['x', '_', '_']]

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

    def count_rows(self, player, target):
        for i in range(self.length):
            counter = 0
            for j in range(self.length):
                mark = str(self.squares[i][j])
                if mark == player:
                    counter = counter + 1
                elif mark == '_':
                    move_tuple = (i + 1, j + 1)
            print(counter)
            if counter == target:
                print(move_tuple)
                return move_tuple


    def count_cols(self, player, target):
        for i in range(self.length):
            counter = 0
            for j in range(self.length):
                mark = str(self.squares[j][i])
                if mark == player:
                    counter = counter + 1
                elif mark == '_':
                    move_tuple = (j + 1, i + 1)
            print(counter)
            if counter == target:
                print(move_tuple)
                return move_tuple

    def count_diag_l(self, player, target):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i])
            if mark == player:
                counter = counter + 1
            elif mark == '_':
                move_tuple = (i + 1, i + 1)
        print(counter)
        if counter == target:
            print(move_tuple)
            return move_tuple

    def count_diag_r(self, player, target):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i * -1 - 1])
            if mark == player:
                counter = counter + 1
            elif mark == '_':
                move_tuple = (i + 1, self.length-i)
        print(counter)
        if counter == target:
            print(move_tuple)
            return move_tuple



def count_sth(board, player, target):
    board.count_rows(player, target)
    board.count_cols(player, target)
    board.count_diag_l(player, target)
    board.count_diag_r(player, target)





#    win_move = last_move(board, player)
#    print(win_move)
#    if win_move:
#        return win_move
#    else:
#        if player == 'x':
#            player = 'o'
#        else:
#            player = 'x'
#        win_move = last_move(board, player)
#        if win_move:
#            return win_move
#        else:
#            if board.squares[1][1] == '_':
#                win_move = (2,2)
#                return win_move

new_board = Board(3)
print("Congratulations! You created " + str(3) + "-sided board, which has " + str(9) + " squares.")
print("See your board below:")
new_board.printme()

test_number = count_sth(new_board, 'x', 3)
if test_number == 3:
    print('yesss!')