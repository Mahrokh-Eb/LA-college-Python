import stdio
import stddraw

#convos plot
x0= stdio.readFloat()
x1= stdio.readFloat()
y0= stdio.readFloat()
y1= stdio.readFloat()

#scale of canvus
stddraw.setXscale(x0, x1)
stddraw.setXscale(y0, y1)

#draw point
while not stdio.isEmpty():
    x= stdio.readFloat()
    y= stdio.readFloat()
    stddraw.point(x, y)

stddraw.show()
