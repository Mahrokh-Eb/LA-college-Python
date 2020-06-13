import sys

n = int(sys.argv[1])

i = 0
power = 1
while i <= n:
    print(str(i) + ' ' + str(power))
    i = i +1
    power= power*2

