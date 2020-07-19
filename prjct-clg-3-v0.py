'''programmer: Mahrokh Ebrahimi COMPELETED
Description: Program1: LISTS & FUNCTIONS ( 50 Points)
For this program, you have to write your own functions without using any of the build in functions.
List functions that you CAN'T use: insert(), append(), remove(), del(), max(), min(), reverse(), sort(), etc.
Only functions that you MAY use:   len(), index(). Here is an sample output:

Create a menu to allow the user to add, insert, remove, find the maximum score, the minimum score, and sort the list in descending order (larger to smaller value).

These are your lists:
employees=["Mike navarro","Miguel saba","Maria Rami"]

salaries=  [20000.00, 30000.00, 40000.00]
1- Add a new Employee
2- Remove an Employee
3- Insert new Employee
4- Sort salaries in descending order
5- Search for an employee
6- find total salary
7- Display the list of employees
8- Quit the program .....exit()

===========================Here is more details for every function================

1- Add a new Employee ..........addEmployee(employee, salary)
2- Remove an Employee .......removeEmployee(employee, salary)
3- Insert an Employee into a specific location.....insertNewEmployee(employee, index, salary)
4- Sort salaries in descending order .....sortSalaries(employees, salaries)
5- Search function for an employee ....searchEmployee(employee) --> will return the index and the salary
6- find total salary ... totalSalary(salaries )
7- Display the list.... displayList(employees,  salaries)
8- Quit the program .....exit()

Please enter your option: 3

Where do you want to insert the item? (Enter the index number) 1
Please enter the employee name you want to insert: "Tina Mari"
Please enter the employee salary you want to insert: 65000.00
Your program should call the function insertNewEmployee(employee, index, salary)

Your original Lists:

employees = ["Mike navarro","Miguel saba","Maria Rami"]
salaries=  [20000.00, 30000.00, 40000.00]
After inserting an item into index 1:
employees = ["Mike navarro","Tina Mari", "Miguel saba","Maria Rami"]
salaries=  [20000.00, 65000.00, 30000.00, 40000.00]

Once the user enters an option, your program should execute the code for that option and displays the list before and after the operations. Make sure to use a while loop so the program runs until user enters the quit option.

Date: 7/16/2020
'''
employees = ["Mike navarro", "Miguel saba", "Maria Rami"]
salaries = [20000.00, 30000.00, 40000.00]


# 1- Add a new Employee ..........addEmployee(employee, salary)
def addEmployee(employee, salary):
    employees = ["Mike navarro", "Miguel saba", "Maria Rami"]
    salaries = [20000.00, 30000.00, 40000.00]
    employees += employee
    salaries += salary
    return employees, salaries


# 2- Remove an Employee .......removeEmployee(employee, salary)
def removeEmployee(employee, salary):
    employees = ["Mike navarro", "Miguel saba", "Maria Rami"]
    salaries = ['20000.00', '30000.00', '40000.00']
    if employee in employees:
        employees.pop(employees.index(employee))
    print('employees after remove', employees)

    if salary in salaries:
        salaries.pop(salaries.index(salary))
    print('salaries after remove', salaries)


# 3- Insert an Employee into a specific location.....insertNewEmployee(employee, index, salary)
def insertNewEmployee(employee, index, salary):
    employees = ["Mike navarro", "Miguel saba", "Maria Rami"]
    salaries = [20000.00, 30000.00, 40000.00]
    for i in range(0, len(employees), 1):
        employee = [employee]
        if i == index:
            list1 = [employees[i]]
            list2 = [employees[i + 1]]
            employees = [*list1, employee, *list2]
            print(employees)

    for i in range(len(salaries)):
        salary = [str(salary)]
        if i == index:
            list3 = [salaries[i]]
            list4 = [salaries[i + 1]]
            salaries = [*list3, salary, *list4]
            print(salaries)


# 4- Sort salaries in descending order .....sortSalaries(employees, salaries)
def sortSalaries(employee, salary):
    employees = ["Mike navarro", "Miguel saba", "Maria Rami"]
    salaries = [20000.00, 30000.00, 40000.00]
    salary = [salary]
    salaries += salary
    for i in range(len(salaries)):
        for j in range(i + 1, len(salaries)):
            if (salaries[i] < salaries[j]):
                temp = salaries[i]
                salaries[i] = salaries[j]
                salaries[j] = temp
    print("Element After Sorting List in descending Order is : ", salaries)


# 5- Search function for an employee ....searchEmployee(employee) --> will return the index and the salary
def searchEmployee(employee):
    indexes = [index for index in range(len(employees)) if employees[index] == employee]
    print('index is: ', indexes)
    strings = [str(integer) for integer in indexes]
    a_string = "".join(strings)
    an_integer = int(a_string)
    # print(an_integer)
    print('salary is: ', salaries[an_integer])


# 6- find total salary ... totalSalary(salaries )
def totalSalary(salaries):
    total = 0
    for i in range(len(salaries)):
        total = total + salaries[i]
    print('total salary is: ', total)


'''    
#7- Display the list.... displayList(employees,  salaries)
def displayList(employees,  salaries):

#8- Quit the program .....exit()


employees=["Mike navarro","Miguel saba","Maria Rami"]
salaries=  [20000.00, 30000.00, 40000.00]
print(employees)
print(salaries)
'''
print()
print(
    'what would you like to do?\n----------------------------------------------------------------------\n 1- Add a new Employee \n 2- Remove an Employee \n 3- Insert new Employee \n 4- Sort salaries in descending order \n 5- Search for an employee \n 6- find total salary \n 7- Display the list of employees \n 8- Quit the program .....exit()\n----------------------------------------------------------------------\n ')

option = 0
while (option <= 8):
    while True:
        try:
            option = int(input('Enter an option, it shoud be digit number:'))
            break
        except:
            print('enter a number between 1 & 8 !')

    # 1- Add a new Employee ..........addEmployee(employee, salary)
    if option == 1:
        employee = [input('who is the employee? ')]
        salary = [input('what is the salary? ')]
        print(addEmployee(employee, salary))

    # 2- Remove an Employee .......removeEmployee(employee, salary)
    if option == 2:
        employee = input(
            'who is the employee that you want to remove?(select betwwen "Mike navarro","Miguel saba","Maria Rami") ')
        salary = input('what is the salary you want to remove?(select between 20000.00, 30000.00, 40000.00) ')
        removeEmployee(employee, salary)

    # 3- Insert an Employee into a specific location.....insertNewEmployee(employee, index, salary)
    if option == 3:
        employee = input('employee to insert?  ')
        salary = int(input('salaryto insert?  '))
        index = int(input('index? '))
        insertNewEmployee(employee, index, salary)

    # 4- Sort salaries in descending order .....sortSalaries(employees, salaries)
    if option == 4:
        employee = input('put a new employee to sort in descending order?  ')
        salary = int(input('put a new salary to sort in descending order?  '))
        sortSalaries(employee, salary)

    # 5- Search function for an employee ....searchEmployee(employee)--> will return the index and the salary
    if option == 5:
        employee = input(
            'put the employees name to find the index and salary for him/her, between "Mike navarro","Miguel saba","Maria Rami"')
        searchEmployee(employee)

    # 6- find total salary ... totalSalary(salaries )
    if option == 6:
        totalSalary(salaries)

    # 7- Display the list.... displayList(employees,  salaries)
    if option == 7:
        print('print Employees: ', employees)
        print('print salaries: ', salaries)

    # 8- Quit the program .....exit()
    if option == 8:
        exit('goodbye :)')
