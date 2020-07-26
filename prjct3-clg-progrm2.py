'''
programmer: Mahrokh Ebrahimi

Description: Student average score  50 pts
Professor Navarro is trying to find the average score for 5 exams. She wants to drop the lowest and highest scores from the list before finding the average.

Below is the list of  her students with 5 scores for 5 exams :

studentName   ex1 ex2 ex3 ex4 ex5
===================================
Jones Tom      94  99  96 74  56
Thompson Frank 67 58  86  95  47
Jackson Tom    95 97  94  87  67
Jackie Michael 43 23  34  77  64
Johnson Sara   84 93  64  57  89
Colt McCoy     84 93  64  57  70
Freeman Tina   67 58 86  95  47
First, we will ask the user to enter student name and  scores for 5 exams. Store these information into a two dimensional list (matrix)
Your program should include the following functions:

  getStudentInfo() should ask the user for student info including student name and 5 scores, before storing each of these scores into the list, make sure to validate it by calling another function ValidateUserInput(score). The function getStudentInfo() should be called from the main program.
findLowest(scores) should find and return the lowest of the 5 scores passed to it. NOTE: You are not allowed to use min() function
findHighest(scores) should find and return the highest of the 5 scores passed to it. NOTE: You are not allowed to use max() function
    • calcScore(scores) should calculate and return the average of the 3 scores that
       remain after dropping the highest and lowest scores the student received. This
       function should be called just once by main and should be passed the scores.

Two additional functions, described above findHighest() and findLowest(), should be called by calcScore, which uses the returned information to determine which of the scores to drop.

Date: 7/16/2020
'''

def getStudentInfo():
    '''ask the user for student info including student name and 5 scores'''
    # it gets all student's name and save in "esm"
    esm = []
    for i in range(studentsNum):
        name = [input('What is the student name? ')]
        esm += name
    print(esm)

    # it gets all student's score and save in "scores"
    global scores
    scores = []
    for i in range(studentsNum):
        global score
        for j in range(3):
            score = int(input('What is the score of 5 exams for the students in the order you entered their names? '))
            score = ValidateUserInput(score)
            scores += [score]
        print(scores)

def ValidateUserInput(score):
    '''validate score by calling another function ValidateUserInput(score)'''
    while (score<0 or score>100):
        newScore = int(input('try again! What is the score of 5 exams for the students in the order you entered their names?'))
        score = newScore
        break
    return score

def findLowest(scores):
    '''find and return the lowest of the 5 scores passed to it'''
    global mini, maxi
    mini = min(scores)
    maxi = 1
    for i in scores:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i
    print('minimum score is = ', mini)


def findHighest(scores):
    '''find and return the highest of the 5 scores passed to it'''
    mini = min(scores)
    maxi = 1
    for i in scores:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i
    print('maximum score is = ', maxi)


def  calcScore(scores):
    # the average of the scores that remain
    for i in scores:
        sumofAll = sum(scores)
        average = sumofAll / len(scores)
    print('the average is: ', average)




# it asks the user how many students exist
while True:
    try:
        studentsNum = int(input('how many students do you want to enter their names? it should be a digit number: '))
        break
    except:
        print('Enter a number not character please.')

# printing student's name and score in a matrix for esm and scores
print('studentName   ex1 ex2 ex3 ex4 ex5 \n===================================')
getStudentInfo()
findLowest(scores)
findHighest(scores)
#dropping the highest and lowest scores the student received.
minIndx = scores.index(mini)
maxIndx = scores.index(maxi)
scores.remove(mini)
scores.remove(maxi)
print('min scores after removing minimumm and maximum scores: ', scores)
calcScore(scores)
