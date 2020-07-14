def checkPositive(num):
    while(num<0):
        num = int(input('please try + number again: '))
    return num

num1 = int(input('enter first + integer: '))
checkPositive(num1)

num2 = int(input('enter second + integer: '))
checkPositive(num2)
sum = num1 + num2
print('num1+ num2 = ' , sum)