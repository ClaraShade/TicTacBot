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
        self.squares = [['x', '_', 'x'], ['o', '_', 'o'], ['x', '_', 'x']]
        self.score = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

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
            count_enemies = 0
            count_friends = 0
            for j in range(self.length):
                mark = str(self.squares[i][j])
                if mark == player:
                    count_enemies = count_enemies + 1
                elif mark == '_':
                    pass
                else:
                    count_friends = count_friends + 1
            for j in range(self.length):
                mark = str(self.squares[i][j])
                if mark == '_':
                    if count_enemies == 0:
                        self.score[i][j] = self.score[i][j] + 5
                        if count_friends == self.length - 1:
                            self.score[i][j] = self.score[i][j] + 10000
                    elif count_enemies == self.length - 1:
                        self.score[i][j] = self.score[i][j] + 500
                    else:
                        self.score[i][j] = self.score[i][j] - 5

        print(self.score)

    def eval_cols(self, player):
        for i in range(self.length):
            count_enemies = 0
            count_friends = 0
            for j in range(self.length):
                mark = str(self.squares[j][i])
                if mark == player:
                    count_enemies = count_enemies + 1
                elif mark == '_':
                    pass
                else:
                    count_friends = count_friends + 1
            for j in range(self.length):
                mark = str(self.squares[j][i])
                if mark == '_':
                    if count_enemies == 0:
                        if count_friends == self.length - 1:
                            self.score[j][i] = self.score[j][i] + 10000
                        else:
                            self.score[j][i] = self.score[j][i] + 5
                    elif count_enemies == self.length - 1:
                        self.score[j][i] = self.score[j][i] + 500
                    else:
                        self.score[j][i] = self.score[j][i] - 5

        print(self.score)

    def eval_diag_l(self, player):
        count_enemies = 0
        count_friends = 0
        for i in range(self.length):
            mark = str(self.squares[i][i])
            if mark == player:
                count_enemies = count_enemies + 1
            elif mark == '_':
                pass
            else:
                count_friends = count_friends + 1
        for i in range(self.length):
            mark = str(self.squares[i][i])
            if mark == '_':
                if count_enemies == 0:
                    if count_friends == self.length - 1:
                        self.score[i][i] = self.score[i][i] + 10000
                    else:
                        self.score[i][i] = self.score[i][i] + 5
                elif count_enemies == self.length - 1:
                    self.score[i][i] = self.score[i][i] + 500
                else:
                    self.score[i][i] = self.score[i][i] - 5
        print(self.score)

    def eval_diag_r(self, player):
        count_enemies = 0
        count_friends = 0
        for i in range(self.length):
            mark = str(self.squares[i][i * -1 - 1])
            if mark == player:
                count_enemies = count_enemies + 1
            elif mark == '_':
                pass
            else:
                count_friends = count_friends + 1
        for i in range(self.length):
            mark = str(self.squares[i][i * -1 - 1])
            if mark == '_':
                if count_enemies == 0:
                    if count_friends == self.length - 1:
                        self.score[i][i * -1 - 1] = self.score[i][i * -1 - 1] + 10000
                    else:
                        self.score[i][i * -1 - 1] = self.score[i][i * -1 - 1] + 5
                elif count_enemies == self.length - 1:
                    self.score[i][i * -1 - 1] = self.score[i][i * -1 - 1] + 500
                else:
                    self.score[i][i * -1 - 1] = self.score[i][i * -1 - 1] - 5
        print(self.score)


def evaluate_move(board, player):
    board.eval_rows(player)
    board.eval_cols(player)
    board.eval_diag_l(player)
    board.eval_diag_r(player)
    print(board.score)


new_board = Board(3)
print("Congratulations! You created " + str(3) + "-sided board, which has " + str(9) + " squares.")
print("See your board below:")
new_board.printme()


evaluate_move(new_board, 'o')
