'''
Video: 6.1
Topic: Strings
'''

# Looping inside strings 
fruit = "banana"
letter = fruit[3]
print(letter) # Output: a

x = 3
w = fruit[x-1]
print(w) # Output: n

# Len Function
car = "porchse"
y = len(car)
print(y) # Output: 7

# Looping through strings
'''
Using a while statement and an iteration variable, and the 'len()' function, we can construct a loop to look at each of the letters in a string individually.
'''

# Using a Indeterminate loop
component = "motherboard"
index = 0
while index < len(component):
    x = component[index]
    print(index, x)
    index = index + 1
'''
Output: 
0 m
1 o
2 t
3 h
4 e
5 r
6 b
7 o
8 a
9 r
10 d
'''

'''
Now, unless you actually need to know the position, just if you want to go through all the letters in a loop, a much more convenient thing to do is just use a 'for' loop – a determinate loop.
'''

'''
A determinate loop using a for statement is much more elegant.
'''

'''
The iteration variable is completely taken care of by the for loop.
'''

# Using a Determinate loop
salad = 'chia seed salad'
for x in salad:
    print(x) 

'''
Output:
c
h
i
a

s
e
e
d

s
a
l
a
d
'''
'''
$ Looping and counting using Determinate loop:
----------------------------------------------

food = "biriyani"
count = 0
for letter in food:
    if letter == "i":
        count = count + 1
print(f'\n{count}') # Output: 3
'''

'''
# Slicing Strings:
------------------
s = 'hey, my name is sushmoy'
print(s[16: ]) # sushmoy
print(s[0:3]) # hey
print(s[8:12]) # name
'''

'''
$ Using 'in' as a logical operator:
-----------------------------------
* The 'in' keyword can also be used to check to see if one string is "in" another string.

* The 'in' expression is a logical expression that returns True or False and can be used in an if statement.
'''

'''
Example:
--------
>>> fruit = 'banana'
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> 'nan' in fruit
True
>>> if 'a' in fruit:
        print("Found it!")

Found it!
'''

'''
$  Searching a String:
---------------------
* We use the 'find()' function to search for a substring within another string. 

* 'find()' function finds the first occurence of the substring.

* If the substring is not found, 'find()' returns -1
'''

file_name = 'manipulating strings'
position = file_name.find('string')
print(position) # 13

z = file_name.find('abc')
print(z) # -1

'''
$ Search and Replace:
---------------------
* The 'replace()' function is like a "search and replace" operation in a word processor.

* It replaces all occurrences of the search string with the replacement string.
'''

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr) # Hello Jane

nstr = greet.replace('o', 'x')
print(nstr) # Hellx Bxb

'''
$ Stripping Whitespace:
-----------------------
• lstrip()and rstrip()remove whitespace at the left or right

• strip() removes both beginning and ending whitespace
'''
word = "   Hello, World!    "
print(word.strip()) # Output: Hello, World!
print(word.lstrip()) # Output: Hello, World!    
print(word.rstrip()) # Output:    Hello, World!


'''
$ Prefixes:
----------
A real common problem to be scanning through a file and want to know only the lines that start with a prefix. And there is a built-in method called 'startswith()'
'''

line = 'Please have a nice day'
print(line.startswith('Please')) # True
print(line.startswith('x')) # False

'''
$ Parsing and Extracting:
-------------------------
'''
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:15 2008'

atpos = data.find('@')
print(atpos) # Output: 21

sppos = data.find(' ', atpos) # in 'find()' you can put up a second argument, and say that's where to start. for this line it means, find the blank space but start searching from the position 21.
print(sppos) # Output: 31

host = data[atpos+1 : sppos]
print(host) # Output: uct.ac.za

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3]) # Output: .ma