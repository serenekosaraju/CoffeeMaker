 Please run coffee_machine.py 
 1. Gets test input from user after initializing with values for all the ingredients based on input from initialization file
 Example test cases:
 Input:
 "Do you want to buy, fill, remaining, exit": "buy"
 "What do you want to buy?": "1"

 Output:
 Ginger tea is prepared
 #After a few attempts of buying items, we get a message saying it is not possible to buy some items due to some ingredients not being available

###---------------------New testing cases-----------------------
###Read input from test_input.py which contains the dictionary containing ingredient initialization as total_items_quantity
and also contains the multiple requests of different beverages made to the coffee machine

Our code currently accepts the multiple requests and handles multithreading race conditions using locks

The output for the input given in test_input.py is:
Do you want to buy, fill, remaining, exit):
"buy"

Output:
hot_tea can't be prepared because hot_water not available
hot_tea can't be prepared because hot_milk not available
hot_coffee is prepared
green_tea can't be prepared because hot_water not available
green_tea can't be prepared because green_mixture not available
black_tea can't be prepared because hot_water not available

