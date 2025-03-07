
from project2 import grid as Grid
from project2 import gamecontroller as GameController




def main():
    
    grid = Grid(10.10)
    game_controller = GameController(grid)
    game_controller.run(100)



if __name__ == '__main__':
    main()
