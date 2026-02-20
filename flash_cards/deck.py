from flashcard import Flashcard
import random

class Deck:
    def __init__(self, cards):
        self.__current_index = 0
        self.is_flipped = False

        self.cards = []
        for row in cards:
            question = row[0]
            answer = row[1]
            new_flashcard = Flashcard(question,answer)
            self.cards.append(new_flashcard)

    @property
    def current_index(self):
        return self.__current_index

    def next_card(self):
        # Usamos __current_index para modificarlo
        self.__current_index = (self.__current_index + 1) % len(self.cards)
        self.is_flipped = False

    def previous_card(self):
        # Usamos __current_index para modificarlo
        self.__current_index = (self.__current_index - 1) % len(self.cards)
        self.is_flipped = False

    def shuffle(self): # Corregido: shuffle
        random.shuffle(self.cards)
        self.__current_index = 0 # Usamos __current_index
        self.is_flipped = False

    def toggle_flip(self):
        self.is_flipped = not self.is_flipped   

    def get_current(self):
        return self.cards[self.__current_index]