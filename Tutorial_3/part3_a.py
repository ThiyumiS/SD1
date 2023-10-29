#Part3_a
# Ask the user for their choice
choice = input("Enter '1' to convert from Celsius to Fahrenheit or '2' to convert from Fahrenheit to Celsius: ")

# Convert Celsius to Fahrenheit
if choice == '1':
    # Get temperature from the user
    celsius = float(input("Enter the temperature in Celsius: "))
    
    # Apply the conversion formula
    fahrenheit = (celsius * 1.8) + 32
    
    # Display the converted temperature
    print("The temperature in Fahrenheit is: fahrenheit,°F")

# Convert Fahrenheit to Celsius
elif choice == '2':
    # Get temperature from the user
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    
    # Apply the conversion formula
    celsius = (fahrenheit - 32) / 1.8
    
    # Display the converted temperature
    print("The temperature in Celsius is: {celsius}°C")

# Handle invalid input
else:
    print("Invalid option entered.")
