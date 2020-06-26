'''
Programmer: Mahrokh Ebrahimi
Discription: check if a digit is prime
Date: 6/25/2020
'''
import sys


def prime(n):
    digit = int(sys.argv[n])
    if digit / 2 == 0:
        print('it is prime')
    else:
        print(' it is NOT prime!')
    return digit

digit = int(sys.argv[1])
for i in range(digit):
    num = prime(n)




