##################################
#
#  Exercise 18: Decode a webpage
#  https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
#
##################################

import random as rand

SIZE = 4

def getRandomNumber():
    numbers = rand.sample(range(9), SIZE)
    return "".join([str(i) for i in numbers])

def checkGuess(cpuNumber, userNumber):
    result = {
        "cows": 0,
        "bulls": 0
        }

    for i in range(len(cpuNumber)):
        if userNumber[i] == cpuNumber[i]:
            result["cows"] += 1
        elif userNumber[i] in cpuNumber:
            result["bulls"] += 1
    return result


if __name__=="__main__":
    cpuNumber = getRandomNumber()
    while True:
        invalidInput = True
        while invalidInput:
            guess = input("Guess a " + str(SIZE) + " digit number: ")
            if len(guess) != SIZE:
                print("Invalid size. Number must be " + SIZE + " digits long")
            else:
                invalidInput = False
        result = checkGuess(cpuNumber, guess)
        if result["cows"] == SIZE:
            print("Correct! The number was " + cpuNumber + ".")
            break
        else:
            print("Incorrect. " + guess + " had " + str(result["cows"]) + " cows and " + str(result["bulls"]) + " bulls. Guess again.")
        

