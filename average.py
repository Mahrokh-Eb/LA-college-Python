import stdio

total = 0
count = 0

while not stdio.isEmpty():
     value = stdio.readInt()
     total += value
     count += 1
     print('Average is %.2f' %(total/ count))