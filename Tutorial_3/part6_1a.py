#part6_1a

#1a. Exception handling for number over 100
try:
    n = int(input('Give me a number over 100: '))
    if n <= 100:
        print(n, 'is not over 100')
    else:
        print("Thank you for providing a number over 100!")
except ValueError:
    print("Please enter a valid integer value.")
