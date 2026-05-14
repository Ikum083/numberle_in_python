# numberle in python
# numberle is a game inspired from wordle where instead of guessing a 5 letter word you guess an equation 
from random import randint
from generate_equation import Equation
## setup main class
class MainClass(Equation):
## setup instance method
    def __init__(self):
        ##generate a random number from 001 to 99
        self.total = randint(1, 99)
        ### generate an equation that equals to the random generated number
        self.equation_used = Equation.generate_equation(self, self.total)
        self.answering = True
        self.answer_quantity = 0
        self.win = 0
        self.lost = 0
        self.win_streak = 0
        self.quantity_right_ans = 0

        print("--Welcome to numberle!--")
        print("Rules:")
        print("1. You must enter an equation with a limit of 8 characters")
        print("2. Use +, -, * and / to illustrate operations")
        print("3. You are limited  to 6 tries")
        print("4. We will display 'O' if the character is correct, 'H' if the answer is correct but in the wrong place and 'X' if the answer is wrong")

        ### give the user 6 tries to answer the question
        while self.answering:
            self.correction = ""
            self.character = 0

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
                self.answering = False
            else:
                self.answer_quantity += 1
                self.quantity_right_ans = 0
                continue

            if self.answer_quantity == 6:
                print(f"\nYou lose! The equation is {self.equation_used}")
                self.answer_quantity = 0
                self.answering = False

if __name__ == "__main__":
    MainClass()

### ask user to continue or end game (setup while loop)
### keep track of user streak through a text file
