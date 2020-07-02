import random

def bernoulli(p= 0.5):
    return random.random()<p

n = 6
def binomial(n, p= 0.5):
    heads = 0
    for i in range(n):
        if bernoulli(p):
            heads +=1
    return heads