import math

class TicTacToe():

    def __init__(self):

        self.board = []
        self.free_spaces = []
        self.create_board()

    def space_array_create(self):
        for i in range(1,10):
            self.free_spaces.append(i)

    def create_board(self):
        board = self.board
        for row in range(3):
            board.append([])
            for column in range(3):
                board[row].append('.')

        self.space_array_create()

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def input_marker(row, column, input_type):
        self.board[row][column] = input_type
        self.print_board(board)

    def win_check_row(self, letter):
        for r in self.board:
          if r[0] == r[1] == r[2] == letter:
            return('win')


    def win_check_column(self, letter):
        board = self.board
        for c in range(0, len(board[0])):
          if board[0][c] == board[1][c] == board[2][c] == letter:
            return('win')


    def win_check_diag(self, letter):
        board = self.board
        if board[0][0] == board[1][1] == board[2][2] == letter:
            return("win")
        elif board[0][2] == board[1][1] == board[2][0] == letter:
            return("win")
        else:
            return False

    def win_check(self, letter):
        if self.win_check_row(letter) == "win" or self.win_check_column(letter) == "win" or self.win_check_diag(letter) =="win":
            return "win"

    def receive_input(self, position, letter):
        if isinstance(position, list):
            r, c = position
        else:
            r, c = self.int_to_position(position)

        self.board[r][c] = letter
        self.free_board_space(r,c)


    def free_board_space(self, row, column):
        free_int = row * 3 + 1 + column
        self.free_spaces.remove(free_int)

    def int_to_position(self, num):
        row = math.floor((num - 1) / 3)
        column = num - row * 3 - 1
        return [row, column]
