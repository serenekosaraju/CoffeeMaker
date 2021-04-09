import threading


class CoffeeMachine:
    def __init__(self, coffee_syrup, tea_leaves_syrup, ginger_syrup, cardamom_syrup, cups, water, milk, sugar_syrup):
        self.coffee_syrup = coffee_syrup
        self.tea_leaves_syrup = tea_leaves_syrup
        self.cardamom_syrup = cardamom_syrup
        self.ginger_syrup = ginger_syrup
        self.sugar_syrup = sugar_syrup
        self.cups = cups
        self.hot_water = water
        self.hot_milk = milk
        self.beverages = ip1["machine"]["beverages"]
        self.not_available = ""
        self.choice = 0
        self.reduced = [0, 0, 0, 0, 0, 0, 0, 0]
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
            self.buy()
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
        elif self.cups - self.reduced[4] < 0:
            self.not_available = "cups"
        elif self.hot_water - self.reduced[5] < 0:
            self.not_available = "hot_water"
        elif self.hot_milk - self.reduced[6] < 0:
            self.not_available = "hot_milk"
        elif self.sugar_syrup - self.reduced[7] < 0:
            self.not_available = "sugar_syrup"

        if self.not_available != "":  # if something was detected to be below zero after deduction
            return False
        else:  # if everything is enough to make the coffee
            return True

    def deduct_supplies(self):  # performs operation from the reduced list, based on the coffee chosen
        self.hot_water -= self.reduced[5]
        self.hot_milk -= self.reduced[6]
        self.coffee_syrup -= self.reduced[0]
        self.cardamom_syrup -= self.reduced[3]
        self.tea_leaves_syrup -= self.reduced[1]
        self.ginger_syrup -= self.reduced[2]
        self.sugar_syrup -= self.reduced[7]
        self.cups -= self.reduced[4]

    def buy(self):
        beverages_catered = {"hot_ginger_tea": [0, 10, 5, 0, 1, 50, 10, 10], "cardamom_tea": [0, 10, 0, 5, 1, 50, 10, 10],
                             "hot_coffee": [10, 0, 0, 0, 1, 50, 10, 10], "hot_milk": [0, 0, 0, 0, 10, 0, 50, 0],
                             "hot_water": [0, 0, 0, 0, 10, 50, 0, 0]}
        for beverage in self.beverages:
            if beverage in beverages_catered.keys():
                self.reduced = beverages_catered[beverage]
                if self.available_check():  # checks if supplies are available
                    self.deduct_supplies()  # if it is, then it deducts
                    print("{} is prepared".format(beverage))
                else:
                    print("{} cannot be prepared because {} is not available".format(beverage, self.not_available))
            else:
                ingredients_available = ["coffee_syrup", "tea_leaves_syrup", "ginger_syrup", "cardamom_syrup", "cups",
                                         "hot_water", "hot_milk", "sugar_syrup"]
                ingredients_required_for_beverage = self.beverages[beverage].keys()
                for ingredient in ingredients_required_for_beverage:
                    if ingredient not in ingredients_available:
                        print("{} can't be prepared because {} not available".format(beverage, ingredient))
        self.return_to_menu()

    def thread_task(self, lock):
        """
        task for thread
        calls buy function n times.
        """
        t = []
        for i in range(len(self.beverages)):
            lock.acquire()
            t[i] = threading.Thread(target=self.buy())
            lock.release()

    def main_task(self):

        # creating a lock
        lock = threading.Lock()

        # creating threads
        t = []
        for thread in range(len(self.beverages)):
            t[thread] = threading.Thread(target=self.thread_task, args=(lock,))
            t[thread].start()
            t[thread].join()

    def fill(self):  # for adding supplies to the machine
        self.hot_water += int(input("Write how many ml of water do you want to add:\n"))
        self.hot_milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee_syrup += int(input("how many ml of coffee syrup do you want to add:\n"))
        self.cardamom_syrup += int(input("how many ml of cardamom syrup do you want to add:\n"))
        self.ginger_syrup += int(input("how many ml of ginger syrup do you want to add:\n"))
        self.tea_leaves_syrup += int(input("how many ml of tea leaves syrup do you want to add:\n"))
        self.sugar_syrup += int(input("how many ml of sugar syrup do you want to add:\n"))
        self.cups += int(input("Write how many cups of coffee do you want to add:\n"))
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
        print("{} of cups".format(self.cups))
        self.return_to_menu()


if __name__ == "__main__":
    from initialization_of_ingredients_for_further_testing import ip
    from test_input import ip1

    num_outlets_1 = int(ip1["machine"]["outlets"]["count_n"])
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
    cf_init = CoffeeMachine(coffee_syrup, tea_leaves_syrup, ginger_syrup, cardamom_syrup, num_cups, hot_water, hot_milk,
                            sugar_syrup)
    cf_init.main_task()
