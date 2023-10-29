#part6_(Using a nested if-else solution:)

#Part 4d. Avoid ZeroDivisionError in a simple calculator program
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

if num2 != 0:
    result = num1 / num2
    print("Result:", result)
else:
    print("Error: Cannot divide by zero.")
