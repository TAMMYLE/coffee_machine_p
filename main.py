# import resouces and menu dictionaries
from menu import resources, MENU

""" option + shift + A ---> block comment """

""" PROGRAM REQUIREMENTS
    1. Print report

    print out all remain resources including Water, Milk, Coffee, Money

    2. Check resources sufficient

    look thru all remain resources -- check it against the recipe of the drink -- tells the user if there is insufficient resources (as long as one resource is not sufficient)
    -- drink CANNOT be made -- print the feedback to the user

    3. Coin payment

    * small gold coin ($2)
    * large gold coin ($1)
    * 50 cents
    * 20 cents
    * 10 cents
    * 5 cents

    user choose DRINK --> ask user to INSERT the quantity of each COINS (how many $2 coin? how many $1? etc.)
    --> if user doesn't insert enough coins --> print out feedback and refund the coins
    --> if user inserts enough coins --> calculate how much money all of these coins are worth --> calculate the CHANGE based on the cost of the drink 
    --> hand user the DRINK 

    4. Check transaction successful

    program must:
        DEDUCT the RESOURCES if user sucessfully paid for their drink
        ADD money to the tilt
    
    5. Make the coffee

 """


# function print_drink() : Print out user choice of drink if it exists in the MENU

def print_drink(input):

    drink_checker = [key for key, value in MENU.items() if key == input] #--> array

    match_drink = ""

    if drink_checker: 

        # convert result to string
        match_drink = drink_checker[0]
        print(f"You have chose {match_drink}. \n")

        return match_drink

def resource_checker(selected_drink):
    # Check if the selected drink is in the MENU
    if selected_drink not in MENU:
        
        print("Selected drink is not available.")
        return False
    
    # Get the ingredients required for the selected drink
    required_ingredients = MENU[selected_drink]["ingredients"]
    
    # Check each ingredient in the required ingredients
    for item, required_amount in required_ingredients.items():
        if resources[item] < required_amount:
            print(f"\n oh No, We're running out of {item} for your {selected_drink}.")
            return False
   
    # Ask user to insert coins 
    total_payment_received = initial_payment()
    
    # Calculate the change
    transaction_checker(selected_drink, total_payment_received)

    # Add user payment to tilt
    # Hand the drink to user


def initial_payment():
   """ 
    * small gold coin ($2)
    * large gold coin ($1)
    * 50 cents
    * 20 cents
    * 10 cents
    """ 
   print("\n Please insert coins \n")
   two_dollar = int(input("How many $2 coins?: \n"))
   one_dollar = int(input("How many $1 coins?: \n"))
   fifty_cent = int(input("How many 50 cents?: \n"))
   twenty_cent = int(input("How many 20 cents?: \n"))
   ten_cent = int(input("How many 10 cents?: \n"))

   total_receive = (two_dollar * 2) + (one_dollar * 1) + (fifty_cent * 0.5) + (twenty_cent * 0.2) + (ten_cent * 0.1)

   return total_receive

# Return True if payment is sufficient and False when payment is not
def transaction_checker(selected_drink, amount):

    drink_cost = MENU[selected_drink]["cost"]
    drink_ingredients = MENU[selected_drink]["ingredients"]

    if amount < drink_cost:
        print("Sorry that's not enough money. Money refunded.\n")
        return False
    
    elif amount == drink_cost:
        resources["money"] = amount
        make_coffee(selected_drink, drink_ingredients)
        return True
    
    elif amount > drink_cost:
        
        change = amount - drink_cost
        print(f"Here is {change:.2f} dollars in change.\n")

        resources["money"] = drink_cost

        make_coffee(selected_drink, drink_ingredients)

        return True

# make_coffee()
def make_coffee(selected_drink, ingredient_usage):
    """ deduct ingredients from resources """
    for item in ingredient_usage:

        resources[item] -= ingredient_usage[item]

    print(f"Here is your {selected_drink}. Enjoy!!!\n")

# print_report() ---> receive input from user, and print out the report if user's input is report
def print_report():
    # when user enters "report" to the prompt --> remain resources must be printed
    # must retrieve from resources dictionary
    for item in resources:
        if item == "water" or item == "milk":
            print(f"{item}: {resources[item]}ml")
        elif item == "coffee":
            print(f"{item}: {resources[item]}g")
        elif item == "money":
            print(f"{item}: ${resources[item]}")

# Main Run
# machine_control -- switch off the coffee machine when barista wants to

machine_state = True

# Barista can use secret word ("off") to turn off the machine, end execution
while machine_state:

    print("\n\n ☕️ THANKS FOR USING TAMMY'S COFFEE MACHINE  ☕️ \n\n")

    barista_quest = input("What would you like to order? espresso/ latte/ cappuccino: \n").lower()

    if barista_quest == "off":

        machine_state = False

    elif barista_quest == "report":
        print_report()

    else:

        customer_drink = print_drink(barista_quest)

        resource_checker(customer_drink)

        machine_state = True
