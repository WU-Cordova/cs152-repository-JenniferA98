
from project2 import grid as Grid
import time
from time import sleep
from project2.kbhit import KBHit





class GameController:

    def __init__(self, grid: Grid, max_history: int = 5):
        
        self.grid = grid
        self.max_history = max_history
        self.history = []



    def check_repitition(self):

        for previous_grid in self.history:
            if self.grid == previous_grid:
                return True
            
        return False
    
    def store_current_grid(self):

        if len(self.history) >= self.max_history:
            self.history.pop(0)

        self.history.append(self.grid)

    def run(self, mode: str = 'A', max_runs:int = 100):
        generation = 0
        kb = KBHit

        while generation < max_runs:
            print(f"Generation {generation}")
            self.grid.Grid.print_grid()

            if self.check_repitition():
                print(f"Game stopped due to repitition in generation {generation}")
                break

            self.store_current_grid()

            if mode == 'M':  
                print("Press 'S' to step or 'A' to switch to Automatic mode or 'Q' to quit.")
                while True:
                    if kb.kbhit():
                        key = kb.getch()
                        if key.lower() == 's':  
                            self.grid.next_state()
                            break
                        elif key.lower() == 'a':  
                            print("Switched to Automatic Mode.")
                            self.run(mode='A', max_runs=max_runs)
                            return 
                        elif key.lower() == 'q':  
                            print("Game Over.")
                            return
                        else:
                            continue

            # In Automatic Mode, advance automatically every second
            elif mode == 'A':  # Automatic mode
                self.grid.next_state()
                sleep(1)  # Pause for 1 second between generations
            generation += 1

        if generation == max_runs:
            print(f"Game stopped after reaching the maximum run limit of {max_runs} iterations.")


