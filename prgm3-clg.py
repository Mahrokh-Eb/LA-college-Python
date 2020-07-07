# 1. Prompt the user for the size of the list (N). Then it should prompt the user to enter N numbers and store them into an list called burstList. Note, you should specify the maximum size of N allowed
n = int(input('Enter size of the list (N), consider,it should be an integer number'))

if n > 7:
    print('why is it more than 6?')
    n = int(input('for second time, the maximum size of N allowed is 6,  '))
    n = 0
    while True:
        n = int(input('I told you, less or equall to 6, we wait till you enter a number less than 6, '))
        if n < 7:
            break

print('now you have to enter', n, 'number to make a list')
burstList = []
i = 0
while (i < n):
    digit = int(input('put number to make a list '))
    x = burstList.insert(i, digit)
    i += 1
print(burstList)

# 2. Given N and list, your program should compute the lengths of the bursts of zeros and store them in an list called BurstLengths. Use a for loop in this step.
length = len(burstList)
print('length of list is = ', length)
BurstLengths = []
BurstLengths.append(length)
print(BurstLengths)