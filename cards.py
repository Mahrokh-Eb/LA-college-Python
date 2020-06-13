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




