import sys
import random

stake = int(sys.argv[1]) # mojudi avaliye, your initial investment
goal = int(sys.argv[2])
trial = int(sys.argv[3]) # dafati k mikham in azmayesho konm

wins = 0
bets = 0

for t in range(trial):
    cashe= stake
    while 0 < cashe < goal:
        bets +=1
        if random.randrange(0,2)==0 :
            cashe +=1
        else:
            cashe -=1
    if cashe==goal:
        wins +=1

print(str(100* wins// trial))
print(str(bets// trial))






