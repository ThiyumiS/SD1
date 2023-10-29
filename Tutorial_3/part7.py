#part7_Generating random numbers

import random

# Generate a random number: 0 or 1
coin_flip = random.randint(0, 1)

# Use an if-else statement to determine and print the result
if coin_flip == 0:
    print("Heads")
else:
    print("Tails")
