Bistro System - Project 3

Class Justifications

Menu -
Structure : 2D Array
Menu is a collection of drinks with multiple characteristics, Array2D's allow for the natural mapping of these charactersitcs with easy lookup time and efficiency. Both retrieving drinks has O(1) complexity and because the menu is a fixed size its rather efficient, however this would mean the structure would need to be recreated each time the menu was changed. 

Customer Order -
Structure : Array Stack 
Each customer allows for multiple drink selection, and Array Stack runs with LIFO to allow for the drinks, which have mutliple features to be repeated back to the customer. This structure would also be helpful for order review and modification. Retrieving and adding drinks to the Array stack has O(1) complexity while price computation is O(n). Array stacks have a fixed max size which for larger operations would prove an issue but in terms of the Bearcat Bistro I don't think it should be a problem.

Open Orders -
Structure : Deque
Orders need to be processed in a FIFO order, the time complexity also remains at O(1) so it is an effecient process/structure. Considered using a circular queue to place order limitations but ended up going with a deque because its more flexible, meaning orders can be added to the front and back, which allows for employees to move orders ahead of the que if needed.

Completed Orders -
Strucutre : Deque
FIFO structure allows for the daily summaries to be retrieved starting from the start of the day. Maintains O(1) complexity.

Customer_Order Histroy and Sales Summaries - 
Structure : Hashmaps
Allows for customer names to be associated with customer order objects for effecient retrieval, and allows for sales summaries to be stored and retrieved effectively. Further they simplifty the code for order tracking and reporting, allowing for clean and easy use. Complexity time should reamin at O(1). Hashmaps do use more memory than arrays would and they also require keys to be unique, thus drink names would need to not be repeated. Important to note that collisions will degrade performance but this is mitigated somewhat beacause of the small menu size. Forsee issues with customers with the same name in terms of order storage.


HOW TO USE:
Follow the on-screen prompts for directory selection and then each item has its own prompts and functions:
 1. Take New Order
 You'll be prompted to enter your name, then the menu will be displayed. Type in your drink kind selection and your customization and then your size selection. You can continue to add drinks to your order or type in done. Your order should then be summarized for you including the total price.
 2. Complete Order
 This function removes orders from the open orders deque and moves it to the completed orders deque.
 3. View Open Orders
 Will display all open orders.
 4. View Completed Orders
 Will display all completed orders.
 5. View End of Day Report
 Prints out end of day summary listing the count of each kind and the total revenue for each kind. Summarizing it in a daily total.
 6. Quit
 Clickind this causes a break in the main program so program ends.


BUGS AND LIMITATIONS:
Stacks sizes are predifined so as the operation scale increases this will be an issue. Input validation is minimal at this point, specifically in terms of customizaton, customizations do not have an price associations which is not the common practice.

Bugs- Doesn't allow/prompt for customization. Error messages in drink selection are not populated but if drink is invalid it will not add to order. 

FUTURE WORK:
I think having adding expecited time of order completion would be a nice feature to have overall, both in terms of employees pacing themselves adn managers understanding how the business is functioning. 
