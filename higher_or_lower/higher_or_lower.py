import random
from data_for_higher_or_lower import data
from logo import logo, vs

print(logo)


def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"

def higher_or_lower(score = 0):
    account_a = random.choice(data)
    account_b = random.choice(data)

    account_a_followers = account_a['follower_count']
    account_b_followers = account_b['follower_count']

    game_over = False
    while not game_over:

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        choice = input("Who has more followers? Type 'A' or 'B'? ")

        if choice == 'A':
            if account_a_followers > account_b_followers:
                score += 1
                print("\n" * 20)
                print(f"You are right! Your score is {score}")
                higher_or_lower(score)
            else:
                print("\n" * 20)
                print(f"Sorry! Thats wrong. Your final score is {score}")
                score = 0

        elif choice == 'B':
            if account_b_followers > account_a_followers:
                score += 1
                print("\n" * 20)
                print(f"You are right! Your score is {score}")
                higher_or_lower(score)
            else:
                print("\n" * 20)

                print(f"Sorry! Thats wrong. Your final score is {score}")
                score = 0

        if score == 0:
            quit()
higher_or_lower()
