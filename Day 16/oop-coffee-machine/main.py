from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()

money = MoneyMachine()

on = True
while on:
    response = input(f"What would you like?({menu.get_items()}): ").lower()
    if response == "report":
        machine.report()
        money.report()
    elif response == "latte" or response == "espresso" or response == "cappuccino":
        drink = menu.find_drink(response)
        if machine.is_resource_sufficient(drink) and response == drink.name:
            money.make_payment(drink.cost)
            machine.make_coffee(drink)
    elif response == "off":
        on = False

