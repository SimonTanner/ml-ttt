import unittest
from ttt.lib.game import Game
from ttt.lib.ttt_board import TicTacToe
from ttt.lib.machine_model import MachinePlayer

class GameTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_a_new_game_is_started_the_player_must_enter_a_name(self):
        self.game = Game('Michelle')
        self.assertEqual(self.game.player_name, 'Michelle')

    def test_a_board_is_created_when_a_new_game_starts(self):
        self.game = Game('Michelle')
        board = self.game.board
        self.assertIsInstance(board, TicTacToe)

    def test_a_machine_player_instance_is_created_when_a_game_starts(self):
        self.game = Game('Helen')
        player_2 = self.game.machine_player
        self.assertIsInstance(player_2, MachinePlayer)

    def test_a_game_chooses_a_player_at_random_to_go_first(self):
        first_turns = []
        test_count = 10
        for i in range(test_count):
            self.game = Game('Helen')
            first_turns.append(self.game.whose_turn)
        self.assertLess(first_turns.count('Helen'), test_count)

    def test_a_player_can_choose_a_space(self):
        self.game = Game('Helen', 'X')
        self.game.whose_turn = 'Helen'
        self.game.choose_space('1')
        self.assertEqual(self.game.board.board['1'], 'X')

    def test_once_a_player_has_taken_their_turn_the_other_player_goes_next(self):
        self.game = Game('Helen', 'X')
        self.game.whose_turn = 'Helen'
        previous_turn = self.game.whose_turn
        self.game.take_turn('4')
        current_turn = self.game.whose_turn
        self.assertNotEqual(previous_turn,current_turn)

    def test_if_a_player_tries_to_choose_a_space_already_taken_game_gives_a_msg_to_choose_again(self):
        self.game = Game('Pete')
        self.game.whose_turn = 'Pete'
        self.game.take_turn('4')
        self.game.whose_turn = 'Pete'
        message = self.game.take_turn('4')
        self.assertEqual(message, 'Sorry that space is already taken')

    def test_the_machine_player_can_take_a_turn(self):
        self.game = Game('Pete')
        test_board = list(range(1, 10))
        self.game.whose_turn = 'machine_player'
        self.game.take_turn()
        self.assertNotEqual(test_board, self.game.board.free_spaces)

    def test_when_a_game_is_won_game_announces_who_won(self):
        player = 'Mary'
        self.game = Game(player)
        for i in range(3):
            self.game.whose_turn = player
            message = self.game.take_turn(str(i + 1))

        self.assertEqual(message, player + ' won!!!')





if __name__ == '__main__':
    unittest.main()
