
import random
from project2 import cell as Cell
from datastructures.array2d import Array2D




class Grid():
    
    def __init__(self, height:int, width:int):
        self.height = height
        self.width = width

        starting_sequence = [
            [random.choice([True, False]) for _ in range(width)] for _ in range(height)
        ]

        self.cells = Array2D(starting_sequence)
        

    def __getitem__(self, row:int):
        return self.cells[row]
    
    def get_neighbors(self, row:int, col:int):
        neighbors = []

        for i in range(row - 1, row + 2):
            for j in range(col -1, col +2):
                if (i != row or j != col) and 0 <= i < self.height and 0 <= j < self.width:
                    neighbors.append(self.cells[i][j]) 

        return neighbors
    
    def next_state(self):

        new_cells = Array2D.empty(self.height, self.width)

        for row in range(self.height):
            for col in range(self.width):
                neighbors = self.get_neighbors(row, col)
                self.cells[row][col].neighbors = neighbors

                new_is_alive = self.cells[row][col].next_state()

                new_cells[row][col] = Cell(row, col, new_is_alive)

        self.cells = new_cells

    def print_grid(self):
        """Prints the grid state."""
        for row in self.cells:
            print(" ".join(["X" if cell.is_alive else "." for cell in row]))


    def __eq__(self, other):
        """Check if two grids are equal."""
        return all(self.cells[row][col].is_alive == other.cells[row][col].is_alive
                   for row in range(self.height) for col in range(self.width))