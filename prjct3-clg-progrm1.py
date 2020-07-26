# defining the function before solving, solved completed is in prjct-clg-3-v0. i put all the belows in func 
employees=["Mike navarro","Miguel saba","Maria Rami"]
salaries=  [20000.00, 30000.00, 40000.00]

#index = int(input('index? '))
'''
#2- Remove an Employee .......removeEmployee(employee, salary)
def removeEmployee(employee, salary):
    if employee in employees:
        employees.pop(employees.index(employee))
    print('employees after remove', employees)

    if salary in salaries:
        salaries.pop(salaries.index(salary))
    print('salaries after remove',salaries)
    return (employees, salaries)
removeEmployee(employee, salary)
'''
'''# 3- Insert an Employee into a specific location.....insertNewEmployee(employee, index, salary)
for i in range(0, len(employees), 1):
    employee = [employee]
    if i == index:
        list1 = [employees[i]]
        list2 = [employees[i+1]]
        employees =  [*list1, employee, *list2]

for i in range(len(salaries)):
    salary = [str(salary)]
    if i == index:
        list3 = [salaries[i]]
        list4 = [salaries[i+1]]
        salaries =  [*list3, salary, *list4]
print(employees , salaries)
'''
'''#4- Sort salaries in descending order .....sortSalaries(employees, salaries)
salary = [salary]
salaries += salary
for i in range(len(salaries)):
    for j in range(i+1, len(salaries)):
        if(salaries[i] < salaries[j]):
            temp = salaries[i]
            salaries[i] = salaries[j]
            salaries[j] = temp
print("Element After Sorting List in descending Order is : ", salaries)'''
'''#5- Search function for an employee ....searchEmployee(employee)
# --> will return the index and the salary
indexes = [index for index in range(len(employees)) if employees[index] == employee]
print ('index is: ',indexes)
strings = [str(integer) for integer in indexes]
a_string = "".join(strings)
an_integer = int(a_string)
#print(an_integer)
print('salary is: ',salaries[an_integer])'''
'''#6- find total salary ... totalSalary(salaries )
total = 0
for i in range(len(salaries)):
    total = total + salaries[i]
print('total salary is: ', total)
'''
'''#7- Display the list.... displayList(employees,  salaries)
print(employees)
print(salaries)'''
#8- Quit the program .....exit()
#exit()

# 1- Add a new Employee ..........addEmployee(employee, salary)
def addEmployee(employee, salary):
    global employees
    global salaries
    employees += employee
    salaries += salary
    return employees, salaries

# 2- Remove an Employee .......removeEmployee(employee, salary)
def removeEmployee(employee):
    global employees
    global salaries
    ei = employees.index(employee)
    employees.pop(ei)
    salaries.pop(ei)
    print(salaries)
    return employees

# 3- Insert an Employee into a specific location.....insertNewEmployee(employee, index, salary)
def insertNewEmployee(employee, index, salary):
    global employees
    global salaries
    print('lenght of the list is= ',len(employees))
    for i in range(len(employees)):
        if i == index:
            list1 =employees [slice(0,index )]
            list2 = employees[slice(index, len(employees))]
            employees = [*list1, employee, *list2]
            print(employees)

    for i in range(len(salaries)):
        #salary = [str(salary)]
        if i == index:
            list3 = salaries [slice(0,index )]
            list4 = salaries[slice(index, len(salaries))]
            salaries = [*list3, salary, *list4]
            print(salaries)

# 4- Sort salaries in descending order .....sortSalaries(employees, salaries)
def sortSalaries():
    global employees
    global salaries
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
        employee = [input('you select to add the employee. What is the name of the employee? ')]
        salary = [input('what is the salary? ')]
        print(addEmployee(employee, salary))

    # 2- Remove an Employee .......removeEmployee(employee, salary)
    if option == 2:
        employee = input('who is the employee that you want to remove?')
        #salary = input('what is the salary you want to remove?')
        print(removeEmployee(employee))

    # 3- Insert an Employee into a specific location.....insertNewEmployee(employee, index, salary)
    if option == 3:
        employee = input('employee to insert?  ')
        salary = int(input('salaryto insert?  '))
        index = int(input('index? '))
        insertNewEmployee(employee, index, salary)

    # 4- Sort salaries in descending order .....sortSalaries(employees, salaries)
    if option == 4:
        sortSalaries()


    # 5- Search function for an employee ....searchEmployee(employee)--> will return the index and the salary
    if option == 5:
        employee = input('put the employees name to find the index and salary for him/her')
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



