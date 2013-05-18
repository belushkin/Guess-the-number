# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
secret_number = 0
num_range = 100
guess_left = 7

def init():
    global secret_number
    global guess_left

    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", guess_left
    print ""
    secret_number = random.randrange(0, num_range)
    
# define event handlers for control panel
def range100():
    global num_range
    global guess_left

    num_range = 100
    guess_left = 7
    init()

def range1000():
    global num_range
    global guess_left

    num_range = 1000
    guess_left = 10
    init()

def get_input(guess):
    global guess_left
    guess_left -= 1

    print "Guess was", guess
    print "Number of remaining guesses is", guess_left

    if guess_left == 0:
        print "You loose";
        print ""

        if num_range == 100:
            range100()
            return False
        else:
            range1000()
            return False

    if int(guess) > secret_number:
        print "Lower!"
    elif int(guess) == secret_number:
        print "Correct!"
        print ""

        if num_range == 100:
            range100()
        else:
            range1000()
        return False
    else:
        print "Higher!"

    print ""

# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

init()

# start frame
frame.start()

# always remember to check your completed program against the grading rubric

