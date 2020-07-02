# generating random point
import sys
import stddraw
import stdrandom
def main():
    n = int(sys.argv[1])
    for i in range(n):
        x = stdrandom.gaussian(0.5, 0.2)
        y = stdrandom.gaussian(0.5, 0.2)
        stddraw.point(x, y)
    stddraw.show()

