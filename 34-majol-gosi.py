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

def Phi(z):
    if z < -8.0: return 0.0
    if z > 8.0: return 1.0
    total = 0
    term = z
    i = 3
    while total != total + term:
        total += term
        term *= z * z / float(i)
        i +=2
    return 0.5 + phi(z) * total

def cdf(z, mu = 0.0, sigma = 1.0):
    return phi((z - mu)/sigma) 