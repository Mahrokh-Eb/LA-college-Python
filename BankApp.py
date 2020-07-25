
# opening txt file
fileRead = open('UserInformtion.txt', 'r')
#reading username, passwords, and balances for each customer, and store them into three lists.
userName = []
passWord = []
balances = []
for i in fileRead:
    myList = i.split()

    for j in range(0, 1):
        userName += [myList[j]]

    for k in range(1,2):
        passWord.append(myList[k])

    for t in range(2, len(myList)):
        balances.append(float(myList[t]))
def menue(indexBalance):
    option = 'A'
    while(option != 'D' or 'W' or 'B' or 'C' or 'E' ):
        option = input('Type D to deposit money\nType W to withdraw money\nType B to display Balance\nType C to change user, display user name\nType E to exit: ---')
        if (option == 'D'):
            depositAmount = int(input('what is the amount of deposit? '))
            validateUserInput(depositAmount)
            DepositFunction(depositAmount, indexBalance)
        elif (option == 'W'):
            withDrawAmount = int(input('what is the amount of money that you would like to withdraw? '))
            validateUserInput(withDrawAmount)
            withDrawFunction(withDrawAmount, indexBalance)

#function to check the input that is entered by user to make sure that t is not negetive
def validateUserInput(depositAmount):
    while (depositAmount<0):
        depositAmount = int(input('try again: '))
    return depositAmount
#function to deposit the money in the account
def DepositFunction(depositAmount, indexBalance):
    balanceChange = balances[indexBalance]
    balanceChange += depositAmount
    print('new balance after deposit is: ',balanceChange)
#function to withdraw money from the account
def withDrawFunction(withDrawAmount, indexBalance):
    balanceChange = balances[indexBalance]
    if (balanceChange > withDrawAmount):
        balanceChange -= withDrawAmount
        print('new balance after whthdrawing ',withDrawAmount, 'is= ', balanceChange )



print(userName)
print(passWord)
print(balances)

# getting username and password from the user
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
                        print('welcome Beauty!')
                        menue(indexBalance)








