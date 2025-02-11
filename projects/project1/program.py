from project1.game import BagJack


def main():
    print("Welcome to BagJack!")
    
    # Start the game loop
    while True:
        # Create an instance of the game
        game = BagJack()

        # Play a round of the game
        game.play()

        # Ask the player if they want to play another round
        play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break  # Exit the loop and end the game

# Start the game when the script is run
if __name__ == '__main__':
    main()