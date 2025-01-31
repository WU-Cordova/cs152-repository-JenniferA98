import random
from character import Character

class Game:
    "Manages the Dice Battle game logic"

    def __init__(self, player1: Character, player2: Character):
        """Initializes game with two players."""
        self.__player1 = player1
        self.__player2 = player2


    def attack(self):
        """Performs an attack where the attacker rolls a die to determine damage dealt"""
        dice_roll = random.int(1,6)
        
