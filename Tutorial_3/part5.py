#part5
#Basic Structure with if, elif, and else
response = input("Do you like Python? (yes/no): ")

if response == "yes":
    print("You are on the right course!")
elif response == "no":
    print("You might change your mind.")
else:
    print("I did not understand.")
    
#Accept Additional Ways of Saying Yes/No
response = input("Do you like Python? (yes/no): ")

if response == "yes" or response == "Yes" or response == "y":
    print("You are on the right course!")
elif response == "no" or response == "No" or response == "n":
    print("You might change your mind.")
else:
    print("I did not understand.")

#Using the lower() Method
response = input("Do you like Python? (yes/no): ")
response = response.lower()

if response == "yes" or response == "y":
    print("You are on the right course!")
elif response == "no" or response == "n":
    print("You might change your mind.")
else:
    print("I did not understand.")
