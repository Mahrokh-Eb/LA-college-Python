# random walker - self avoiding random walk
import random
import sys

n = int(sys.argv[1]) #tedade grid
trials = int(sys.argv[2])
dead_end = 0 #tedade that we face to dead-end

#tedad tekrare azmayesh ha
for t in range(trials):
        a = [[False] * n for i in range(n)]
        x, y = n//2, n//2
        while 0 < x < n-1 and 0 < y  < n-1:
            if a[x-1][y]and a[x+1][y]and a[x][y+1] and a[x][y-1]:
                dead_end += 1
                break
            a[x][y] = True

            r = random.random()
            if r < 0.25:
                if not  a[x+1][y]:
                    x += 1
                elif r < 0.5:
                    if not a[x-1][y]:
                        x -= 1
                elif r < 0.75:
                    if not a[x][y+1]:
                        y += 1
                else:
                    if not a[x][y-1]:
                        y -= 1
print(100 * dead_end // trials)






