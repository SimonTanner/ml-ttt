from ttt.lib.ttt_board import TicTacToe
from ttt.lib.machine_model import MachinePlayer
import random

class Game():

    def __init__(self, player_name='Human', x_or_o='X'):
        chars = {'X':'0', '0':'X'}
        self.player_name = player_name
        machine_player_char = chars[x_or_o]
        self.board = TicTacToe()
        self.machine_player = MachinePlayer()
        self.players = {player_name : x_or_o, 'machine_player' : machine_player_char}
        self.player_switch = {player_name : 'machine_player', 'machine_player' : player_name}
        self.who_goes_first()
        self.create_render_data()

    def who_goes_first(self):
        self.whose_turn = random.choice(list(self.players.keys()))

    def create_render_data(self, message='Play'):
        self.render_data = {}
        for i in range(1,10):
            num = str(i)
            self.render_data['choice_' + num] = self.board.board[num]
        self.render_data['new_player'] = self.player_name
        self.render_data['current_player'] = self.whose_turn
        self.render_data['message'] = message



    def choose_space(self, choice):
        return self.board.choose_space(str(choice), self.players[self.whose_turn])

    def win_check(self):
        winner_char = self.board.winning_char
        winner = [key for key, value in self.players.items() if value == winner_char][0]
        msg = '%s won!!!' % str(winner)
        return msg

    def take_turn(self, choice=None):
        msg = None
        if self.whose_turn == 'machine_player':
            choice = self.machine_player.choose_option(self.board.free_spaces)
            self.choose_space(choice)
            self.whose_turn = self.player_switch[self.whose_turn]
        elif self.choose_space(choice):
            msg = 'Sorry that space is already taken'
        else:
            self.choose_space(choice)
            self.whose_turn = self.player_switch[self.whose_turn]
        if self.board.win == True:
            msg = self.win_check()
            self.machine_player.game_won()
        self.create_render_data(msg)
        #self.render_data['message'] = msg
        return msg
