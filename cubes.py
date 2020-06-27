'''
Programmer: Mahrokh Ebrahimi
Discription: return cube of a digit
Date: 6/26/2020
'''

import sys

#function
def cubes(i):
    j = i * i * i
    return j

#starting the program and calling the function
n = int(sys.argv[1])
for i in range(1, n+1):
    print('%s %s' %(i ,cubes(i)))





