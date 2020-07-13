'''
Programmer: Mahrokh Ebrahimi

Description:
Running the Race using list and function
Write a program that asks for the names of three runners and the time it took each of them
to ﬁnish a race. The program should display who came in ﬁrst, second, and third place.
Think about how many test cases are needed to verify that your problem works correctly.
(That is, how many different ﬁnish orders are possible?)

Date: 7/10/2020
'''
name = []
time = []
for i in range(3):
    names = input('what is your name?')
    name.append(names)
    times = int(input('how long does it take for you to finish the race?'))
    time.append(times)

print(name, time)
if (time[1] < time[2]):
    if (time[1] < time[3]):
        print(name[1])
