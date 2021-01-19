from phrasehunter.phrase import Phrase
import random

class Game():
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("Hello World"), 
                        Phrase("The Cat in the Hat"), 
                        Phrase("Now dig on this"), 
                        Phrase("Watch the hands"), 
                        Phrase("This is your stage")]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    def welcome(self):
        print("===========================\n"
              "  Welcome to Phrase Hunter\n"
              "===========================\n")
        
    def start(self):
        self.welcome()
        while self.active_phrase.check_complete(self.guesses) == False and self.missed < 5:
            print(f"Number missed: {self.missed}")
            self.active_phrase.display(self.guesses)
            self.user_guess = self.get_guess()
            self.guesses.append(self.user_guess)
            if not self.active_phrase.check_guess(self.user_guess):
                self.missed += 1
        
        self.game_over()
        
    def get_guess(self):
        while True:
            guess = input("\nPlease guess a letter\n")
            if guess.isalpha() and len(guess) == 1:
                return guess
            else:
                continue
        
    def game_over(self):
        if self.missed >= 5:
            print("You lose!")
        else:
            print("You win!")