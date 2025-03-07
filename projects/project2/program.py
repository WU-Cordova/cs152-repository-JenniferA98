
from project2.grid import Grid
from project2.gamecontroller import GameController

def main():

    print("Welcome to the Game of Life Simulation!")
    grid = Grid(height=5, width=5)
    game_controller = GameController(grid)

    while True:
        print("\nSelect mode:")
        print("A - Automatic Mode")
        print("M - Manual Mode")
        print("Q - Quit")
        mode_input = input("Enter choice (A/M/Q): ").strip().lower()

        if mode_input == 'a':
            game_controller.run(mode='A', max_runs=100)
        elif mode_input == 'm':
            game_controller.run(mode='M', max_runs=100)
        elif mode_input == 'q':
            print("Exiting Game.")
            break
        else:
            print("Invalid input. Please try again.")

        
if __name__ == "__main__":
    main()