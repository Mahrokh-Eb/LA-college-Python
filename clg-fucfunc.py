# calling function from another function
def main():
    def checkValidation(option):
        while (option < 0 or option > 5):
            option = int(input('invalid number'))
        return option

    def addition(num1, num2):
        return num1 + num2

    def Subtraction(num1, num2):
        return num1 - num2

    def Multiplication(num1, num2):
        return num1 * num2

    def Division(num1, num2):
        return num1 / num2

    def Quit():
        return exit()

    option = 0
    while (option != 5):
        option = int(input(
            'which one? \n 1) Addition\n 2) Subtraction \n 3) Multiplication \n 4) Division \n 5) Quit calculator.py'))
        option = checkValidation(option)

        if option !=5:

            num1 = int(input('put num1= '))
            num2 = int(input('put num2= '))

            if option == 1:
                print(num1, '+', num2, '= ', addition(num1, num2))

            elif option == 2:
                print(num1, '-', num2, '= ', Subtraction(num1, num2))

            elif option == 3:
                print(num1, 'x', num2, '= ', Multiplication(num1, num2))

            elif option == 4:
                print(num1, '/', num2, '= ', Division(num1, num2))

            else:
                exit()

main()