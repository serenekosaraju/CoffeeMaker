import threading


class CoffeeMachine:
    def __init__(self, coffee_syrup, tea_leaves_syrup, ginger_syrup, cardamom_syrup, cups, water, milk, sugar_syrup,
                 beverages):
        self.coffee_syrup = coffee_syrup
        self.tea_leaves_syrup = tea_leaves_syrup
        self.cardamom_syrup = cardamom_syrup
        self.ginger_syrup = ginger_syrup
        self.sugar_syrup = sugar_syrup
        self.hot_water = water
        self.hot_milk = milk
        self.beverages = beverages
        self.not_available = ""
        self.choice = 0
        self.reduced = [0, 0, 0, 0, 0, 0, 0]
        self.money = 0
        self.count_n = 1
        self.running = False
        self.action = ""
        if self.running is False:
            self.start()

    def start(self):
        self.running = True
        self.action = input("Do you want to buy, fill, remaining, exit):\n")
        # possible choices to perform in the coffee machine
        if self.action == "buy":
            self.main_task()
        elif self.action == "fill":
            self.fill()
        elif self.action == "exit":
            exit()
        elif self.action == "remaining":
            self.status()

    def return_to_menu(self):  # returns to the menu after an action
        print()
        self.start()

    def available_check(self):  # checks if it can afford making that type of coffee at the moment
        # by checking whether the supplies goes below 0 after it is deducted
        if self.coffee_syrup - self.reduced[0] < 0:
            self.not_available = "coffee_syrup"
        elif self.tea_leaves_syrup - self.reduced[1] < 0:
            self.not_available = "tea_leaves_syrup"
        elif self.ginger_syrup - self.reduced[2] < 0:
            self.not_available = "ginger_syrup"
        elif self.cardamom_syrup - self.reduced[3] < 0:
            self.not_available = "cardamom_syrup"
        elif self.hot_water - self.reduced[4] < 0:
            self.not_available = "hot_water"
        elif self.hot_milk - self.reduced[5] < 0:
            self.not_available = "hot_milk"
        elif self.sugar_syrup - self.reduced[6] < 0:
            self.not_available = "sugar_syrup"
        if self.not_available != "":  # if something was detected to be below zero after deduction
            return False
        else:  # if everything is enough to make the coffee
            return True

    def deduct_supplies(self):  # performs operation from the reduced list, based on the coffee chosen
        self.hot_water -= self.reduced[4]
        self.hot_milk -= self.reduced[5]
        self.coffee_syrup -= self.reduced[0]
        self.cardamom_syrup -= self.reduced[3]
        self.tea_leaves_syrup -= self.reduced[1]
        self.ginger_syrup -= self.reduced[2]
        self.sugar_syrup -= self.reduced[6]

    def buy(self):

        for beverage in self.beverages:
            ingredients = self.beverages[beverage].keys()
            ingredients_available = ["coffee_syrup", "tea_leaves_syrup", "ginger_syrup", "cardamom_syrup",
                                     "hot_water", "hot_milk", "sugar_syrup"]
            if set(ingredients).issubset(ingredients_available):
                for index, ingredient in enumerate(ingredients_available):
                    if ingredient in ingredients:
                        self.reduced[index] = self.beverages[beverage][ingredient]
                    else:
                        self.reduced[index] = 0
                if self.available_check():  # checks if supplies are available
                    self.deduct_supplies()  # if it is, then it deducts
                    print("{} is prepared".format(beverage))
                else:
                    print("{} cannot be prepared because {} is not available".format(beverage, self.not_available))

            # Ingredients not in available set of ingredients
            else:
                for ingredient in self.beverages[beverage].keys():
                    if ingredient not in ingredients_available:
                        print("{} can't be prepared because {} not available".format(beverage, ingredient))

        self.start()

    def thread_task(self, lock):
        """
        task for thread
        calls buy function n times.
        """
        lock.acquire()
        thread = threading.Thread(target=self.buy())
        lock.release()

    def main_task(self):

        # creating a lock
        lock = threading.Lock()

        # creating threads
        for thread in range(len(self.beverages)):
            t = threading.Thread(target=self.thread_task, args=(lock,))
            t.start()
            t.join()

    def fill(self):  # for adding supplies to the machine
        self.hot_water += int(input("Write how many ml of water do you want to add:\n"))
        self.hot_milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee_syrup += int(input("how many ml of coffee syrup do you want to add:\n"))
        self.cardamom_syrup += int(input("how many ml of cardamom syrup do you want to add:\n"))
        self.ginger_syrup += int(input("how many ml of ginger syrup do you want to add:\n"))
        self.tea_leaves_syrup += int(input("how many ml of tea leaves syrup do you want to add:\n"))
        self.sugar_syrup += int(input("how many ml of sugar syrup do you want to add:\n"))
        self.return_to_menu()

    def status(self):  # to display the quantities of supplies in the machine at the moment
        print("The coffee machine has:")
        print("{} of water".format(self.hot_water))
        print("{} of milk".format(self.hot_milk))
        print("{} of coffee syrup".format(self.coffee_syrup))
        print("{} of cardamom_syrup".format(self.cardamom_syrup))
        print("{} of ginger_syrup".format(self.ginger_syrup))
        print("{} of sugar_syrup".format(self.sugar_syrup))
        print("{} of tea_leaves_syrup".format(self.tea_leaves_syrup))
        self.return_to_menu()


if __name__ == "__main__":
    from test_input import ip

    num_outlets = int(ip["machine"]["outlets"]["count_n"])
    total_items_quantity = ip["machine"]["total_items_quantity"]
    ginger_syrup = total_items_quantity['ginger_syrup']
    coffee_syrup = total_items_quantity['coffee_syrup']
    tea_leaves_syrup = total_items_quantity['tea_leaves_syrup']
    cardamom_syrup = total_items_quantity['cardamom_syrup']
    num_cups = total_items_quantity['num_cups']
    hot_water = total_items_quantity['hot_water']
    hot_milk = total_items_quantity['hot_milk']
    sugar_syrup = total_items_quantity['sugar_syrup']
    beverages = ip["machine"]["beverages"]
    cf_init = CoffeeMachine(coffee_syrup, tea_leaves_syrup, ginger_syrup, cardamom_syrup, num_cups, hot_water, hot_milk,
                            sugar_syrup, beverages)
    cf_init.main_task()
