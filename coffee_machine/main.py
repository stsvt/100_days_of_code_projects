from data import coffee_data
from data import coffee_maker
# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
is_machine_on = True

water = 300
milk = 200
coffee = 100
money = 0

ingredients_bank = {'water': water, 'milk': milk, 'coffee': coffee, 'money': money}

def report():
    return f'''
Water: {ingredients_bank['water']}ml
Milk: {ingredients_bank['milk']}ml
Coffee: {ingredients_bank['coffee']}g
Money: ${ingredients_bank['money']}
            '''

while is_machine_on:
    wish = input("What would you like? (espresso/latte/cappuccino): ")

    if wish == 'report':
        print(report())
    elif wish == 'off':
        print("Machine is successfully off")
        is_machine_on = False
    else:
        coffee_maker(wish, ingredients_bank)
