



class Cell():

    def __init__(self, row, col, is_alive):
        self.row = row
        self.col = col
        self.is_alive = is_alive
        self.neighbors = []
        
    def count_neighbors(self, neighbors):
        "Returns the amount of alive neighbors"
        return sum(1 for neighbor in self.neighbors if neighbor.is_alive)
    
    def next_state(self):
        "Determines wether the cell will be alive in the next generation"

        live_neighbors = self.count_neighbors()

        if self.is_alive:
            if live_neighbors < 2 or live_neighbors > 3:
                return False
            else:
                return True
        else:
            if live_neighbors == 3:
                return True
            else:
                return False

    