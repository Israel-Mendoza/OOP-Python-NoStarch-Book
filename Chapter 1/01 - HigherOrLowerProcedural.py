from __future__ import annotations
import random

# Defining annotations
card_type = dict[str, str | int]
deck_type = list[card_type]

# Defining card constants and variables
SUIT_TUPLE: tuple[str, ...] = ("Spades", "Hearts", "Clubs", "Diamonds")
RANK_TUPLE: tuple[str, ...] = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
NCARDS: int= 8
score: int = 50
starting_deck: list[card_type] = []

for suit in SUIT_TUPLE:
    for value, rank in enumerate(RANK_TUPLE):
        card: card_type = {"rank": rank, "suit": suit, "value": value + 1}
        starting_deck.append(card)

# Defining functions

def get_card (deck_list_in: list[card_type]) -> card_type:
    """
    Pass in a deck (list[dict[str, str]]) and returns a random card (dict[str, str])
    """
    card: card_type = deck_list_in.pop()
    return card

def shuffle_deck(deck: list[card_type]) -> list[card_type]:
    """
    Pass in a deck (list[dict[str, str]]) and returns a shuffled copy of it.
    """
    shuffled_deck: list[card_type] = deck.copy()
    random.shuffle(shuffled_deck)
    return shuffled_deck

# Main code
print("\n\nWelcome to 'Higher Or Lower'.")
print("You have to choose whether the next card to be shown will be higher or lower than th current card.")
print("Getting it right adds 20 points; get it wrong and you lose 15 points.")
print("You have 50 points to start.\n\n")

# Main game loop
while True:
    game_deck: list[card_type] = shuffle_deck(starting_deck)
    current_card: card_type = get_card(game_deck)
    current_card_rank: str = current_card["rank"]
    current_card_suit: str = current_card["suit"]
    current_card_value: int = current_card["value"]
    current_card_name: str = f"{current_card_rank} of {current_card_suit}"
    print(f"Starting card is: '{current_card_name}'\n\n")

    for card_number in range(0, NCARDS):
        message: str = f"{card_number} Will the next card be higher or lower than the {current_card_name}? (enter h or l):"
        answer: str = input(message).casefold()
        next_card: card_type = get_card(game_deck)
        next_card_rank: str = next_card["rank"]
        next_card_suit: str = next_card["suit"]
        next_card_value: int = next_card["value"]
        next_card_name: str = f"{next_card_rank} of {next_card_suit}"
        print(f"The next card is: '{next_card_name}'")

        # Start comparisons
        if answer == "h":
            if next_card_value > current_card_value:
                print("You got it right! The card was higher! :)")
                score += 20
            else:
                print("Sorry, the card was not higher... :( ")
                score -= 15
        elif answer == "l":
            if next_card_value < current_card_value:
                print("You got it right! The card was lower! :)")
                score += 20
            else:
                print("Sorry, the card was not lower... :(")
                score -= 15
        if score <= 0:
            print("Sorry, you lost! GAME OVER...")
            break
        else:
            print(f"You're current score is: {score}\n\n")
        
        current_card_rank = next_card_rank
        current_card_suit = next_card_suit
        current_card_value = next_card_value
        current_card_name = next_card_name
    
    message_to_continue: str = "To play again, press ENTER, or 'q' to quit: "
    go_again: str = input(message_to_continue).casefold()
    if go_again == "q":
        break

print("OK bye!")



