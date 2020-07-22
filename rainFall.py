'''Using Files—Total and Average Rainfall

Write a program that reads in from a ﬁle a starting month name, an ending month name,
and then the monthly rainfall for each month during that period. As it does this, it should
sum the rainfall amounts and then report the total rainfall and average rainfall for the
period. For example, the output might look like this:
During the months of March–June the total rainfall was 7.32 inches and the average
monthly rainfall was 1.83 inches.
Data for the program can be found in the Rainfall.txt ﬁle.
Hint: After reading in the month names, you will need to read in rain amounts until
the EOF is reached, and count how many pieces of rain data you read in.
Using notepad you can create a data file called Rainfall.txt with the following data.'''

#reading from txt file
fileRead = open('rainFall.txt', 'r')
fileWrite = open('rainFallResult.txt', 'w')

#print(fileRead.read())
line = 1
total = 0
for i in fileRead:
    if line ==3:
        fileWrite.write(i)
        myList = i.split() #it split to a list
        print(myList)
        print(i)         #it is string
        for j in myList:
            total += float(j)
    line +=1

print(total)
print('average = ', format(total/(len(myList)),'.2f' ))
fileWrite.write('    average rainfall = '+ format(total/(len(myList)),'.2f' ))
fileWrite.write('\n'+'done')



