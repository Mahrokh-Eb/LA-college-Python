#send output to a text file rather than getting the result in terminal

import sys
import random

n = int(sys.argv[1])

for i in range(n):
    print(random.random())
print()