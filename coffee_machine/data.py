coffee_data = {
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

def coins_counter():
    bank = []
    print("Please insert coins.")
    insert_coins = int(input("How many quarters?: "))
    bank.append(insert_coins * 0.25)

    insert_coins = int(input("How many dimes?: "))
    bank.append(insert_coins * 0.1)

    insert_coins = int(input("How many nickles?: "))
    bank.append(insert_coins * 0.05)

    insert_coins = int(input("How many pennies?: "))
    bank.append(insert_coins * 0.01)
    return sum(bank)

def coffee_maker(wish, ingredients_bank):

    cost_in_machine = coffee_data[wish]['cost']
    water_for_coffee = coffee_data[wish]['ingredients']['water']
    milk_for_coffee = coffee_data[wish]['ingredients']['milk']
    require_coffee = coffee_data[wish]['ingredients']['coffee']

    coins = coins_counter()

    if coins >= cost_in_machine and ingredients_bank['water'] >= water_for_coffee and ingredients_bank['milk'] >= milk_for_coffee and ingredients_bank['coffee'] >= require_coffee:
        print(f"You successful buy a {wish}! Enjoy it")
        ingredients_bank['water'] -= water_for_coffee
        ingredients_bank['milk'] -= milk_for_coffee
        ingredients_bank['coffee'] -= require_coffee
        ingredients_bank['money'] += cost_in_machine
        if coins > coffee_data['latte']['cost']:
            coins -= coffee_data['latte']['cost']
            print(f"Here is ${coins.__round__(2)} in change")
    elif water_for_coffee > ingredients_bank['water']:
        print("Sorry there is not enough water")
    elif milk_for_coffee > ingredients_bank['milk']:
        print("Sorry there is not enough milk")
    elif require_coffee > ingredients_bank['coffee']:
        print("Sorry there is not enough coffee")
    else:
        print("Not enough money")

    return ingredients_bank