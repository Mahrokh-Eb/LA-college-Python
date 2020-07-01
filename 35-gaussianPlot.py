# draw plot
import sys
import stddraw
import gaussian

def main():
    n = int(sys.argv[1])
    stddraw.setYscale(-4, 4)
    stddraw.setYscale(0, 5)
    stddraw.setPenRadius(0.1)

    x = [0.0] * (n+1)
    y = [0.0] * (n+1)

    for i in range(n+1):
        x[i] = -0.4 + 0.8 * i/n
        y[i] = gaussian.pdf(x[i])

    for i in range(n):
        stddraw.line(x[i], y[i], x[i+1], y[i+1])
    stddraw._show()

if __name__ == '__main__':
    main() 
