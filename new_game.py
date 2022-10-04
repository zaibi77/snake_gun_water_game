import random
randNumber = random.randint(1,100)
userGuess = None
guessess = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess"))
    guessess += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        
        else:
            print("You guessed it wrong! Enter a larger number")
print(f"You guessed the number in {guessess} guesses")
