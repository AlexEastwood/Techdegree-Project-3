from phrasehunter.phrase import Phrase
import random

class Game():
    def __init__(self):
        self.missed = 0
        self.phrases = ["Hello World", "The Cat in the Hat", "Now dig on this", "Watch the hands", "This is your stage"]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def get_random_phrase(self):
        return random.choice(self.phrases)