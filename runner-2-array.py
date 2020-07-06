'''
Programmer: Mahrokh Ebrahimi

Description: Mike, Tina, Jason, Vicky, and Tammy are preparing for an upcoming marathon.
Each day of the week, they run a certain number of miles and write them into a notebook. At the end of the week, they would like to know the number of miles run each day, the total miles for the week, and average miles run each day, Write a program to help them analyze their data. Your program must contain parallel lists: a list to store the the names of the runners and a two-dimensional list of five rows and seven columns to store the number of miles run by each runner each day.

Sample Output
Name  Day 1   Day 2    Day 3    Day 4   Day 5   Day 6   Day 7   Average
=============================================
Mike   10.00   15.00    20.00   25.00    18.00    20.00    26.00    19.14
Tina   15.00   18.00    29.00   16.00    26.00    20.00    23.00    21.00
Jason  20.00   26.00    18.00   29.00    10.00    12.00    20.00    19.29
Vicky  17.00   20.00    15.00   26.00    18.00    25.00    12.00    19.00
Tammy  16.00   8.00     28.00   20.00    11.00    25.00    21.00    18.43

Date: 7/6/2020
'''

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
runner = []
total = 0
for i in range(5):
    names = input('Enter the name of the runners?')
    runner.append(names)
    for j in range(len(week_days)):
        while True:
            try:
                miles = float(input('how many miles did you run?'))
                break
            except:
                print('give digit not character')
        runner.append(miles)
        total = miles + total
    average = total / 7
    runner.append(average)
    print(
        "Name  Day 1   Day 2    Day 3    Day 4   Day 5   Day 6   Day 7   Average \n=========================================================== ")
    print(runner)






