# defining the function befor solving, solved completed is in prjct-clg-3-v0
employees = ["M", "Miguel saba", "Maria Rami"]
salaries = [20, 30000.00, 40000.00]

employee = input('employee?  ')
salary = int(input('salary?  '))
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












