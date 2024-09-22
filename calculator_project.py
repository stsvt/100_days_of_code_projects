logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \\ `.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\  `.___.'\\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

while True:
    answer = ""
    if answer == "y":
        continue
    else: first_number = float(input("Type a first number: "))

    operation = input("+\n-\n/\n*\nPick an operation: ")
    second_number = float(input("Type a next number: "))

    def calc(first_number, operation, second_number):
        result = 0
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            if second_number != 0:
                result = first_number / second_number
            else: print("Second number can't be equal 0")
        print(f"{first_number} {operation} {second_number} = {result}")
        return result

    result = calc(first_number, operation, second_number)

    answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if answer == "y":
        operation = input("+\n-\n/\n*\nPick an operation: ")
        second_number = float(input("Type a next number: "))
        result = calc(result, operation, second_number)
        answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    elif answer == "n":
        result = 0
        answer = ""

