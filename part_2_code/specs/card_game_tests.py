import unittest
# from part_2_code.src.card import Card
# from part_2_code.src.card_game import CardGame

from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.ace_of_spades =     Card('Spades', 1)
        self.three_of_clubs =    Card('Clubs', 3)
        self.nine_of_hearts =    Card('Hearts', 9)
        self.list_of_cards = [self.ace_of_spades, self.three_of_clubs, self.nine_of_hearts]


    def test_check_for_ace(self):
        #yyp = check_for_ace(self.ace_of_spades)
        pass

    def test_highest_card(self):
        x = highest_card(self.ace_of_spades, self.nine_of_hearts)

    def test_cards_total(self):
        pass
        
    