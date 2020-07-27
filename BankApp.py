'''
programmer: Mahrokh Ebrahimi
Discription: appliction for bank. user can withdraw, deposite, display his/her balance and
changing the user by choosing different options. it uses the database which is saved on a txt file
named:'UserInformtion'
========
Mike Jane Steve
sorat1237# -- para432@4 -- asora8731%
Date 7/24/2020
'''
# opening txt file
fileRead = open('UserInformtion.txt', 'r')
#reading username, passwords, and balances for each customer, and store them into three lists.
userName = []
passWord = []
balances = []
#reading from txt file
for i in fileRead:
    myList = i.split()

    for j in range(0, 1):
        userName += [myList[j]]

    for k in range(1,2):
        passWord.append(myList[k])

    for t in range(2, len(myList)):
        balances.append(float(myList[t]))

#function to ask user what he wants to do
def menue(indexBalance):
    option = 'A'
    while(option != 'D' or 'W' or 'B' or 'C' or 'E' ):
        option = input('Type D to deposit money\nType W to withdraw money\nType B to display Balance\nType C to change user, display user name\nType E to exit: ---')
        if (option == 'D'): #deposit
            depositAmount = int(input('what is the amount of deposit? '))
            validateUserInput(depositAmount) #calling function to validate user input to make sure that it is not negetive
            DepositFunction(depositAmount, indexBalance) #calling function to deposite the function and show new balance
        elif (option == 'W'): #withdraw
            withDrawAmount = int(input('what is the amount of money that you would like to withdraw? '))
            validateUserInput(withDrawAmount)
            withDrawFunction(withDrawAmount, indexBalance)
        elif (option == 'B'): #display the balance
            ShowBalanceFunction()
        elif (option == 'C'): #change the user
            ChangeUserFunction()
        elif (option == 'E'): #exit
            exit('Goodbye :)')

#function to validate the option
def validateOption(option):
    while(option != 'D' or 'W' or 'B' or 'C' or 'E' ):
        option = int(input('option is invalid! '))
    return option

#function to check the input that is entered by user to make sure that t is not negetive
def validateUserInput(depositAmount):
    while (depositAmount<0):
        depositAmount = int(input('try again: '))
    return depositAmount

#function to deposit the money in the account
def DepositFunction(depositAmount, indexBalance):
    global balanceChange
    balanceChange = balances[indexBalance]
    balanceChange += depositAmount
    print('new balance after deposit is: ',balanceChange)

#function to withdraw money from the account
def withDrawFunction(withDrawAmount, indexBalance):
    global balanceChange
    balanceChange = balances[indexBalance]
    if (balanceChange > withDrawAmount):
        balanceChange -= withDrawAmount
        print('new balance after whthdrawing ',withDrawAmount, 'is= ', balanceChange )

#function to display the balance
def ShowBalanceFunction():
    global balanceChange
    #balanceChange = balances[indexBalance]
    print('the balance is= ', balanceChange)

#function to change the user
def ChangeUserFunction():
    main()

'''print(userName)
print(passWord)
print(balances)'''

# getting username and password from the user
def main():
    global indexBalance
    while True:
        user = input('please Enter your userName: ')
        user = user.strip()
        userPass = input('please Enter your password: ')
        userPass = userPass.strip()
        # checking the username and password if they are matched
        for i in userName:
            if i == user:
                indexUser = userName.index(i)
                indexBalance = userName.index(i)
                print(indexBalance)
                for j in passWord:
                    if j == userPass:
                        indexPass = passWord.index(j)
                        if indexUser == indexPass:
                            global balanceChange
                            balanceChange = balances[indexBalance]
                            print('welcome Beauty!')
                            menue(indexBalance)
main()








