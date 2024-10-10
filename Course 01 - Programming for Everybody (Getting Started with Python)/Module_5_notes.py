'''
Topic: Conditional Statements, Try and Except
'''

# Example of Try and Except
'''
value = input("Type any number in digits: ")

try:
    ival = int(value)
except:
    ival = -1

if ival >= 0:
    print("You typed =", value)
else:
    print("Not a digit!")
'''

'''
Assingment 3.1: Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
'''
# Solution: Time and a Half Calculations, With Examples --> Link: https://blog.bernieportal.com/time-and-a-half-calculations-with-examples
'''
hrs = float(input("Enter how many hours a day you work: "))
rph = float(input("Enter the hourly rate: "))

if hrs >= 0:
    if hrs > 40:
        extraHours = hrs - 40 
        bonusRate = rph * 1.5
        extraPay = extraHours * bonusRate
        grossPay = (40 * rph) + extraPay 
        print(grossPay)
    else:
        grossPay = hrs * rph
        print(grossPay)
else:
    print("Start working!")
'''

'''
Assignment 3.2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program.
'''
# Solution 01:-
'''
try:
    hrs = float(input("Enter how many hours a day you work: "))
    rph = float(input("Enter the hourly rate: "))
except:
    hrs = -1
    rph = -1
    
if hrs >= 0:
    if hrs > 40:
        extraHours = hrs - 40 
        bonusRate = rph * 1.5
        extraPay = extraHours * bonusRate
        grossPay = (40 * rph) + extraPay 
        print("Pay:", grossPay)
    else:
        grossPay = hrs * rph
        print("Pay:", grossPay)

else: 
    print("Error, please enter numeric input")
'''
# Solution 02:-
'''
try:
    hrs = float(input("Enter how many hours a day you work: "))
    rph = float(input("Enter the hourly rate: "))
except:
    print("Error, please enter numeric input")
    quit()
    
if hrs > 40:
    extraHours = hrs - 40 
    bonusRate = rph * 1.5
    extraPay = extraHours * bonusRate
    grossPay = (40 * rph) + extraPay 
    print("Pay:", grossPay)
else:
    grossPay = hrs * rph
    print("Pay:", grossPay)
'''

'''
Assingment 3.3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
'''
# Solution:-
'''
score = input("Enter score: ")

try:
    fScore = float(score)
except:
    fScore = -1

if 0 <= fScore <= 1.0:    

    if 0.9 <= fScore <= 1.0:
        print("A")
    elif 0.8 <= fScore < 0.9:
        print("B")
    elif 0.7 <= fScore < 0.8:
        print("C")
    elif 0.6 <= fScore < 0.7:
        print("D")
    else:
        print("F")
else:
    print("The score should be in the range between 0.0 - 1.0")
'''

