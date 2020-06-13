import sys

n= int(sys.argv[1])

total= 0
for i in range(1, n+1):
    total += 1/i
print(total)

# sum= 1 + 1/2 + 1/3 +....+ 1/n