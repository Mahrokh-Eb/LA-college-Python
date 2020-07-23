'''
Read in 10 scores from a file, scores.txt
Write the 10 scores into another file.
Find the highest score and append it into the same file.
Find the lowest score and append it into the same file.
Find the average score and append it into the same file
'''
fileRead = open("score-clg-p13.txt", 'r')
fileWrite = open('score-result-clg-p13.py', 'w')
# secod way to read from txt file: print(fileRead.read())
def findMinimum(scores):
    minimum = scoresList[0]
    for i in scoresList:
        if i < minimum:
            minimum = i
    return minimum

#reading from txt file with a 'for loop'
for i in fileRead:
    # print(i): it shows the txt file
    # fileWrite.write(i): it writes in txt file
    # print(i.split()): it shows like a list
    # fileWrite.write(str(i.split()): it shows the txt file like a list
    myList = i.split()
    scoresList = []
    for j in range(2, len(myList)):
        scoresList.append(float(myList[j]))
        fileWrite.write(myList[j]+'  ')
    minimum = findMinimum(scoresList)
    fileWrite.write(str(minimum))
    print(scoresList )
    fileWrite.write("\n")





