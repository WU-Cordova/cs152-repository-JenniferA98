
from project2.grid import Grid
from time import sleep
from project2.kbhit import KBHit





class GameController:

    def __init__(self, grid: Grid, max_history: int = 5):
        """Initailized game and allows for the storing of a small grid history"""
        self.grid = grid
        self.max_history = max_history
        self.history = []



    def check_repetition(self):
        """Checks if grid has been repeated in the previous five iterations"""
        for previous_grid in self.history:
            if self.grid == previous_grid:
                return True
            
        return False
    
    def store_current_grid(self):
        """Maintains and stores grid history"""
        if len(self.history) >= self.max_history:
            self.history.pop(0)

        self.history.append(self.grid)

    def run(self, mode: str = 'A', max_runs:int = 100):
        """Runs game of life up to 100 generation, allowing or manual user mode using KBHit"""
        generation = 0
        kb = KBHit()

        while generation < max_runs:
            print(f"Generation {generation}")
            self.grid.print_grid()

            if self.check_repetition():
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

            
            elif mode == 'A':  
                self.grid.next_state()
                sleep(1)  
            generation += 1

        if generation == max_runs:
            print(f"Game stopped after reaching the maximum run limit of {max_runs} iterations.")


