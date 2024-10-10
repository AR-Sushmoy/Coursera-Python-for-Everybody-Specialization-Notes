'''
Video: 8.1
Topic: Lists
'''

'''
$ Algorithms
-> A set of rules or steps used to solve a problem.

$ Data structures 
-> A particular way of organizing data in a computer.
'''

'''
$ Important Facts about Python lists:
-------------------------------------
* A list is a kind of collection also known as list object. 
Example: friends = ['Havier', 'Jack', 'josef']

* A collection allows us to put many values in a single "variable"

In short, a list is a collection, meaning that in a single variable we can have more than one thing.

* A list element can be any Python object - even another list. Example: arr = [1, 2, [3, 4], 5]

* A list can be emptly. Example: arr = []

* lists are "mutable" -> we can change an element of a list using the index operator. On the other hand, Strings are "immutable" - we cannot change the contents of a string. 
'''

'''
$ Using the Range function:
---------------------------
* The range function returns a list of numbers that range from zero to one less than the parameter.
'''
'''
print(range(4)) # Output: range(0, 4)
print(list(range(4))) # Output: [0, 1, 2, 3]

for i in range(0, 2):
    print('Hello World')
'''
'''
Output: 
Hello World
Hello World

Explanation: range(0, 2) means the loop will run twice. Think of it as the slice method in a string. Inside the range function the first argument is the starting point and the second argument is the limit but excluding that. so, the number before that.  
'''
'''
friends = ['Havier', 'Jack', 'josef']
print(len(friends)) # Output: 3
print(list(range(len(friends)))) # Output: [0, 1, 2]


# for friend in friends:
#     print("Happy new year: ", friend)

# A counted loop:-
for i in range(len(friends)):
    friend = friends[i]
    print("Happy new year: ", friend)
'''
'''
Output: 
Happy new year:  Havier
Happy new year:  Jack
Happy new year:  josef
'''

# ----------------------------------------------------- # ------------------------------------------------------
# ----------------------------------------------------- # ------------------------------------------------------
# ----------------------------------------------------- # ------------------------------------------------------

'''
Video: 8.2
Topic: Manipulating Lists
'''

'''
$ Concatenating Lists Using '+' :
---------------------------------
* We can create a new list by adding two existing lists together.

a = [1, 3, 5]
b = [2, 4, 6]
c = a + b # Adding a and b to make c does not hurt either a or b.
print(c) # Output: [1, 3, 5, 2, 4, 6]
'''

'''
$ Lists Can Be Sliced Using ':' :
---------------------------------
* Remember: Just like in strings, the second number is "up to but not including".

* It's very much like strings. Slicing of lists is like slicing of strings except that the list is slicing entire cells within the string. 

r = [9, 41, 12, 3, 76, 13]
print(r[1:3]) # Output: [41, 12]
print(r[:4]) # Output: [9, 41, 12, 3]
print(r[3:]) # Output: [3, 76, 13]
print(r[:]) # Output: [9, 41, 12, 3, 76, 13]
'''

'''
$ List Methods:
---------------
* z = list() -> We're calling this 'list()' Constructor and so list is a predefined type. So we say, make a brand new list, it's the same as saying, give me an empty list and then assign it to the variable z. So, this is a list with nothing in it.
'''
'''
x = list()
print(type(x)) # Output: <class 'list'>
print(dir(x)) # Output: ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort', and so on ...]
'''

'''
$ Building a List from Scratch:
-------------------------------
* We can create an empty list and then add elements using the 'append' method.

* The list stays in order and new elements are added at the end of the list.

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff) # Output: ['book', 99]
stuff.append('cookie')
print(stuff) # Output: ['book', 99, 'cookie']
'''

'''
Now, recall that strings are not mutable, so all these methods would not affect the original string. But lists are mutable, and so appending actually changes this variable 'stuff'. 

So, for example, you don't want to do something like -> stuff = stuff.append(2).

Because the return value that you get back here, actually messes the variable stuff up. So, you do not want to do that. You just say x.append and that works a lot better.
'''

'''
$ Is something in a List?:
--------------------------

some = [1, 9, 21, 10, 16]
print(9 in some) # Output: True
print(15 in some) # Output: False 
print(20 not in some) # Output: True
'''

'''
$ Lists are in Order:
---------------------
* A list can be sorted (i.e., change its order)

* The sort method (unlike in strings) means "sort yourself"

siblings = ['Joseph', 'Glenn', 'Sally']
siblings.sort()
print(siblings) # Output: ['Glenn', 'Joseph', 'Sally']
print(siblings[1]) # Output: Joseph ; Because lists are mutable. 
'''

'''
$ Built-in Functions and Lists:
-------------------------------
* There are a number of functions built into Python that take lists as parameters. 

* Remember the loops we built? These are much simpler.

nums = [3, 41, 12, 9, 74, 15]
print(len(nums)) # Output: 6
print(max(nums)) # Output: 74
print(min(nums)) # Output: 3
print(sum(nums)) # Output: 154
print(round((sum(nums)/len(nums)), 2)) # Output: 25.67
'''

'''
Exercise: Ask the user to enter numbers, when they type done tell them the average of the numbers that they've inputed.


# Solution 01: (The Old Way)
# --------------------------
total = 0
count = 0
while True:
    inp = input("Enter any number: ")
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print("Average:", average)

# Solution 02: (The New Way)
# --------------------------
num = list()
while True: 
    user_inp = input("Enter any number: ")
    if user_inp == 'done': break
    val = float(user_inp)
    num.append(val)
avg = round((sum(num)/len(num)),2)
print("Average:", avg)
'''

# ----------------------------------------------------- # ------------------------------------------------------
# ----------------------------------------------------- # ------------------------------------------------------
# ----------------------------------------------------- # ------------------------------------------------------

'''
Video: 8.3
Topic: Lists and Strings
'''

'''
$ Best Friends: Strings and Lists:
----------------------------------
* Split breaks a string into parts and produces a list of strings. We think of these as words. We can access a particular word or loop through all the words.

abc = 'With three words'
stuff = abc.split()
print(stuff) # Output: ['With', 'three', 'words']
print(len(stuff)) # Output: 3
print(stuff[1]) # Output: three

for i in stuff:
    print(i)
'''
'''
Output: 
With 
three
words
'''

'''
* When you do not specify a delimiter, multiple spaces are treated like one delimiter.

line = 'A lot           of spaces'
arr1 = line.split()
print(arr1) # Output: ['A', 'lot', 'of', 'spaces']
'''

'''
* You can specify what delimiter character to use in the splitting.

line1 = 'first;second;third'
arr2 = line1.split(';')
print(arr2) # Output: ['first', 'second', 'third']
print(len(arr2)) # Output: 3
'''

'''
# Exercise-01: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 -> print what day of the week this thing happened in.

# Solution:
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

'''
'''
Output: 
Sat
Fri
Fri
Fri
Fri ...
'''

'''
# Exercise-02: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 -> print the email address's last part.

# Solution:
sentence = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
word = sentence.split()
email = word[1]
pieces = email.split("@")
print(pieces[1]) # Output: uct.ac.za
'''













