'''# it asks the user how many students exist
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
    for j in range(5):
        score = [int(input('What is the score of 5 exams for the students in the order you entered their names? ' ))]
        scores += score
    print(scores)
'''
'''# printing student's name and score in a matrix for esm and scores
print('studentName   ex1 ex2 ex3 ex4 ex5 \n===================================')
for i in range(len(esm)):
    print(esm[i])
    for j in range(5):
        print(scores[j])'''


'''for i in range(studentsNum):
    name = input('student name? ')

    for j in range(3):
        score = [int(input('What is the score of the exams? '))]
    print(name, score)'''

# A basic code for matrix input from user

R = int(input("Enter the number of students (rows):"))
C = 5

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):  # A for loop for row entries
      a = []
      for j in range(C):  # A for loop for column entries
            a.append(int(input('put score of exams: ')))
      matrix.append(a)

# For printing the matrix
for i in range(R):
      for j in range(C):
            print(matrix[i][j], end=" ")
      print()
