
from project2 import grid as Grid




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

    def run(self, max_runs:int):
        generation = 0

        while generation < max_runs:
            print(f"Generation {generation}")
            self.grid.Grid.print_grid()

            if self.check_repitition():
                print(f"Game stopped due to repitition in generation {generation}")
                break

            self.store_current_grid()

            self.grid.Grid.next_state()

            generation += 1

            if generation == max_runs:
                print(f"Game stopped aften reaching the maximum run limit of {max_runs}")


