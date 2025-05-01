Bistro System - Project 3

Class Justifications

Menu -
Structure : 2D Array
Menu is a collection of drinks with multiple characteristics, Array2D's allow for the natural mapping of these charactersitcs with easy lookup time and efficiency. Both retrieving drinks has O(1) complexity and because the menu is fized sizes its rather efficient.

Customer Order -
Structure : Array Stack 
Each customer allows for multiple drink selection, and Array Stack runs with LIFO to allow for the drinks, which have mutliple features to be repeated back to the customer. Retrieving and adding drinks to the Array stack has O(1) complexity while price computation is O(n).

Open Orders -
Structure : Deque
Orders need to be processed in a FIFO order, the time complexity also remains at O(1) so it is an effecient process/structure.

Completed Orders -
Strucutre : Deque
FIFO structure allows for the daily summaries to be retrieved starting from the start of the day. Maintains O(1) complexity.

Customer_Order Histroy and Sales Summaries - 
Structure : Hashmaps
Allows for customer names to be associated with customer order objects for effecient retrieval, and allows for sales summaries to be stored and retrieved effectively. Further they simplifty the code for order tracking and reporting, allowing for clean and easy use. Complexity time should reamin at O(1).


HOW TO USE:



BUGS AND LIMITATIONS:

FUTURE WORK:
