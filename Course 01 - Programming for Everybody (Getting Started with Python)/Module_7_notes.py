'''
Topic: Loop, Indifinite Loop, and Definite Loop
'''

'''
The idea behind loop is that you've done something, let's go do that thing again. 

And the way we express that in Python is with a couple of keywords. One of the keywords is the "while" keyword and the "for" keyword. 

And so we'll start talking about the "while" and these are called indefinite loops. And in a bit, we'll talk about definite loops using "for". 

indefinite loops, and that's the use of the "while" keyword that just runs until some logical condition is false or you hit a break. 

Definite loops are finite. definite loops are for lists or lines in a file or characters in a string, and, they iterate through members of a set.
'''

#Example of a indifinite loop (While loop):

# n = 5
# while n > 0:
#     print(n)
#     n = n - 1

# print("Blastoff!")
# print(n)

'''
Output:
5
4
3
2
1
Blastoff!
0
'''

'''
So, an important part of any loop is what we call the iteration variable, okay? And that is something that changes, because if we don't change anything in the loop, then it's going to run forever. That's what we call an infinite loop.
'''

'''
Now, we have some statements that we can use to get out of a loop. One of them is the "break" statement. And it's an executable statement. When it runs, it basically breaks out of the loop, moves to the line beyond the end of the loop.
'''
# For Example: 

# while True:
#     line = input("> ")
#     if line == "done":
#         break
#     print(line)
# print("Done!")

'''
Output:
> hello there
hello there
> finished
finished
> done
Done!
'''

'''
"Continue" basically says quit on the current iteration and go to the next iteration. So it skips out of the loop, but it doesn't skip to the line beyond it, it skips back up to the top. So continue says, oh, we're going to go up to the top. Break says get out and continue says don't do the rest of this iteration but go up and do the next iteration.
'''
# For Example: 
'''
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")
'''
'''
Output:
> hello there
hello there
> # finished
doesn't print finished
> print this!
print this!
> done
Done!
'''

'''
In a nutshell, 'break' skips out of the loop and 'continue' skips to the top of the loop. In other words, 'continue' abandons the current iteration and goes to the next iteration.
'''

# Exercise-1: Finding the largest value in a list
'''
largest_so_far = -1
print("Before", largest_so_far)
for i in [3, 6, 45, 31, 85, 4, 15, 90, 2, 1]:
    if i > largest_so_far:
        largest_so_far = i
        print(largest_so_far, i)
print("After", largest_so_far)
'''
'''
Output:
Before -1
3 3
6 6
45 45
85 85
90 90
After 90
'''

# Exercise-2: Counting in a loop

# zork = 0
# print('Before', zork)
# for thing in [9, 41, 12, 4, 65, 14]:
#     zork = zork + 1
#     print(zork, thing)
# print('After', zork)

'''
Output:
Before 0
1 9
2 41
3 12
4 4
5 65
6 14
After 6
'''

# Exercise-3: Summing up a series of values using loop

# zork = 0
# print('Before', zork)
# for thing in [9, 41, 12, 4, 65, 14]:
#     zork = zork + thing
#     print(zork, thing)
# print('After', zork)

'''
Output:
Before 0
9 9
50 41
62 12
66 4
131 65
145 14
After 145
'''

# Exercise-4: Finding the average in a loop

# num = [9, 41, 12, 4, 65, 14]
# sum = 0
# count = 0
# print('Before', count, sum)
# for thing in num:
#     sum = sum + thing
#     count = count + 1
#     print(count, sum, thing)
# avg = round((sum / count), 2)
# print('After', count, sum, avg)

'''
Output:
Before 0 0
1 9 9
2 50 41
3 62 12
4 66 4
5 131 65
6 145 14
After 6 145 24.17
'''

# Exercise-5: Filtering in a loop

# print("Before")
# for i in [2, 56, 14, 67, 98, 113]:
#     if i > 20:
#         print("Larger Number", i)
# print("After")

'''
Output:
Before
Larger Number 56
Larger Number 67
Larger Number 98
Larger Number 113
After
'''

# Exercise-6: Search using a boolean variable

# found = False
# print("Before", found)
# for thing in [43, 21, 5, 87, 4, 3, 12, 23]:
#     if thing == 3:
#         found = True
#         break
#     print(found, thing)
    
        
# print("After", found)

'''
Output:
Before False
False 43
False 21
False 5
False 87
False 4
After True
'''

# Exercise-7: Find the smallest value

# smallest is working as a flag variable in here

# We have yet another type of variable. There is a variable called None type, "None". It only has one constant in it. For reference, booleans have "True" and "False", integers have a whole bunch, and then floats have a whole bunch, and None types have one thing, "None". So, None is a value, that we can distinctly detect different than numbers.
'''
smallest = None 
print("Before")
for the_num in [43, 21, 5, 87, 4, 3, 12, 23]:
    
    if smallest is None: # Here we can ask, is the contents of smallest None? If smallest is None, here the word 'is', it's more powerful than double equal sign.
        smallest = the_num
    elif the_num < smallest:
        smallest = the_num
    print(smallest, the_num)
print("After", smallest)
'''
'''
Output:
Before
43 43
21 21
5 5
5 87
4 4
3 3
3 12
3 23
After 3
'''


# Another Solution: 
'''
x = [1, 2, 4, 5, 6, 9, 10, 0]
small_num = x[0]
print("Before ", small_num)
for n in x:
    if n < small_num:
        small_num = n
    print(small_num, n)
print("After ", small_num)
'''
'''
Output:
Before  1
1 1
1 2
1 4
1 5
1 6
1 9
1 10
0 0
After  0
'''


'''
Notes:
------
> Python has an "is" operator that can be used in logical expressions

> Implies "is the same as"

> Similar to, but stronger than, "=="

> "is not" also is a logical operator
'''


'''
Practice 1: Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers. If the user enters anything other than a integers, detect their mistake using try and except and print an error message and skip to the next integers. 
Link --> https://www.py4e.com/html3/05-iterations#:~:text=Exercises-,Exercise%201%3A,-Write%20a%20program

For Example >
---------------
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
'''
# Solution:
'''
count = 0
sum = 0.0

while True:
    sval = input("Enter a number: ")
    if sval == 'done' or sval == 'Done':
        break
    try:
        fval = float(sval)
    except:
        print("Invalid Input")
        continue
    
    count = count + 1
    sum = fval + sum

print(sum, count, sum/count)
'''

'''
Assignment 5.2: Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
'''


largest = None
smallest = None

while True:
    s_num = input("Enter a number: ")
    if s_num == "done" or s_num == "Done":
        break
    try:
        i_num = int(s_num)
    except:
        print("Invalid input")
        continue
    # condition for finding the smallest number
    if smallest is None:
        smallest = i_num
    elif i_num < smallest:
        smallest = i_num
    # condition for finding the largest number
    if largest is None:
        largest = i_num
    elif i_num > largest:
        largest = i_num


print(f"Maximum is {largest}")
print(f"Minimum is {smallest}")
