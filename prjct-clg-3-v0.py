#usinf a function rather than remove() in the list

employees = ["Mike navarro", "Miguel saba", "Maria Rami"]
salaries = [20000.00, 30000.00, 40000.00]
print(employees.index('Miguel saba'))
print(employees[1])

employee = input('employee to remove?')


#2- Remove an Employee .......removeEmployee(employee, salary)
index = employees.index(employee)
smallest = employees[0]
for i in range(1, len(employees)):
    if employees[i] < smallest:
        smallest = employees[i]


