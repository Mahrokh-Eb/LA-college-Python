import stddraw

RADIUS, DT = 0.05, 15

#defult for canvus is 0, 1,,we change scales
stddraw.setXscale(-1.0, +1.0)
stddraw.setYscale(-1.0, +1.0)

#start point of the ball
rx, ry = .48, .86
#speed of the ball
vx, vy = .015, .023

while True:
    if abs(rx + vx)+ RADIUS > 1.0: vx= -vx
    #absolute value = -1 < rx+vx < +1
    if abs(ry, vy)+ RADIUS > 1.0: xy= -vy

    #to update the locTion of the ball
    rx = rx+ vx
    ry= ry + vy

    #clean the convus
    stddraw.clear(stddraw.PINK)
    #draw a ball in rx, ry
    stddraw.filledCircle(rx, rx, RADIUS)
    #now wait
    stddraw.show(DT)


