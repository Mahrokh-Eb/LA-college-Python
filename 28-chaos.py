#it draws a triangle, every time in the midle of two points
import sys
import random
import stddraw

n = int(sys.argv[1])

cx = [0.0, 1.0, 0.50]
cy = [0.0, 0.0, 0.86]

x, y = 0, 0
for i in range(n):
    r = random.randrange(0,3) #entekhabe ye ras be surate tasadofi
    x = (x + cx[r])/2
    y = (y + cy[r])/2
    stddraw.setPenColor(stddraw.PINK)
    stddraw.point(x, y)
    #stddraw.show(0) # it causes to draw slow not all of a sudden

stddraw.show()




