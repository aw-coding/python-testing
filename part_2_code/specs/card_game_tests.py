
import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.ace_of_spades           = Card("Spades", 1)
        self.four_of_clubs           = Card("Clubs", 4)
        self.small_deck             = [self.ace_of_spades, self.four_of_clubs]

    
    def test_check_for_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.ace_of_spades))

    
    def test_highest_card(self):
        x = CardGame.highest_card(self, self.ace_of_spades, self.four_of_clubs)
        self.assertEqual(self.four_of_clubs, x)


    def test_cards_total(self):
        self.assertEqual("You have a total of 5", CardGame.cards_total(self, self.small_deck))



        
    