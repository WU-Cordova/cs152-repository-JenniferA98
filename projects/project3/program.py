from projects.project3.menu import Menu
from projects.project3.drink import Drink
from projects.project3.order_item import OrderItem
from projects.project3.customer_order import CustomerOrder
from projects.project3.bistro_system import BistroSystem

def main():
    kinds = ["Bearcat Mocha", "Sunrise Smoothie", "Strawberry Matcha", "Cold Brew", "Lightning Latte"]
    sizes = ["small", "medium", "large"]
    menu = Menu(kinds, sizes)
    bistro = BistroSystem(menu)

    while True:
        print("\n=== Bistro System ===")
        print("1. Take New Order")
        print("2. Complete Order")
        print("3. View Open Orders")
        print("4. View Completed Orders")
        print("5. View End of Day Report")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            bistro.take_new_order()
        elif choice == "2":
            bistro.complete_order()
        elif choice == "3":
            bistro.view_open_orders()
        elif choice == "4":
            bistro.view_completed_orders()
        elif choice == "5":
            bistro.view_end_of_day_report()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
