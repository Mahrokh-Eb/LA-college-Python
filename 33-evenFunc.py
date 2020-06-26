'''
Programmer: Mahrokh Ebrahimi
Discription: check if a digit is odd or even
Date: 6/25/2020
'''
import sys

def even(n):
    if n <= 2: return False
    digit = n
    if digit % 2 == 0:
        print('it is even')
    elif digit % 2 !=0:
        print(' it is NOT odd!')
    return digit

print(even(int(sys.argv[1])))




