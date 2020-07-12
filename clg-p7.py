'''
Programmer: Mahrokh Ebrahimi

Description:
 -Write a program to declare two empty lists one is for name and one for salaries. Within the for loop ask for employees name and their salaries and append them into the list accordingly. Find out the total salary using accumulation concept but you need to call a function called EvaluateSalary() within the for loop passing the argument salary for each iteration.

Output : Both of the lists with their items and the total salary.

Date: 7/10/2020
'''

name = []
salary = []
total = 0

for i in range(2):
    nameask = input('what is your name?')
    name.append(nameask)
    salaryask = int(input('how muh is your salary?'))
    salary.append(salaryask)
    total += salary[i]
print(name, salary, total)

# def EvaluateSalary():
