from utils.deck import Deck, GameDeck

#Main function to demonstrate deck creation, shuffling, and dealing cards.
def main():
    # Create a new deck
    deck = Deck()
    print(deck)  # Print the full deck

    # Create a game deck from the original deck
    game_deck = GameDeck(deck.cards)
    
    # Shuffle the game deck
    game_deck.shuffle()
    print("\nShuffled Deck:")
    for card in game_deck.game_deck:
        print(card)

    # Deal 5 cards from the game deck
    print("\nDealing 5 cards:")
    for _ in range(5):
        dealt_card = game_deck.deal_card()
        if dealt_card:
            print(dealt_card)
        else:
            print("No more cards to deal.")
    print(f"\nCards remaining in deck: {len(game_deck.game_deck)}")


# Run the main function
if __name__ == "__main__":
    main()