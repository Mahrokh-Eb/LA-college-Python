# get as many as number till user doesn't enter, give the average!

import stdio

total = 0
count = 0

while not stdio.isEmpty():
     value = stdio.readInt()
     total += value
     count += 1
     print('Average is %.2f' %(total/ count))