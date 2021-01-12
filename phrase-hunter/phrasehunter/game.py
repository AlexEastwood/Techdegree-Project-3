from .phrase import Phrase


class Game():
    def __init__(self, missed, phrases, active_phrase, guesses):
        self.missed = 0
        self.phrases = [Phrase(), Phrase(), Phrase(), Phrase(), Phrase()]
        self.active_phrase = None
        self.guesses = []
        
    
    
    