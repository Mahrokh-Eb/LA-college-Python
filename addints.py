import sys
import stdio

n = int(sys.argv[1])

total = 0
for i in range(n):
    total += stdio.readInt()


print('the sum is %d' %total )

