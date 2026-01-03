## Deck utility functions
import random

SUITS = ['Hearts ♥', 'Diamonds ♦', 'Clubs ♣', 'Spades ♠']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# Card class to represent a single playing card.
class Card:    
    # Initialize a card with suit, rank, and value.
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
    # String representation of the card
    def __str__(self):
        return f"{self.rank} of {self.suit}, value: {self.value}"
    

# Deck class to manage a collection of cards, its a tuple.
class Deck:
    # Initialize the deck with 52 cards.
    def __init__(self):
        self.cards = [] # Initialize an empty list for the deck
        for rank, value in zip(RANKS, VALUES): # Iterate through ranks and their corresponding values
            for suit in SUITS: # Iterate through each suit 
                self.cards.append(Card(suit, rank, value)) # Create a Card object and add it to the deck
        
    
    def get_cards(self):
        return tuple(self.cards) # Return the deck as a tuple for immutability

    # String representation of the deck
    def __str__(self):
        deck_comp = ''
        for card in self.cards:
            deck_comp += '\n ' + card.__str__()
        return "The deck has:" + deck_comp
    

# GameDeck class to manage the deck during gameplay.
class GameDeck(Deck):
    def __init__(self, deck):
        self.game_deck = [] # Initialize an empty list for the game deck
        self.game_deck = list(deck)  #transform tuple to list for mutability

    # Shuffle the deck of cards.
    def shuffle(self):
        random.shuffle(self.game_deck)

    # Deal a single card from the deck.
    def deal_card(self):
        return self.game_deck.pop() if self.game_deck else None
