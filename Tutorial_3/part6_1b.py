#part6_1b

#1b. Exception handling for age input
try:
    age = int(input('Enter your age: '))
    if age >= 18:
        print("You can vote")
    else:
        print("Sorry, you're too young to vote.")
except ValueError:
    print("Please enter a valid age as an integer value.")

