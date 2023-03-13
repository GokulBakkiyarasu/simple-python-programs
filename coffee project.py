MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit ={
    "Money": 0,
}

logo = """
//     ____   U  ___ u  _____   _____ U _____ uU _____ u    __     __ U _____ u _   _    ____      U  ___ u   ____     
//  U /"___|   \/"_ \/ |" ___| |" ___|\| ___"|/\| ___"|/    \ \   /"/u\| ___"|/| \ |"|  |  _"\      \/"_ \/U |  _"\ u  
//  \| | u     | | | |U| |_  uU| |_  u |  _|"   |  _|"       \ \ / //  |  _|" <|  \| |>/| | | |     | | | | \| |_) |/  
//   | |/__.-,_| |_| |\|  _|/ \|  _|/  | |___   | |___       /\ V /_,-.| |___ U| |\  |uU| |_| |\.-,_| |_| |  |  _ <    
//    \____|\_)-\___/  |_|     |_|     |_____|  |_____|     U  \_/-(_/ |_____| |_| \_|  |____/ u \_)-\___/   |_| \_\   
//   _// \\      \\    )(\\,-  )(\\,-  <<   >>  <<   >>       //       <<   >> ||   \\,-.|||_         \\     //   \\_  
//  (__)(__)    (__)  (__)(_/ (__)(_/ (__) (__)(__) (__)     (__)     (__) (__)(_")  (_/(__)_)       (__)   (__)  (__) 
"""


total_water = resources["water"]
total_milk = resources["milk"]
total_coffee = resources["coffee"]
required_water = 0
required_milk = 0
required_coffee = 0


def required_amount():
    global required_water
    global required_milk
    global required_coffee
    if user_input == "espresso":
        required_water = MENU["espresso"]["ingredients"]["water"]
        required_coffee = MENU["espresso"]["ingredients"]["coffee"]
        required_milk = 0
        return [required_water, required_milk, required_coffee]
    elif user_input == "latte":
        required_water = MENU["latte"]["ingredients"]["water"]
        required_milk = MENU["latte"]["ingredients"]["milk"]
        required_coffee = MENU["latte"]["ingredients"]["coffee"]
        return [required_water, required_milk, required_coffee]

    else:
        required_water = MENU["cappuccino"]["ingredients"]["water"]
        required_milk = MENU["cappuccino"]["ingredients"]["milk"]
        required_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        return [required_water, required_milk, required_coffee]


def available_amount():
    global total_water
    global total_milk
    global total_coffee
    total_water -= required_water
    total_milk -= required_milk
    total_coffee -= required_coffee



def process_coin():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    coins=coin_input()
    total_quarters = coins[0] * quarters
    total_dimes = coins[1] * dimes
    total_nickles = coins[2] * nickles
    total_pennies = coins[3] * pennies
    return total_quarters + total_dimes + total_nickles + total_pennies

def transactions():
    if user_input == "espresso":
        cost = MENU["espresso"]["cost"]
    elif user_input == "latte":
        cost = MENU["latte"]["cost"]
    elif user_input == "cappuccino":
        cost = MENU["cappuccino"]["cost"]
    total = process_coin()
    if total >= cost:
        profit["Money"] += cost
        print(f"Here is your {user_input}☕.Enjoy!")
        if total > cost:
            balance = total - cost
            print(f"Here is {balance} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")


def coin_input():
    print("Please insert coins.")
    no_of_quarters = int(input("how many quarters?: "))
    no_of_dimes = int(input("how many dimes?: "))
    no_of_nickles = int(input("how many nickles?: "))
    no_of_pennies = int(input("how many pennies?: "))
    return [no_of_quarters, no_of_dimes, no_of_nickles, no_of_pennies]



should_continue = True
while should_continue:
    print(logo)
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        required_amount()
        if total_water > required_water and total_milk > required_milk and total_coffee > required_coffee and (user_input == "latte" or "cappuccino" or "espresso"):
            transactions()
            available_amount()
        else:
            if total_water < required_water:
                print(f"Sorry, there is not enough water to make your {user_input}☕.")
            elif total_milk < required_milk:
                print(f"Sorry, there is not enough milk to make your {user_input}☕.")
            elif total_coffee < required_coffee:
                print(f"Sorry, there is not enough coffee to make your {user_input}☕.")
    elif user_input == "report":
        print(f"water: {total_water}")
        print(f"milk: {total_milk}")
        print(f"coffee: {total_coffee}")
        print(f"Money: {profit['Money']}")
    else:
        should_continue = False












