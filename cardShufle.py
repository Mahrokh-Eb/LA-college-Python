import sys
import random

m = int(sys.argv[1])
n = int(sys.argv[2])

perm = [i for i in range(n)] #comprehension, kole list

for i in range(m): #un tedadi k mikhay
    r = random.randrange(i, n)
    perm[r], perm[i] = perm[i], perm[r]


for i in range(m):
    print(str(perm[i]), end=' ')
print()