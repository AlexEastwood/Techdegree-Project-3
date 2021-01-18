class Phrase(): 
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        

    def display(self, guesses):
        self.guesses = guesses
        print("\n")
        for i in range(len(self.phrase)):
            if self.phrase[i] in self.guesses:
                print(self.phrase[i] + " ", end="")
            else:
                print("_ ", end="")
                
        print("\n")
        
    def check_guess(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False
        
    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False

        return True