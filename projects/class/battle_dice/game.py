import random
from character import Character

class Game:
    "Manages the Dice Battle game logic"

    def __init__(self, player1: Character, player2: Character):
        """Initializes game with two players."""
        self.__player1 = player1
        self.__player2 = player2


    def attack(self, attacker:Character, defender:Character):
        """Performs an attack where the attacker rolls a die to determine damage dealt"""
        dice_roll = random.randint(1,6)
        scaled_attack = dice_roll * attacker.attack_power

        defender.health -= scaled_attack
        if defender.health <= 0:
            defender.health = 0
            print(f"{defender.name} has been defeated!")

        return scaled_attack



    def start_battle(self):
        """Starts a turn based battle between two players"""
        ##want it to be random as to who starts
        self.__turn = random.randint(1,2)
        
        while self.__player1.health > 0 and self.__player2.health > 0:

    