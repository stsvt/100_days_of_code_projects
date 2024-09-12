import random

game = ['Rock', 'Paper', 'Scissors']

game[0] = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

game[1] = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

game[2] = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    my_options = int(input("\nPlease type 1 - Rock, 2 - Paper, 3 - Scissors\n"))
    if my_options == 1:
        print(f"You chose: {game[my_options - 1]}")
    elif my_options == 2:
        print(f"You chose: {game[my_options - 1]}")
    elif my_options == 3:
        print(f"You chose: {game[my_options - 1]}")
    else:
        print("Invalid option")

    computer_option = random.randint(1, 3)
    if computer_option == 1:
        print(f"Computer chose: {game[computer_option - 1]}")
    elif computer_option == 2:
        print(f"Computer chose: {game[computer_option - 1]}")
    elif computer_option == 3:
        print(f"Computer chose: {game[computer_option - 1]}")

    if game[computer_option - 1] == game[0] and game[my_options - 1] == game[2]:
        print("You lose!")
    elif game[computer_option - 1] == game[2] and game[my_options - 1] == game[0]:
        print("You won!")

    elif game[computer_option - 1] == game[1] and game[my_options - 1] == game[2]:
        print("You won!")
    elif game[computer_option - 1] == game[2] and game[my_options - 1] == game[1]:
        print("You lose!")

    elif game[computer_option - 1] == game[0] and game[my_options - 1] == game[1]:
        print("You won!")
    elif game[computer_option - 1] == game[1] and game[my_options - 1] == game[0]:
        print("You lose!")
    else:
        print("Draw!")
