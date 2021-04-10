 Please run coffee_machine.py 
---------------------Test case output-----------------------
Read input from test_input.py which contains the dictionary containing ingredient initialization as total_items_quantity
and also contains the multiple requests of different beverages made to the coffee machine

Our code currently accepts the multiple requests and handles multithreading race conditions using locks

The output for the input given in test_input.py is:
Do you want to buy, fill, remaining, exit):
"buy"

Output: <br/>
hot_ginger_tea is prepared <br />
hot_coffee is prepared <br />
green_tea can't be prepared because green_mixture not available <br />
black_tea cannot be prepared because hot_water is not available <br />

Do you want to buy, fill, remaining, exit):<br />
"buy"<br />
hot_ginger_tea cannot be prepared because hot_milk is not available<br />
hot_coffee cannot be prepared because hot_milk is not available<br />
green_tea can't be prepared because green_mixture not available<br />
black_tea cannot be prepared because hot_water is not available<br />

Other functionalities such as fill and remaining and exit also work <br />