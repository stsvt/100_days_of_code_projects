print("Welcome to secret auction!")

def finding_max_bid(auction):
    max_bid = 0
    winner = ""
    for key in auction:
        if auction[key] > max_bid:
            max_bid = auction[key]
            winner = key

    print(f"The winner is {winner} with bit ${max_bid}. Congratulations!")

auction = {}
continue_auction = True
while continue_auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction[name] = bid
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    print("\n" * 20)
    if answer == "no":
        continue_auction = False
        finding_max_bid(auction)


finding_max_bid(auction)