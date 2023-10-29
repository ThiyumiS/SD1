#Importing random number
import random
low=1
high=20
guess=random.randint(low,high)
guesses=0
num=0

#Asking user's input


while True :
    num=int(input("Enter number between 1 - 20 :"  ))

    if num!=guess:
        print("The",num,"is not correct")

        if num>guess:
            print( "The",num,"is too high")

        else:
            print("The",num,"is too low")
                                
                                        
    else:
        print("The",num,"is correct")
        break        



