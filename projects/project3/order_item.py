from projects.project3.menu import Menu
from projects.project3.drink import Drink



class OrderItem:
    def __init__(self, drink: Drink, customization: str = ""):
        self.drink = drink
        self.customization = customization

    def __str__(self):
        return f"{self.drink} | Custom: {self.customization or 'None'}"

    def get_price(self):
        return self.drink.get_price()
