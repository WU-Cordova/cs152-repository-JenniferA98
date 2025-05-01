#Use Circular Que - first in first out- text based
from datastructures.deque import Deque
from datastructures.hashmap import HashMap

from project3.menu import Menu
from project3.drink import Drink
from project3.order_item import OrderItem
from project3.customer_order import CustomerOrder


class BistroSystem:
    def __init__(self, menu: Menu):
        self.menu = menu
        self.open_orders = Deque(data_type = CustomerOrder)
        self.completed_orders = Deque(data_type=CustomerOrder)
        self.customer_orders = HashMap(data_type = CustomerOrder)
        self.drink_sales_count = HashMap(data_type=int)
        self.drink_sales_total = HashMap(data_type=float)


    def display_menu(self):
        """Displays entire menu"""
        print(self.menu)

    def take_new_order(self):
        name = input("Enter customer name: ")
        order = CustomerOrder(name)

        while True:
            print("Available dirnks:")
            self.display_menu()
            drink_kind = input("Enter drink kind (or 'done' to finish): ").strip()
            if drink_kind.lower() == "done":
                break
            drink_size = input("Enter drink size (small, medium, large): ").strip()

            try:
                drink = self.menu.get_drink(drink_kind, drink_size)
                order.add_item(OrderItem(drink))

                if drink_kind not in self.drink_sales_count:
                    self.drink_sales_count[drink_kind] = 0
                    self.drink_sales_total[drink_kind] = 0.0
                self.drink_sales_count[drink_kind] += 1
                self.drink_sales_total[drink_kind] += drink.get_price()
            except ValueError as e:
                print(e)

            self.open_orders.enqueue(order)
            self.customer_orders[name] = order
            print(f"Order added for {name}.")

    def complete_order(self):
        """Complete the first order in the open orders queue and move it to completed."""
        if self.open_orders.empty():
            print("No open orders.")
            return

        order = self.open_orders.dequeue()
        self.completed_orders.enqueue(order)
        print(f"Order for {order} has been completed.")
    
    def view_open_orders(self):
        """Display all open orders."""
        if self.open_orders.empty():
            print("No open orders.")
            return
        
        print("=== Open Orders ===")
        for order in self.open_orders:
            print(order)

    def view_completed_orders(self):
        """Display all completed orders."""
        if self.completed_orders.empty():
            print("No completed orders.")
            return
        
        print("=== Completed Orders ===")
        for order in self.completed_orders:
            print(order)

    def view_end_of_day_report(self):
        """Generate a sales report for the day."""
        print("=== End of Day Report ===")
        total_revenue = 0.0
        for drink_kind in self.drink_sales_count:
            count = self.drink_sales_count[drink_kind]
            total = self.drink_sales_total[drink_kind]
            print(f"{drink_kind}: {count} sold, Revenue: ${total:.2f}")
            total_revenue += total
        print(f"Total Revenue for the Day: ${total_revenue:.2f}")



