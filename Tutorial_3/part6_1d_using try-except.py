#part6_1d(Using a try-except solution)

#Part 4d. Avoid ZeroDivisionError in a simple calculator program

try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
