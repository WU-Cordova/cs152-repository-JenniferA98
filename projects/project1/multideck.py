import random
from datastructures.bag import Bag
from project1.card import Card



class MultiDeck():
    """Handles the storing of multideck for bag jack game"""

    def __init__(self, num_decks:int) -> None:
        self.num_decks = num_decks
        self.bag = Bag()
        self._init_deck()

    def _init_deck(self):
        """Initialize bag w/ cards for multiple decks"""
        suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        faces = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

        for deck in range(self.num_decks):
            for suit in suits:
                for face in faces:
                    card = Card(face,suit)
                    self.bag.add(card)

    def shuffle(self) -> None:
        self.bag.shuffle()

    def draw(self):
        if len(self.bag) > 0:
            card = self.bag.bag_inventory.pop()
            return card
        return None
    
    def count(self) -> int:
        return len(self.bag)
    
    def distinct_cards(self) -> list[str]:
        return [str(card) for card in self.bag.distinct_items()]






