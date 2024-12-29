import unittest
from game import PokerGame
from deck import Deck
from player import Player

class TestPokerGame(unittest.TestCase):
    def setUp(self):
        self.game = PokerGame()
        self.game.deck = Deck()
        self.game.players = [Player("Player 1"), Player("Player 2")]

    def test_high_card(self):
        self.game.players[0].hand = [('2', 'Hearts'), ('3', 'Diamonds')]
        self.game.players[1].hand = [('4', 'Clubs'), ('5', 'Spades')]
        self.game.community_cards = [('6', 'Hearts'), ('7', 'Diamonds'), ('8', 'Clubs'), ('9', 'Spades'), ('10', 'Hearts')]
        self.game.determine_winner()
        self.assertEqual(self.game.players[1].name, "Player 2")

    def test_pair(self):
        self.game.players[0].hand = [('2', 'Hearts'), ('2', 'Diamonds')]
        self.game.players[1].hand = [('3', 'Clubs'), ('4', 'Spades')]
        self.game.community_cards = [('5', 'Hearts'), ('6', 'Diamonds'), ('7', 'Clubs'), ('8', 'Spades'), ('9', 'Hearts')]
        self.game.determine_winner()
        self.assertEqual(self.game.players[0].name, "Player 1")

    def test_two_pair(self):
        self.game.players[0].hand = [('2', 'Hearts'), ('2', 'Diamonds')]
        self.game.players[1].hand = [('3', 'Clubs'), ('3', 'Spades')]
        self.game.community_cards = [('4', 'Hearts'), ('4', 'Diamonds'), ('5', 'Clubs'), ('6', 'Spades'), ('7', 'Hearts')]
        self.game.determine_winner()
        self.assertEqual(self.game.players[1].name, "Player 2")

    def test_three_of_a_kind(self):
        self.game.players[0].hand = [('2', 'Hearts'), ('2', 'Diamonds')]
        self.game.players[1].hand = [('3', 'Clubs'), ('3', 'Spades')]
        self.game.community_cards = [('3', 'Hearts'), ('4', 'Diamonds'), ('5', 'Clubs'), ('6', 'Spades'), ('7', 'Hearts')]
        self.game.determine_winner()
        self.assertEqual(self.game.players[1].name, "Player 2")

    def test_straight(self):
        self.game.players[0].hand = [('2', 'Hearts'), ('3', 'Diamonds')]
        self.game.players[1].hand = [('4', 'Clubs'), ('5', 'Spades')]
        self.game.community_cards = [('6', 'Hearts'), ('7', 'Diamonds'), ('8', 'Clubs'), ('9', 'Spades'), ('10', 'Hearts')]
        self.game.determine_winner()
        self.assertEqual(self.game.players[1].name, "Player 2")

    def test_flush(self):
        self.game.players[0].hand = [('2', 'Hearts'), ('3', 'Hearts')]
        self.game.players[1].hand = [('4', 'Clubs'), ('5', 'Clubs')]
        self.game.community_cards = [('6', 'Hearts'), ('7', 'Hearts'), ('8', 'Hearts'), ('9', 'Hearts'), ('10', 'Hearts')]
        self.game.determine_winner()
        self.assertEqual(self.game.players[0].name, "Player 1")

    def test_full_house(self):
        self.game.players[0].hand = [('2', 'Hearts'), ('2', 'Diamonds')]
        self.game.players[1].hand = [('3', 'Clubs'), ('3', 'Spades')]
        self.game.community_cards = [('3', 'Hearts'), ('2', 'Clubs'), ('5', 'Diamonds'), ('6', 'Spades'), ('7', 'Hearts')]
        self.game.determine_winner()
        self.assertEqual(self.game.players[1].name, "Player 2")

    def test_four_of_a_kind(self):
        self.game.players[0].hand = [('2', 'Hearts'), ('2', 'Diamonds')]
        self.game.players[1].hand = [('3', 'Clubs'), ('3', 'Spades')]
        self.game.community_cards = [('3', 'Hearts'), ('3', 'Diamonds'), ('5', 'Clubs'), ('6', 'Spades'), ('7', 'Hearts')]
        self.game.determine_winner()
        self.assertEqual(self.game.players[1].name, "Player 2")

    def test_straight_flush(self):
        self.game.players[0].hand = [('2', 'Hearts'), ('3', 'Hearts')]
        self.game.players[1].hand = [('4', 'Hearts'), ('5', 'Hearts')]
        self.game.community_cards = [('6', 'Hearts'), ('7', 'Hearts'), ('8', 'Hearts'), ('9', 'Hearts'), ('10', 'Hearts')]
        self.game.determine_winner()
        self.assertEqual(self.game.players[1].name, "Player 2")

    def test_tie(self):
        self.game.players[0].hand = [('2', 'Hearts'), ('3', 'Diamonds')]
        self.game.players[1].hand = [('2', 'Clubs'), ('3', 'Spades')]
        self.game.community_cards = [('4', 'Hearts'), ('5', 'Diamonds'), ('6', 'Clubs'), ('7', 'Spades'), ('8', 'Hearts')]
        self.game.determine_winner()
        self.assertIsNone(self.game.determine_winner())

if __name__ == '__main__':
    unittest.main()