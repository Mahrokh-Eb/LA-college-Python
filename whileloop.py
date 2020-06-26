'''
Programmer: Mahrokh Ebrahimi
Discription: using while loop, using for loop
Date: 6/25/2020
'''
counter = 0

while (counter <= 3):
    print(counter)
    counter +=1
print()

# Discription: using for loop
for i in range(0, 4, 1):
    print(i)
print()

# nested for loop
for i in range(3):
    for j in range(4):
        print(i, 'x', j, '=', i*j)