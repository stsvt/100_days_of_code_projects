import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(player_scores, computer_scores):
    if player_scores == computer_scores:
        return "Draw!"
    elif player_scores == 0:
        return "Win with a Blackjack!"
    elif computer_scores == 0:
        return "Lose, oponent has Blackjack!"
    elif player_scores > 21:
        return "You went over. You lose!"
    elif computer_scores > 21:
        return "Opponent went over. You win!"
    elif player_scores > computer_scores:
        return "You win!"
    else:
        return "You lose!"

def blackjack():

    player_cards = []
    computer_cards = []
    player_score = -1
    computer_score = -1
    for i in range(0, 2):
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    is_game_over = False

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
            continue

        print(f"\t Your cards: {player_cards}, current score: {player_score}")
        print(f"\t Computer first card: {computer_cards[0]}")

        choice = input("Type 'y' to get another card, 'n' to play pass: ")
        if choice == 'y':
            player_cards.append(random.choice(cards))
        else:
            is_game_over = True

    while computer_score != 0 and computer_score > 17:
        computer_cards.append(random.choice(cards))
        computer_score = calculate_score(computer_cards)

    print(f"\tYour final hand: {player_cards}, final score: {player_score}")
    print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("If you want to play 'Blackjack' type 'y', and type 'n' if won't: ") == 'y':
    print("\n" * 20)
    print(logo)
    blackjack()



#My old code
"""choice = input("Type 'y' to get another card, 'n' to play pass: ")
    if choice == 'y':
        player_cards.append(random.choice(cards))
        player_score = calculate_score(player_cards)

        if player_score > 21:
            print(f"\tYour final hand: {player_cards}, final score: {player_score}")
            print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
            print("You went over. You lose!")
        elif player_score == 21:
            print(f"\tYour final hand: {player_cards}, final score: {player_score}")
            print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
            print("You win! You have 21")
        elif player_score < 21:
            print(f"\t Your cards: {player_cards}, current score: {player_score}")
            print(f"\t Computer first card: {computer_cards[0]}")
    elif choice == 'n':
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\tYour final hand: {player_cards}, final score: {player_score}")
        print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
        if computer_score > 21:
            print("Opponent went over. You win!")
        elif computer_score == player_score:
            print("Draw!")
        elif computer_score < player_score:
            print("You win!")
        elif computer_score > player_score:
            print("You lose!") """



