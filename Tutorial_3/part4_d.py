#part4_d*********
mark = int(input('Enter your exam mark: '))

# Check for invalid marks
if mark < 0 or mark > 100:
    print('Invalid exam mark.')

# Check if mark is 70 or more
elif mark >= 70:
    print('Exceptional result!')

# Check if mark is 40 or more but less than 70
elif mark >= 40:
    print('Satisfactory result!')

# All other cases (mark is less than 40)
else:
    print('You have failed.')
