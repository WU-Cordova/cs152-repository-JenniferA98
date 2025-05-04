

class Drink:
    """Represents a single drink w/ kind, size and price"""

    kinds = {
        "Bearcat Mocha": 2.00,
        "Sunrise Smoothie": 1.00,
        "Strawberry Matcha": 2.00,
        "Cold Brew": .50,
        "Lightning Latte": 2.50
    }

    sizes = {"small":12 , "medium":16, "large":20}

    base_prices = {"small":2.00 , "medium":3.00, "large":4.00
    }

    def __init__(self, kind, size):
        if kind not in Drink.kinds:
            raise ValueError(f"Unknown drink kind: {kind}")
        if size not in Drink.sizes:
            raise ValueError(f"Size not avialable.")
        
        self.kind = kind
        self.size = size

    def get_price(self):
        """Calculate total price based on size and kind"""
        return Drink.base_prices[self.size] + Drink.kinds[self.kind]
    
    def __str__(self):
        return f"{self.size} [{self.kind} - ${self.get_price():.2f}]"


    