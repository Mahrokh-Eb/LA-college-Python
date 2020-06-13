import sys
n = int (sys.argv[1])

power = 1
for i in range(n+1):
    print(str(i)+ ' '+ str(power))
    power = power*2
