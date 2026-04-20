import unittest
from unittest.mock import patch
import os
import main
from main import Player


class TestMain(unittest.TestCase):
    
    def setUp(self) -> None:
        num_rounds = 3
        self.round_num = 2
        self.player1 = Player("Player 1", num_rounds)
        self.player1.choice = main.class_assigner("s")
        self.player2 = Player("Player 2", num_rounds)
        self.player2.choice = main.class_assigner("p")
    
    def tearDown(self) -> None:
        if os.path.exists("results.txt"):
            os.remove("results.txt")


    # Test Case 1: class_assigner(choice) assigns Scissors of input is s and so on
    def test_class_assigner_s(self):
        self.assertEqual(main.class_assigner("s").id, 0)
        self.assertEqual(main.class_assigner("s").name, "Scissors")
        self.assertEqual(main.class_assigner("s").symbol, "✂️")
        self.assertEqual(main.class_assigner("s").beats, 1)

    def test_class_assigner_p(self):
        self.assertEqual(main.class_assigner("p").id, 1)
        self.assertEqual(main.class_assigner("p").name, "Paper")
        self.assertEqual(main.class_assigner("p").symbol, "📄")
        self.assertEqual(main.class_assigner("p").beats, 2)

    def test_class_assigner_r(self):
        self.assertEqual(main.class_assigner("r").id, 2)
        self.assertEqual(main.class_assigner("r").name, "Rock")
        self.assertEqual(main.class_assigner("r").symbol, "🪨")
        self.assertEqual(main.class_assigner("r").beats, 0)


    # Test Case 2: winner_validator() validates the winner 
    ## PLAYER 1 TESTS
    def test_winner_validator_player1_sp(self):
        with patch("builtins.print"):
            self.player1.choice = main.class_assigner("s")
            self.player2.choice = main.class_assigner("p")
            main.winner_validator(self.player1, self.player2, 1)
            self.assertEqual(self.player1.wins, 1)
            self.assertEqual(self.player2.loses, 1)

    def test_winner_validator_player1_pr(self):
        with patch("builtins.print"):
            self.player1.choice = main.class_assigner("p")
            self.player2.choice = main.class_assigner("r")
            main.winner_validator(self.player1, self.player2, 1)
            self.assertEqual(self.player1.wins, 1)
            self.assertEqual(self.player2.loses, 1)

    def test_winner_validator_player1_rs(self):
        with patch("builtins.print"):
            self.player1.choice = main.class_assigner("r")
            self.player2.choice = main.class_assigner("s")
            main.winner_validator(self.player1, self.player2, 1)
            self.assertEqual(self.player1.wins, 1)
            self.assertEqual(self.player2.loses, 1)

    ## PLAYER 2 TESTS
    def test_winner_validator_player2_sp(self):
        with patch("builtins.print"):
            self.player2.choice = main.class_assigner("s")
            self.player1.choice = main.class_assigner("p")
            main.winner_validator(self.player1, self.player2, 1)
            self.assertEqual(self.player2.wins, 1)
            self.assertEqual(self.player1.loses, 1)

    def test_winner_validator_player2_pr(self):
        with patch("builtins.print"):
            self.player2.choice = main.class_assigner("p")
            self.player1.choice = main.class_assigner("r")
            main.winner_validator(self.player1, self.player2, 1)
            self.assertEqual(self.player2.wins, 1)
            self.assertEqual(self.player1.loses, 1)

    def test_winner_validator_player2_rs(self):
        with patch("builtins.print"):
            self.player2.choice = main.class_assigner("r")
            self.player1.choice = main.class_assigner("s")
            main.winner_validator(self.player1, self.player2, 1)
            self.assertEqual(self.player2.wins, 1)
            self.assertEqual(self.player1.loses, 1)

    ## TIE TESTS
    def test_winner_validator_tie_scissors(self):
        with patch("builtins.print"):
            self.player1.choice = main.class_assigner("s")
            self.player2.choice = main.class_assigner("s")
            main.winner_validator(self.player1, self.player2, 1)
            self.assertEqual(self.player1.ties, 1)
            self.assertEqual(self.player2.ties, 1)

    def test_winner_validator_tie_paper(self):
        with patch("builtins.print"):
            self.player1.choice = main.class_assigner("p")
            self.player2.choice = main.class_assigner("p")
            main.winner_validator(self.player1, self.player2, 1)
            self.assertEqual(self.player1.ties, 1)
            self.assertEqual(self.player2.ties, 1)

    def test_winner_validator_tie_rock(self):
        with patch("builtins.print"):
            self.player1.choice = main.class_assigner("r")
            self.player2.choice = main.class_assigner("r")
            main.winner_validator(self.player1, self.player2, 1)
            self.assertEqual(self.player1.ties, 1)
            self.assertEqual(self.player2.ties, 1)


    # Test Case 3: write_round_results() writes the round winner to the file
    def test_write_round_results_tie(self):
        main.write_round_results(None, self.round_num)
        with open("results.txt") as f:
            output = f.read()
        self.assertRegex(output, f"Round {self.round_num}: Tied")

    def test_write_round_results_p1_winner(self):
        main.write_round_results(self.player1, self.round_num)
        with open("results.txt") as f:
            output = f.read()
        self.assertRegex(output, f"Round {self.round_num} winner: {self.player1.player_name} - {self.player1.choice.description}")

    def test_write_round_results_p2_winner(self):
        main.write_round_results(self.player2, self.round_num)
        with open("results.txt") as f:
            output = f.read()
        self.assertRegex(output, f"Round {self.round_num} winner: {self.player2.player_name} - {self.player2.choice.description}")


    # Test Case 4: write_game_results() writes the game winner to the file  
    def test_write_game_results_p1(self):
        with patch("builtins.print"):
            self.player1.wins = 2
            self.player2.wins = 1
            main.write_game_results(self.player1, self.player2)
            with open("results.txt") as f:
                output = f.read()
            self.assertRegex(output, "Player 1 WINS!")

    def test_write_game_results_p2(self):
        with patch("builtins.print"):
            self.player1.wins = 1
            self.player2.wins = 2
            main.write_game_results(self.player1, self.player2)
            with open("results.txt") as f:
                output = f.read()
            self.assertRegex(output, "Player 2 WINS!")

    def test_write_game_results_tie(self):
        with patch("builtins.print"):
            self.player1.wins = 2
            self.player2.wins = 2
            main.write_game_results(self.player1, self.player2)
            with open("results.txt") as f:
                output = f.read()
            self.assertRegex(output, "It's a TIE!")


if __name__ == "__main__":
    unittest.main(verbosity=2)