from utils.deck import Deck, GameDeck, Card

# Function to calculate the total value of a hand, accounting for Aces.
def calculate_hand_value(hand):
    total_aces = 0
    for card in hand:
        if card.rank == 'Ace':
            total_aces += 1
    value = sum(card.value for card in hand)
    if value > 21 and total_aces > 0:
        value -= 10 * total_aces
    return value

def main():
    keep_playing = True
    deck = Deck() # Create a new deck
    player_hand = []
    game_deck = GameDeck(deck.get_cards()) # Create a game deck from the original deck
    game_deck.shuffle() # Shuffle the game deck

    player_name = input("Enter player's name: ")
    print(f"Welcome, {player_name}! Let's deal your hand.\n")

    # Deal 2 cards to the player
    for _ in range(2):
        player_hand.append(game_deck.deal_card())

    print(f"{player_name}'s Hand:")
    for card in player_hand:
        print(card)

    print("Total points:", calculate_hand_value(player_hand))

    if calculate_hand_value(player_hand) == 21:
        print("Blackjack! You win!")
        keep_playing = False
        return
    
    while keep_playing:
        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            new_card = game_deck.deal_card()
            if new_card:
                player_hand.append(new_card)
                print(f"\nDealt card: {new_card}")
                print(f"{player_name}'s Hand:")
                for card in player_hand:
                    print(card)
                total_points = calculate_hand_value(player_hand)
                print("Total points:", total_points)
                if total_points == 21:
                    print("Congratulations! You hit 21!")
                    break
                elif total_points > 21:
                    print("Bust! You exceeded 21 points.")
                    break
            else:
                print("No more cards to deal.")
                break
        elif choice == 's':
            print(f"\n{player_name} stands with {sum(card.value for card in player_hand)} points.")
            break
        else:
            print("Invalid choice. Please enter 'h' to hit or 's' to stand.")

if __name__ == "__main__":
    main()