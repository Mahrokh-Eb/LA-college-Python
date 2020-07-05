'''
Programmer: Mahrokh Ebrahimi

Description:Program1: List Menu operation
Create a menu to allow the user to add, insert, remove, find the maximum, the minimum, and sort the list in descending order (larger to smaller value). Declare your list as list of string.

studentFullName=["Mike navarro","Miguel saba","Maria Rami"]

You may use any of build in functions. Here is an sample output:

1- Add an item to the list
2- Remove an item from the list
3- Insert an item to the list
4- Find maximum
5- Find Minimum
6- Sort the list in descending order
7- Quit the program

Please enter your option: 3

Where do you want to insert the item? (Enter the index number) 1

Please enter the value for the item you want to insert: "Tina Mari"

Your original List : ["Mike navarro","Miguel saba","Maria Rami"]

After inserting an item into index 1:

["Mike navarro","Tina Mari", "Miguel saba","Maria Rami"]

Once the user enters an option, your program should execute the code for that option and displays the list before and after the operations. Make sure to use a while loop so the program runs until user enters the quit option.
Date: 7/2/2020
'''

studentFullName=["Mike navarro", "Miguel saba", "Maria Rami"]
print(studentFullName)
print('what would you like to do?')
print('1- Add an item to the listz')
print('2- Remove an item from the list')
print('3- Insert an item to the list')
print('4- Find maximum')
print('5- Find Minimum')
print('6- Sort the list in descending order')
print('7- Quit the program')

option = int(input('please enter your option'))


#1- Add an item to the list
if option == 1:
    add_item = input('what is the item you want to add?')
    studentFullName.append(add_item)
    print(studentFullName)

#2- Remove an item from the list
if option == 2:
    remove_item = input('what is the item which you would like to remove?')
    studentFullName.remove(remove_item)
    print(studentFullName)

#3- Insert an item to the list
if option == 3:
    insert_index = int(input('Where do you want to insert the item?'))
    insert_value = input('Please enter the value for the item you want to insert:')
    studentFullName.insert(insert_index, insert_value)
    print(studentFullName)

#4- Find maximum
if option == 4:
    print('max is = ',max(studentFullName))

#5- Find Minimum
if option ==5:
    print(min(studentFullName))

#6- Sort the list in descending order
if option == 6:
    studentFullName.sort()
    print(studentFullName)

#7- Quit the program
if option == 7:
    exit()
