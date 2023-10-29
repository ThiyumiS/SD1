#part3_c **********
# Ask the diner for the cost of the meal
meal_cost = float(input("Enter the cost of the meal: "))

# Ask the diner for their satisfaction level
rating = int(input("How satisfied were you with your service?\n1 = Totally satisfied\n2 = Satisfied\n3 = Dissatisfied\nEnter your rating (1, 2, or 3): "))

# Calculate tip based on satisfaction level
if rating == 1:
    tip_percentage = 0.20
    satisfaction_level = "Totally satisfied"
elif rating == 2:
    tip_percentage = 0.15
    satisfaction_level = "Satisfied"
elif rating == 3:
    tip_percentage = 0.10
    satisfaction_level = "Dissatisfied"
else:
    print("Invalid satisfaction rating entered.")
    exit()

# Calculate the tip
tip = meal_cost * tip_percentage

# Display the satisfaction level and tip
print("\nSatisfaction level:", satisfaction_level)
print("Suggested tip based on your satisfaction: $", round(tip, 2))
