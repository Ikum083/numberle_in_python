# numberle in python
# numberle is a game inspired from wordle where instead of guessing a 5 letter word you guess an equation 
from random import randint
from generate_equation import Equation

## setup main class
class MainClass(Equation):
## setup instance method
    def __init__(self):
        try:
            with open("game_stats.txt", "r") as statistics:
                game_statistics = statistics.readlines()
                self.win = int(game_statistics[0].split('=')[1].strip())
                self.lost = int(game_statistics[1].split('=')[1].strip())
                self.win_streak = int(game_statistics[2].split('=')[1].strip())
                self.longest_winstreak = int(game_statistics[3].split('=')[1].strip())
        except IndexError:
            self.win = 0
            self.lost = 0
            self.win_streak = 0
            self.longest_winstreak = 0

        ##generate a random number from 001 to 99
        self.total = randint(1, 99)
        ### generate an equation that equals to the random generated number
        self.equation_used = Equation.generate_equation(self, self.total)
        self.answering = True
        self.answer_quantity = 0
        self.quantity_right_ans = 0

        print("--Welcome to numberle!--")
        print("Rules:")
        print("1. You must enter an equation with a limit of 8 characters")
        print("2. Use +, -, * and / to illustrate operations")
        print("3. You are limited  to 6 tries")
        print("4. We will display 'O' if the character is correct, 'H' if the answer is correct but in the wrong place and 'X' if the answer is wrong")
        print("5. Do not put spaces in between any of the characters")

        ### give the user 6 tries to answer the question
        while self.answering:
            self.correction = ""
            self.character = 0

            if self.answer_quantity == 6:
                print(f"\nYou lose! The equation is {self.equation_used}")
                self.lost += 1
                self.win_streak = 0
                self.answer_quantity = 0
                break

            print(self.equation_used)

            self.answer = input("\nEnter your  guess: ")

            if len(self.answer) != 8:
                print("Incorrect amount of characters")
                continue

            for a in self.answer:
                print(self.equation_used[self.character])
                if a == self.equation_used[self.character]:
                    self.correction += "O"
                    self.quantity_right_ans += 1
                else:
                    for b in self.equation_used:
                        if a == b:
                            self.correction += "H"
                            break
                        else:
                            continue
                    else:
                        self.correction += "X"
                self.character += 1

            print(f"\n{self.correction}")

            ### condition for if user guess the equation in or before 6 turns or fails
            if self.quantity_right_ans == 8:
                print(f"\nYou got it right!")
                self.win += 1
                self.win_streak += 1
                self.answering = False
            else:
                self.answer_quantity += 1
                self.quantity_right_ans = 0
                print(self.answer_quantity)
                continue

        if self.win_streak >= self.longest_winstreak:
            self.longest_winstreak = self.win_streak

        with open("game_stats.txt", "w") as statistics:
            statistics.write(f"Wins = {self.win}\n")
            statistics.write(f"Loses = {self.lost}\n")
            statistics.write(f"Current Winstreak = {self.win_streak}\n")
            statistics.write(f"Longest Winstreak = {self.longest_winstreak}\n")
    
    ### keep track of user streak through a text file
    def game_statistics():
        with open("game_stats.txt", "r") as game_statistics:
            for line in game_statistics:
                print(line)

if __name__ == "__main__":
    player_playing = True
    menu = True
    while player_playing:
        MainClass()

        ### ask user to continue or end game (setup while loop)
        while menu:
            print("\n1. Play again")
            print("2. Check game stats")
            print("3. Quit")
            game_menu = input("> ")

            if game_menu == "1":
                break
            elif game_menu == "2":
                MainClass.game_statistics()
                break
            else:
                quit()
