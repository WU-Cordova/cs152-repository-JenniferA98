from datastructures.array import Array
from datastructures.istack import IStack
from datastructures.arraystack import ArrayStack

from projects.project3.order_item import OrderItem
from projects.project3.drink import Drink

class CustomerOrder:
    def __init__(self, customer_name: str, max_size: int = 10, ):
        """Constructor initializes customer order with a stack to hold order items"""
        self.customer_name = customer_name
        self.items = ArrayStack(max_size=max_size, data_type= object)

    def add_item(self, item: OrderItem):
        """Adds an order item (drink) to the stack"""
        try:
            self.items.push(item)
        except IndexError as e:
            print(f"Error: {e}") 

    def pop_item(self):
        """Removes the last added item from the stack (if any)"""
        try:
            return self.items.pop()
        except IndexError as e:
            print(f"Error: {e}")  

    def total_price(self):
        """Calculates the total price of the items in the order stack"""
        return sum(Drink.get_price() for i in self.items)

    def __str__(self):
        """Returns a string representation of the order, including customer name, items, and total price"""
        items_str = "\n  ".join(str(item) for item in self.items)
        return f"Customer: {self.customer_name}\n  {items_str}\nTotal: ${self.total_price():.2f}"

