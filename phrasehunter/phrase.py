class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        

    def display(self, guesses):
        self.guesses = guesses
        for i in range(len(self.phrase)):
            if self.phrase[i] in self.guesses:
                print(self.phrase[i] + " ", end="")
            else:
                print("_ ", end="")