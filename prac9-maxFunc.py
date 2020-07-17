# finding maximum digit, using a function

def findMax(mylist):
    """
for finding the max
    """
    maxItem = mylist[0]
    for i in range(len(mylist)):
        if mylist[i] > maxItem:
            maxItem = mylist[i]
    print('max of the list is = ',maxItem)
    return mylist


mylist1 = [22, 33, 44, 55, 666, 7777]
findMax(mylist1)

mylist2 = [8, 88, 2384, 1975, -32]
findMax(mylist2)



