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

class GameScore:
    def __init__(self, length):
        self.length = length
        self.score = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.squares = [['_', '_', 'o'], ['_', 'o', '_'], ['_', '_', '_']]

    def eval_rows(self, player):
        for i in range(self.length):
            count_enemies = 0
            count_friends = 0
            for j in range(self.length):
                mark = str(self.squares[i][j])
                if mark == player:
                    count_friends = count_friends + 1
                elif mark == '_':
                    pass
                else:
                    count_enemies = count_enemies + 1
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


    def eval_cols(self, player):
        for i in range(self.length):
            count_enemies = 0
            count_friends = 0
            for j in range(self.length):
                mark = str(self.squares[j][i])
                if mark == player:
                    count_friends = count_friends + 1
                elif mark == '_':
                    pass
                else:
                    count_enemies = count_enemies + 1
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

    def eval_diag_l(self, player):
        count_enemies = 0
        count_friends = 0
        for i in range(self.length):
            mark = str(self.squares[i][i])
            if mark == player:
                count_friends = count_friends + 1
            elif mark == '_':
                pass
            else:
                count_enemies = count_enemies + 1
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

    def eval_diag_r(self, player):
        count_enemies = 0
        count_friends = 0
        for i in range(self.length):
            mark = str(self.squares[i][i * -1 - 1])
            if mark == player:
                count_friends = count_friends + 1
            elif mark == '_':
                pass
            else:
                count_enemies = count_enemies + 1
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

    def evaluate_move(self, player):
        self.eval_rows(player)
        self.eval_cols(player)
        self.eval_diag_l(player)
        self.eval_diag_r(player)
        print(self.score)


class Board:
    def __init__(self, side):
        self.length = side
        self.squares = [['_', '_', 'o'], ['_', 'o', '_'], ['_', '_', '_']]
        game_score = GameScore(side)
        self.score = game_score


    def evaluate_move(self, player):
        return self.score.evaluate_move(player)

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




def show_move(board):
    moves = {}
    for i in range(board.length):
        for j in range(board.length):
            movetuple = (i + 1, j + 1)
            print(movetuple)
            moves[(i + 1, j + 1)] = board.score.score[i][j]

    print(moves)
    best_move = max(moves, key=moves.get)
    print(best_move)



new_board = Board(3)
print("Congratulations! You created " + str(3) + "-sided board, which has " + str(9) + " squares.")
print("See your board below:")
new_board.printme()

new_board.evaluate_move('x')

print(new_board.score.score)

show_move(new_board)

