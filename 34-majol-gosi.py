'''
Programmer: Mahrokh Ebrahimi
Discription: return cube of a digit
Date: 6/27/2020
'''
import math
def phi(x):
    return math.exp(-x*x/2.0)/math.sqrt(2.0*math.pi)

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x-mu)/sigma)/sigma
