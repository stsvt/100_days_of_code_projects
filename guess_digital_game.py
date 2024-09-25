import random

random_number = random.randint(100, 10000)
print(random_number)

print("\n" * 20)
print("Welcome to GUESS NUMBER GAME!")
computer_number = list(str(random_number))
user_number = []
digits = len(str(random_number))
print(f"Number is {digits}-digit")

is_guessed = False
count = 0
while not is_guessed:
    number = input(f"Type a {digits}-number: ")
    for i in number:
        user_number.append(i)

    for digit in range(len(computer_number)):
        if user_number[digit] == computer_number[digit]:
            count += 1
    print(f"You have {count} matches")
    if count == digits:
        is_guessed = True
        print(f"Congrats! You guessed the number, that was {random_number}")
    elif count == 0:
        print("Try again")
        is_guessed = False
    count = 0
    user_number.clear()



