# numberle in python
# numberle is a game inspired from wordle where instead of guessing a 5 letter word you guess an equation 
from random import randint
## setup main class
class MainClass:
## setup instance method
    def __init__(self):
##generate a random number from 001 to 999
        self.total = randint(1, 999)
### generate an equation that equals to the random generated number
### give the user 6 tries to answer the question
### condition for if user guess the equation in or before 6 turns or fails
### ask user to continue or end game (setup while loop)
### keep track of user streak through a text file
