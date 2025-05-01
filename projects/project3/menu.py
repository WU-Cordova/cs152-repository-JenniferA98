from datastructures.array2d import Array2D
from projects.project3.drink import Drink


class Menu:
    """Represents a menu of drinks stored in a 2D array"""

    def __init__(self, kinds: list[str], sizes: list[str]):
        self.kinds = kinds
        self.sizes = sizes
        self.rows = len(kinds)
        self.cols = len(sizes)

        self.menu = Array2D.empty(len(kinds), len(sizes), data_type= Drink)

        for r, kind in enumerate(kinds):
            for c, size in enumerate(sizes):
                self.menu[r][c] = Drink(kind,size)

    def get_drink(self, kind:str, size:str) -> Drink:
        """Retrieves a Drink object from menu by kind and size"""
        if kind not in self.kinds or size not in self.sizes:
            raise ValueError("Not on menu.")
        row = self.kinds.index(kind)
        col = self.sizes.index(size)
        return self.menu[row][col]
    
    def __str__(self):
        result = "=== Menu === \n"
        for row_idx, kind in enumerate(self.kinds):
            result += f"{kind}:\n"
            for col_idx, size in enumerate(self.sizes):
                drink: Drink = self.menu[row_idx][col_idx]
                result += f"  {size.title():<8} - ${drink.get_price():.2f}\n"
        return result