#Represents a flash card
class Flashcard:
    def __init__(self,question:str, answer:str):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"Question: {self.question}\nAnswer: {self.answer}"
    