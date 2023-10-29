#Initializing the variables
hidden=6

#Asking user's input
guess=int(input("Enter number between 1 and 20: "))

while guess!=hidden:
    print("Guess is not correct")
    guess=int(input("Enter number between 1 and 20: "))
    
print("Your guess is correct")
