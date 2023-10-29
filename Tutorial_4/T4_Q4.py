num=0
total=0



for x in range (5):
    try:
        num=int(input("Enter a number:"))
        total+=num
    except ValueError:
        print("Please enter valid number")
print("The total number 5 numbers is:",total)
