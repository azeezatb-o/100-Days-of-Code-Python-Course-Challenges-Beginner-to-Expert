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

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


"""def check_resources(ingredients):
    for item in ingredients:
        is_enough = True
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
            return is_enough"""


def add_resources(res):
    add = 0
    for item in res:
        if res["water"] < 300:
            add = 300 - res["water"]
            res["water"] += add
        elif res["milk"] < 200:
            add = 200 - res["milk"]
            res["milk"] += add
        elif res["coffee"] < 100:
            add = 100 - res["coffee"]
            res["coffee"] += add


def calculate_resources(resp, res):
    if resp == "cappuccino":
        res["water"] -= 250
        res["milk"] -= 100
        res["coffee"] -= 24
    elif resp == "latte":
        res["water"] -= 200
        res["milk"] -= 150
        res["coffee"] -= 24
    elif resp == "espresso":
        res["water"] -= 50
        res["coffee"] -= 18


def calculate_money(total):
    cumulative = 0
    cumulative = total
    return cumulative


def process_coins(q, d, n, p):
    total = 0.0
    q *= QUARTER
    d *= DIME
    n *= NICKEL
    p *= PENNY
    total = q + d + n + p
    return total


def check_transaction(resp, total):
    change = 0.0
    for item in MENU:
        if resp == item and total > MENU[item]["cost"]:
            change = round(total - MENU[item]["cost"], 2)
            return f"Here is ${change} in change."
        elif (resp == item) and total < MENU[item]["cost"]:
            return "Sorry that's not enough money. Your money has been refunded"


def make_coffee(res):
    is_on = True
    cumulative = 0.0
    while is_on:
        response = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if response == "report":
            print(f"Water:  {resources['water']}ml\nMilk:  {resources['milk']}ml\nCoffee:  {resources['coffee']}g\nMoney: ${cumulative}")
            add_resources(resources)
            continue
        elif response == "espresso" or response == "latte" or response == "cappuccino":
            coffee = MENU[response]
            # for item in coffee["ingredients"]:
            """ checking if resources are sufficient for making coffee. 
            Since water is usually the highest qty of ingredient used to make coffee, we check if it is sufficient"""
            if resources["water"] < coffee["ingredients"]["water"]:
                print("Sorry there is not enough water to process your request. Try later")
                continue
            # print(resources["water"], coffee["ingredients"])
            print("Please insert coins.")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickel = int(input("How many nickel?: "))
            penny = int(input("How many penny?: "))
            total = process_coins(quarter, dime, nickel, penny)

            change = check_transaction(response, total)
            print(f"{change}\nHere is your {response} ☕ Enjoy!")
            calculate_resources(response, res)

            print(coffee["cost"])
            cumulative += coffee["cost"]
        elif response == "off":
            print("Powering off.....")
            is_on = False
        else:
            print("Invalid response. Please enter a valid response.")
            continue


make_coffee(resources)

