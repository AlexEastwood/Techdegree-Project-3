from phrasehunter.game import Game

if __name__ == "__main__":
    while True:
        game = Game()
        game.start()
        while True:
            yes_no = input("Would you like to play again? Y/N\n")
            if yes_no.upper() == "Y":
                break
            elif yes_no.upper() == "N":
                print("Goodbye")
                exit()
            else:
                continue
    