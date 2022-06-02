###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# # Try to figure out what this code is doing and how it might be useful to you
# import random
# digits = list(range(10))
# random.shuffle(digits)
# print(digits[:3])
#
# # Another hint:
# guess = input("What is your guess? ")
# print(guess)

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

#STARTING POINT
import random as rand

#GET USER GUESS:
def get_guess():
    u_guess = []
    user_guess = input("Please enter 3-digit number!!\n What is your guess?>>")
    user_guess.split()
    for i in range(3):
        u_guess.append(int(user_guess[i]))
    return u_guess
#Generate computer code:
def generate_code():
    guess_list = list(range(10))
    rand.shuffle(guess_list)
    return guess_list[:3]

c_guess = generate_code()
while True:
    u_guess = get_guess()
    print(u_guess)
    print(c_guess)
    if u_guess == c_guess:
        print('Perfect Match!!!')
        break
    elif (u_guess[0] in c_guess and u_guess[1] in c_guess and u_guess[2] in c_guess) and (u_guess[0] != u_guess[1]):
        print("Close!\n(meaning:you've guessed a correct number in the wrong position.)")

    elif u_guess[0] == c_guess[0] or u_guess[1] == c_guess[1] or u_guess[2] == c_guess[2]:
        print("Match!\n(meaning:you've guessed a correct number in the correct position.)")

    else:
        print("NOPE!\n")

#///////// by the instructor: ////////////
import random

def get_guess():
    '''
    Asks for the number guess and transforms the string to a list.
    '''
    return list(input("What is your guess?"))

def generate_code():
    '''
    generates a 3 digit list for the code
    '''
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues(code,userGuess):
    '''
    Takes in a user guess and code then compares the numbers in a loop and
    creates a list of clues according to the matching parameters.
    '''
    if userGuess == code:
        return "CODE CRACKED"

    clues = []

    # Compare guess to code
    for ind,num in enumerate(userGuess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues

# Run Game
print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

# Create a Secret Code to start the Game
secretCode = generate_code()
print("Code has been generated, please guess a 3 digit number")
#print(secretCode)

# Empty Clue Report to Start with
clueReport = []

# Keep asking until the user has gotten it right!
while clueReport != "CODE CRACKED":

    # Ask for guess
    guess = get_guess()

    # Give the clues
    clueReport = generate_clues(guess,secretCode)
    print("Here is the result of your guess:")
    for clue in clueReport:
        print(clue)
