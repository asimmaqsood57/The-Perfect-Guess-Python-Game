
#  Number Guessing Game : The Prefect Guess
#  I hope you will enjoy it. Please try once


import random

randomNum = random.randint(1, 100)


guessNum = 0

totalNumberOfGuesses = 0


while(guessNum != randomNum):
    guessNum = int(input("Enter any Number\n"))
    totalNumberOfGuesses += 1

    if(guessNum == randomNum):
        print("Congratulations! You guessed the right number")
    else:
        if(guessNum < randomNum):
            print(
                "Sorry! You didn't guessed the right number. Please enter a greater Number.")
        else:
            print(
                "Sorry! You didn't guessed the right number. Please enter a smaller Number.")


print(f"You guessed the Number in {totalNumberOfGuesses} guesses.")


with open("highScore.txt", "r") as f:
    currentHighScore = int(f.read())

if(totalNumberOfGuesses < currentHighScore):
    with open("highScore.txt", "w") as f:
        f.write(str(totalNumberOfGuesses))
