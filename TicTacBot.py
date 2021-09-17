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
    def rows_to_win(self):
        for i in range(self.length):
            counter = 0
            for j in range(self.length):
                mark = str(self.squares[i][j])
                if mark == 'x':
                    counter = counter + 1
                elif mark == 'o':
                    counter = counter - 1
                else:
                    pass
            if counter == int(self.length * -1 + 1):
                move_tuple = (i + 1, j + 1)
                print(move_tuple)
                self.move = Move.o_win
                return move_tuple

    def cols_to_win(self):
        for i in range(self.length):
            counter = 0
            for j in range(self.length):
                mark = str(self.squares[j][i])
                if mark == 'x':
                    counter = counter + 1
                elif mark == 'o':
                    counter = counter - 1
                else:
                    pass
            if counter == int(self.length * -1 + 1):
                move_tuple = (j + 1, i + 1)
                print(move_tuple)
                self.move = Move.o_win
                return move_tuple

    def diag_l_to_win(self):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i])
            if mark == 'x':
                counter = counter + 1
            elif mark == 'o':
                counter = counter - 1
            else:
                pass
            if counter == int(self.length * -1 + 1):
                move_tuple = (i + 1, i + 1)
                print(move_tuple)
                self.move = Move.o_win
                return move_tuple

    def diag_r_to_win(self):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i * -1 - 1])
            if mark == 'x':
                counter = counter + 1
            elif mark == 'o':
                counter = counter - 1
            else:
                pass
        if counter == int(self.length * -1 + 1):
            move_tuple = (i + 1, i + 1)
            print(move_tuple)
            self.move = Move.o_win
            return move_tuple

    def rows_to_block(self):
        for i in range(self.length):
            counter = 0
            for j in range(self.length):
                mark = str(self.squares[i][j])
                if mark == 'x':
                    counter = counter + 1
                elif mark == 'o':
                    counter = counter - 1
                else:
                    pass
            if counter == int(self.length-1):
                for j in range(self.length):
                    mark = str(self.squares[i][j])
                    if mark == '_':
                        move_tuple = (i + 1, j + 1)
                        print(move_tuple)
                        self.move = Move.o_win
                        return move_tuple

    def cols_to_block(self):
        for i in range(self.length):
            counter = 0
            for j in range(self.length):
                mark = str(self.squares[j][i])
                if mark == 'x':
                    counter = counter + 1
                elif mark == 'o':
                    counter = counter - 1
                else:
                    pass
            if counter == int(self.length - 1):
                for i in range(self.length):
                    mark = str(self.squares[i][j])
                    if mark == '_':
                        move_tuple = (i + 1, j + 1)
                        print(move_tuple)
                        self.move = Move.o_win
                        return move_tuple

    def diag_l_to_block(self):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i])
            if mark == 'x':
                counter = counter + 1
            elif mark == 'o':
                counter = counter - 1
            else:
                pass
            if counter == int(self.length-1):
                for i in range(self.length):
                    mark = str(self.squares[i][i])
                    if mark == '_':
                        move_tuple = (i + 1, i + 1)
                        print(move_tuple)
                        self.move = Move.o_win
                        return move_tuple

    def diag_r_to_block(self):
        counter = 0
        for i in range(self.length):
            mark = str(self.squares[i][i * -1 - 1])
            print(mark)
            if mark == 'x':
                counter = counter + 1
            elif mark == 'o':
                counter = counter - 1
            else:
                pass
        if counter == int(self.length-1):
            for i in range(self.length):
                mark = str(self.squares[i][i * -1 - 1])
                print(mark)
                if mark == '_':
                    move_tuple = (i+1,i*-1+3)
                    print(move_tuple)
                    self.move = Move.o_win
                    return move_tuple

                    #move_tuple = (i, i)
                    #print(move_tuple)
                    #self.move = Move.o_win
                    #return move_tuple

    def try_win(self):
        self.rows_to_win()
        self.cols_to_win()
        self.diag_l_to_win()
        self.diag_r_to_win()

    def try_block(self):
        self.rows_to_block()
        self.cols_to_block()
        self.diag_l_to_block()
        self.diag_r_to_block()

def enemy(board):
    board.try_win()
    board.try_block()





new_board = Board(3)
print("Congratulations! You created " + str(3) + "-sided board, which has " + str(9) + " squares.")
print("See your board below:")
new_board.printme()

mytuple = enemy(new_board)