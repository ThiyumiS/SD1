total=0
score=0
count=0
average=0

#Getting uer's inputs
score=int(input("Enter score,(Enter -9 to end): "))

while score != -9:
    total += score
    count +=1
    
    score=int(input("Enter score,(Enter -9 to end): ")) 

if count == 0:
    print("No scores were entered")
else:
    average=float(total)/count
    print("Class average is: ",average,"\n")





