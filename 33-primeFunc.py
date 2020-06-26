'''
Programmer: Mahrokh Ebrahimi
Discription: check if a digit is prime
Date: 6/25/2020
'''
import sys

def prime(n):
    if n <= 2: return False
    digit = n
    if digit % 2 == 0:
        print('it is prime')
    elif digit % 2 !=0:
        print(' it is NOT prime!')
    return digit

print(prime(int(sys.argv[1])))




