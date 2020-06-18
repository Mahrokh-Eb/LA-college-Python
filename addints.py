import sys
import stdio
'''stdio library couldn't be imported. 
it is added mauallu by saving into another folder.'''

n = int(sys.argv[1])

total = 0
for i in range(n):
    total += stdio.readInt()


print('Sum is %d' %total )

'''output:
%puthon addints.py 4
10
20
30
40
Sum is 100. '''


