# defining a function

def addNumbers(num1, num2):
    sum = num1 + num2
    return sum

for i in range(2):
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    result = print( num1 ,'+', num2, '=', addNumbers(num1, num2))