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
        self.squares = [['_', 'x', 'o'], ['_', '_', '_'], ['_', 'o', 'x']]

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
            if counter == target:
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
            if counter == target:
                return move_tuple

    def count_diag_l(self, player, target):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i])
            if mark == player:
                counter = counter + 1
            elif mark == '_':
                move_tuple = (i + 1, i + 1)
        if counter == target:
            return move_tuple

    def count_diag_r(self, player, target):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i * -1 - 1])
            if mark == player:
                counter = counter + 1
            elif mark == '_':
                move_tuple = (i + 1, self.length-i)
        if counter == target:
            return move_tuple


def evaluate_move(board, player, target):
    move = board.count_rows(player, target)
    if move:
        return move
    else:
        move = board.count_cols(player, target)
        if move:
            return move
        else:
            move = board.count_diag_l(player, target)
            if move:
                return move
            else:
                move = board.count_diag_r(player, target)
                if move:
                    return move

def change(player):
    if player == 'x':
        player = 'o'
    else:
        player = 'x'
    return(player)

def enemy(board, player):
    winning_move = evaluate_move(board, player, board.length - 1)
    if winning_move:
        print('Win!')
        print(winning_move)
        return winning_move
    else:
        player = change(player)
        blocking_move = evaluate_move(board, player, board.length - 1)
        if blocking_move:
            print('Block!')
            print(blocking_move)
            return blocking_move
        else:
            player = change(player)
            for i in range(board.length - 2):
                free_move = evaluate_move(board, player, i)
                if free_move:
                    print('Free move!')
                    print(free_move)
                    return free_move


new_board = Board(3)
print("Congratulations! You created " + str(3) + "-sided board, which has " + str(9) + " squares.")
print("See your board below:")
new_board.printme()

enemy(new_board, 'x')