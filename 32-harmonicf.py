'''
Programmer: Mahrokh Ebrahimi
Discription: python structure programming
             1-imports 2-defining the functions 3-global part (calling the functions)
Date: 6/24/2020
'''
import sys

def harmonic(n):
    total = 0
    for i in range(1, n+1):
        total += 1/ i
    return total
                # len array = number of it's var
for i in range(1, len(sys.argv)): #تو کتابخونه sys یه متغیری به نام argv وجود داره که یک ارایه هست.- پردازش آرایه با حلقه for
    arg = int(sys.argv[i])
    value = harmonic(arg) #function call
    print(value)

'''
output command:
 python 32-harmonicf.py 2 4 5 
1.5
2.083333333333333
2.283333333333333
'''