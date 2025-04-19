from project1.multideck import MultiDeck
from project1.card import Card

import random


class Hand():

    def __init__(self):
        self.cards = []

    def add_card(self,card):
        self.cards.append(card)

    def total(self):
        total = 0
        for card in self.cards:
            value = card.get_value(card.face)
            if card.face == 'A' and total <= 10:
                value = value[1]
            else:
                value = value[0]
                total += value

        return total 

