import random

import hangmanstages
from hangmanstages import stages

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/""")

"""def display_hangman(lives):
    stage = hangman_stages[lives]
    for line in stage:
        print(line)"""

def print_word():
    for i in list_of_under:
        print(f"{i}", end="")

words = ["mystery", "adventure", "puzzle", "journey", "victory", "challenge", "wizard", "dragon", "knight", "castle", "phantom", "treasure", "legend", "quest", "explorer"]

chosen_word = random.choice(words)

list_of_under = []

for i in range(len(chosen_word)):
    list_of_under.append("_")

lives = 6
while lives > 0:
    print("Word: ", end="")
    print_word()
    print()
    letter = input("Type a letter: ")
    print(f"Guess a letter: {letter}")
    if letter in chosen_word:
        correct_guess = False
        for i in range(len(chosen_word)):
            if letter == chosen_word[i]:
                list_of_under[i] = letter
                correct_guess = True

        if correct_guess:
            print(stages[lives])
            print(f"****************************{lives}/6 LIVES LEFT****************************")
    else:
        correct_guess = False
        lives -= 1
        print(f"You guessed {letter}, that's not in the word. You lose a life.")
        print(stages[lives])

        print(f"****************************{lives}/6 LIVES LEFT****************************")

    if list_of_under == list(chosen_word):
        print("You win!")
        print(f"The word was '{chosen_word}'.")
        break
if lives == 0:
    print("Game over! You've run out of lives. The word was: ", chosen_word)

