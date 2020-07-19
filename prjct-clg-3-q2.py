# it asks the user how many students exist
while True:
    try:
        studentsNum= int(input('how many students do you want to enter their names? it should be a digit number: '))
        break
    except:
        print('Enter a number not character please.')

# it gets all student's name and save in "esm"
esm = []
for i in range(studentsNum):
    name = [input('What is the student name? ')]
    esm += name
print(esm)

# it gets all student's score and save in "scores"
scores = []
for i in range(studentsNum):
    for j in range(3):
        score = [int(input('What is the score of 5 exams for the students in the order you entered their names? ' ))]
        scores += score
    print(scores)

# printing student's name and score in a matrix for esm and scores
print('studentName   ex1 ex2 ex3 ex4 ex5 \n===================================')
print(esm)
print(scores)

# find and return the lowest of the 5 scores passed to it
mini = min(scores)
maxi = 1
for i in scores:
    if i < mini:
        mini = i
    if i > maxi:
        maxi = i
print('minimum score is = ',mini)
print('maximum score is = ', maxi)

# dropping the highest and lowest scores the student received.
minIndx = scores.index(mini)
maxIndx = scores.index(maxi)
scores.remove(mini)
scores.remove(maxi)
print('min scores after removing minimumm and maximum scores: ',scores)

# the average of the scores that remain
for i in scores:
    sumofAll = sum(scores)
    average = sumofAll / len(scores)
print('the average is: ', average)
