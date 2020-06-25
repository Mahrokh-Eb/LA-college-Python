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

for i in range(1, len(sys.argv)):
    arg = int(sys.argv[i])
    value = harmonic(arg) #function call
    print(value)

