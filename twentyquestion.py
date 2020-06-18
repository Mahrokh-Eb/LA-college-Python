#game. guess a number between 1 and 100

import random
import stdio

RANGE= 100
secret = random.randrange(1,RANGE+1)
print('guess a number between 1 and %d' %RANGE)

guess= 0
while guess !=secret:
    print('what is your guess?', end=' ')
    guess = stdio.readInt()

    if guess < secret: print('too low')
    elif guess > secret: print('too high')
    else:
        print('you win!')



