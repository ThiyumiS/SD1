#Importing random number
import random
max_guess=5
hidden=random.randint(1,20)
guesses_Taken=0
guess=0



for y in range(guesses_Taken,5):
    guesses_Taken += 1
    guess=int(input("Enter number between 1 - 20 :" ))

    
    if guess==hidden:
        print("Congrats!You got it in his round you took",guesses_Taken,"Guesss")
        break
    
    elif guess<hidden:
        print("Your guess is too low")

    else:
        print("Your guess is too high")
        
if guess!=hidden:
        print("Not guessed.The correct answer was:",hidden,"This round you took",guesses_Taken,"Guesss")

