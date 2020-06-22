# google search

import stdio
import random

n = stdio.readInt()
link_count = ([0] * n for i in range(n))
out_degrees = [0] * n

while not stdio.isEmpty():
    i = stdio.readInt()
    j = stdio.readInt()
    link_count[i][j] += 1
    out_degrees[i] += 1

print('%d %d'%(n,n))

#to print the matrix
for i in range(n):
    for j in range(n):
        p = 0.9 * (link_count[i][j] / out_degrees) + 0.1/ n
        print('%8.5f'%p, end='')
    print()


# %python transition.py < tiny.txt | randomsurfer.py 10000

