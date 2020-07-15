'''Write a program in python that creates a calculator.
create a function menu with different options as following: (Output sample is below)
 main menu, and prompts for a choice
 Welcome to calculator.py
your options are:
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Quit calculator.py
Choose your option:
'''
# using functions

def checkValidation(option):
    while( option<0 or option>5):
        option = int(input('invalid number'))
    return option

def addition(num1, num2):
    return num1 + num2

def Subtraction(num1, num2):
    return num1 - num2

def Multiplication(num1, num2):
    return num1 * num2


option = 0
while (option !=5 ):
    option = int(input('which one? \n 1) Addition\n 2) Subtraction \n 3) Multiplication \n 4) Division \n 5) Quit calculator.py'))
    option = checkValidation(option)
    num1 = int(input('put num1= '))
    num2 = int(input('put num2= '))
    if option == 1:
        print(num1 ,'+', num2 ,'= ', addition(num1, num2))

    if option == 2:
        print(num1, '-', num2, '= ', Subtraction(num1, num2))

    if option == 3:
        print(num1, 'x', num2, '= ', Multiplication(num1, num2))
