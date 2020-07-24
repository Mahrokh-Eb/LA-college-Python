
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
def menue():
    option = input('Type D to deposit money\nType W to withdraw money\nType B to display Balance\nType C to change user, display user name\nType E to exit: ---')
    if (option==D):
        depositAmount = int(input('what is the amount of deposit? '))
        DepositFunction(depositAmount)

def DepositFunction(depositAmount):
#index e user o pass ro dari,
# vhamun index male balance e. uno update kon
# project2, program1, mige keep displaying menue untill user bege exit


#print(userName[0:1]) it gives mike
print(userName)
print(passWord)
# username ro az user begir age tu liste username hat bud, index un ro dar are
# pass ro az user begir, ba passe marbut be un user compare kon,
# passe marbut b un ro az indexesh mifahmi.
# age index e user 1, e. ba pass index i compare kon

#list2 = ['cat', 'bat', 'mat', 'cat', 'pet']
# Will print the index of 'cat' in list2
#print(list2.index('cat'))


while True:
    user = input('please Enter your userName: ')
    user = user.strip()
    userPass = input('please Enter your password: ')
    userPass = userPass.strip()

    for i in userName:
        if i == user:
            indexUser = userName.index(i)
            for j in passWord:
                if j == userPass:
                    indexPass = passWord.index(j)
                    if indexUser == indexPass:
                        print('welcome Beauty!')
                        menue()








