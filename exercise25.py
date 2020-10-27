##################################
#
#  Exercise 25: Guessing Game Two
#  https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
#
##################################

def main():
    startingList = range(100)

    print("Think of a number between 1 and 100")
    
    lower, upper, guess, i = 1, 100, 50, 0


    correct = False

    while not (correct):
        i += 1        
        guess = ((upper - lower) // 2) + lower

        isCorrect = input("Is your number " + str(guess) + " (yes/low/high): ") 

        if isCorrect == "low":
            lower = guess
        elif isCorrect == "high":
            upper = guess
        elif isCorrect == "yes":
            correct = True
        else:
            i -= 1
            print("Incorrect response. Should be yes/low/high ")

    print("Your number is " + str(guess))
    print("It took " + str(i) + " guess(es)")





if __name__ == "__main__":
    main()