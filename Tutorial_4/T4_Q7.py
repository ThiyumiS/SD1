import random

num_rolls=100
double_count=0

for x in range(num_rolls):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)

    if dice1 == dice2:
        double_count +=1

print("Out of 100 you rolled",double_count,"doubles")
