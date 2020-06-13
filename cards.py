import random

SUITS = ['clubs', 'dimonds', 'hearts', 'spades']
RANK = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'Ace' ]

rank = random.choice(SUITS)
suits = random.choice(RANK)
print(rank + ' of ' + suits)

deck = [ ]
for r in RANK:
    for s in SUITS:
        card = r + s
        print( r + ' of '+ s )
deck += [card]

# Shufelling
n = len(deck)
for i in range(n):
    r= random.randrange (0, i+1)
    deck[i], deck[r] = deck[r], deck[i]




