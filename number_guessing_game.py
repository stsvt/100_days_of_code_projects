import random

EASY_LEVEL = 10
HARD_LEVEL = 5
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
choice_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
is_guess = False

if choice_mode == "easy":
    attempts = EASY_LEVEL
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    attempts = HARD_LEVEL
    print(f"You have {attempts} attempts remaining to guess the number.")

while not is_guess and attempts > 0:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The number was {number}.")
        is_guess = True
    elif guess > number:
        attempts -= 1
        print("Too high!")
        print(f"Attempts remaining: {attempts}")
        is_guess = False
    elif guess < number:
        attempts -= 1
        print("Too low!")
        print(f"Attempts remaining: {attempts}")
        is_guess = False

    if attempts == 0:
        print("You lose! You have run out of guesses!.")
