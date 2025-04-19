from project1.hand import Hand
from project1.multideck import MultiDeck

import random


from project1 import multideck


class BagJack():

    def __init__(self):
        """Initailizes the game by selecting number of decks, shuffling and creating player and dealer hands"""
        num_decks = random.randint(1,4) * 2
        self.__player_hand = Hand()
        self.__dealer_hand = Hand()
        self.multi_deck = multideck.MultiDeck(num_decks)
        self.multi_deck.shuffle()



    def game_start(self):
        """Initial Deal"""
        for i in range(2):
            self.__player_hand.add_card(self.multi_deck.draw())
            self.__dealer_hand.add_card(self.multi_deck.draw())

            print("Player's Hand", self.__player_hand.cards, "| Score", self.__player_hand.total())
            print("Dealer's Hand", [self.__dealer_hand.cards[0], "Hidden Card"], "| Score", self.__dealer_hand.total())

    def player_turn(self):
        """Allow player to hit or stay"""
        while self.__player_hand.total() < 21:
            print("\nYour hand:", self.__player_hand.cards, "| Score:", self.__player_hand.total())
            choice = input("Do you want to [H]it or [S]tay").lower()

            if choice == 'h':
                self.__player_hand.add_card(self.multi_deck.draw())
                print("Player's Hand", self.__player_hand.cards, "| Score", self.__player_hand.total())
            elif choice == 's':
                print("You chose to stay")
                break
            else:
                 print("Please enter 'H' to hit or 'S' to stay in order to play.")

        if self.__player_hand.total() > 21:
            print("You bust! Your score is above 21. Game over")
            return False
        return True


    def dealer_turn(self):
        """Dealers turn unitl Score:17 or higher"""
        print("\nDealers turn:")
        while self.__dealer_hand.total() < 17:
            self.__dealer_hand.add_card(self.multi_deck.draw())
            print("Dealer drew a card. Dealers hand:", self.__dealer_hand.cards, "| Score:", self.__dealer_hand.total())
        
                 
    def show_hands(self):
        """Show both player and dealer's hands"""
        print("\nFinal Hands:")
        print("Player's Hand:", self.__player_hand.cards, "| Score:", self.__player_hand.get_total_value())
        print("Dealer's Hand:", self.__dealer_hand.cards, "| Score:", self.__dealer_hand.get_total_value())

    def determine_winner(self):
        """Determine the winner of the game based on hand totals"""
        player_total = self.__player_hand.total()
        dealer_total = self.__dealer_hand.total()

        if player_total > 21:  
            print("Player busts! Dealer wins.")
        elif dealer_total > 21:  
            print("Dealer busts! Player wins.")
        elif player_total > dealer_total:  
            print("Player wins!")
        elif dealer_total > player_total:  
            print("Dealer wins!")
        else:
            print("It's a tie!")


    def play(self):
        """Run the game loop: deal, play player turn, play dealer turn, and determine winner"""
        self.game_start()


        if not self.player_turn():  
            return

    
        self.dealer_turn()

        
        self.show_hands()
        self.determine_winner()
         