import sys
import random
import stdio

moves = int(sys.argv[1])

n = stdio.readInt()
stdio.readInt()

p = [[0, 0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        p[i][j] = stdio.readFloat()

hit = [0]* n
page = 0

for i in range(moves):            #rolet Wheel- احتمال تجمعی
    r = random.random()
    total = 0
    for j in range(n):
        total += p[page][j]
        if r < total:
            page = j
            break
    hit[page] +=1

for v in hit:
    print('%8.5f' % (1* v/ moves), end =' ')


