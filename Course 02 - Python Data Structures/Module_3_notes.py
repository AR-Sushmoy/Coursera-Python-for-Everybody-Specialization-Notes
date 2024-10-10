'''
Video: 7.1
Topic: Files
'''

'''
 And so everything we've done up to now has either been to the keyboard and the screen, or just inside the computer. Because that's what we've been learning how to basically do things. But now we're going to do things to something, and that is to a file or to something that is stored outside of the CPU and inside of the Secondary memory.
'''

'''
So, we have these files and the files we're going to play with initially are called flat text files. They are files that consist of lines. And the file we're going to play with is called mbox.txt or mboxshort.txt. This turns out to be a standard format called a mailbox format.
'''

'''
These flat text files, meaning that they're not like a word processing document, or a PDF, or something like that, they're just a set of lines that a program can read.
'''


'''
# Opening a File:-
------------------
• Before we can read the contents of the file (flat text file), we must tell Python which file we are going to work with and what we will be doing with the file.

• This is done with the 'open()' function.

• 'open()' returns a "file handle" - a variable used to perform operations on the file.

• In a nutshell, before we can work with a file inside Python, we want to tell Python that we're going to work with that file. 

• This is an act we call opening. 

• It's not actually reading the file. It's just making the file available to the code that we're going to write.
'''

'''
# using open():-
----------------
• Syntax -> handle = open(filename, mode)
for example: fhand = open('mbox.txt', 'r')

• open() function returns a handle that we use to manipulate the file.

• file name is a string i.e, -> 'mbox.txt'

• mode is optional and should be,
    'r' if we are planning to read the file,  
    'w' if we are going to write to the file, and 
    By default it is 'r' meaning read.
'''

# What is a Handle?:- 
'''
So, handle is something that's sort of a porthole between your program and the text file that's sitting on the disk. And we can open it, we can read from it, we can write to it if we want. And then we can close the handle and the handle goes away but the "handle is like our connection".
'''

'''
fhand = open('mbox.txt', 'r')
print(fhand)
# Output: <_io.TextIOWrapper name='mbox.txt' mode='r' encoding='cp1252'>
'''

'''
As we can see it is not the actual lines. It says this is a file, and it's a thing. And that's what its name is, we're reading it. And as we interpret the data coming out of the file, we're going to use the 'cp1252' character set to do that. So it's telling us something but it is not the actual file. There could be hundreds of thousands of lines of data in that file.
'''

# ----------------------------------------------------- # ------------------------------------------------------
# ----------------------------------------------------- # ------------------------------------------------------
# ----------------------------------------------------- # ------------------------------------------------------


'''
Video: 7.2
Topic: Processing Files
'''

'''
$ File Handle as a Sequence:
----------------------------
• A text file can be thought of as a sequence of lines

xfile = open('mbox.txt', 'r')
for line in xfile:
    print(line)

# Output: Prints every line inside the 'mbox.txt' file
'''

'''
• A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence.

• We can use the 'for' statement to iterate through a sequence.

• Remember - a sequence is an ordered set.

• In a nutshell, a file handle open for read can be treated as a sequence of lines, and allows us to iterate through it automatically using the for loop. 
'''

'''
$ Counting Lines in a File:-
----------------------------

fhand = open('mbox.txt', 'r')
count = 0
for line in fhand:
    count = count + 1
print(f'Line Count: {count}')

# Output: Line Count: 132045
'''

'''
$ Reading the *Whole* File:-
-------------------------------
• Sometimes often when reading data from elsewhere, we want to read it all. And so this time, we will read the whole thing in with ".read()"

• ".read()" does not split it into lines.

• It actually just reads all the stuff with a newline. 

• But of course, if you print it out, it will give you all the newlines because the print will show the newlines. But you have to realize you've got the whole as one big blob of characters punctuated by newlines.

• In a Nutshell, We can read the whole file (newlines and all) into a single string. 
'''

'''
thand = open('mbox-short.txt', 'r') 
# -> handle open for read can be treated as a sequence of strings.
inp = thand.read() 
# -> Reads the entire file into the variable inp as a string.
print(len(inp)) # Output: 94626
'''

'''
In this case, we're reading mbox-short.txt, read the whole thing into a string (i.e, thand.read()).

So that takes all of that file, whatever is on that file and takes the characters and sticks them in.

Then, we can say how many things did we get? Well, we got 94626 characters in this case.
'''

'''
$ Searching through a File:-
----------------------------
• We can put an if statement in our for loop to only print lines that meet some criteria.

shand = open('mbox-short.txt', 'r') # -> handle open for read can be treated as a sequence of strings.
for line in shand:
    if line.startswith('From: '):
        print(line) 
'''
'''
# Output: 

From: stephen.marquard@uct.ac.za

From: louis@media.berkeley.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

From: cwen@iupui.edu and so on ...
'''


'''
Now, if you run this code, you're going to see that it prints out the first From line, the second From line, but the question is, something is wrong. We're seeing lots of blank lines.

Well, it turns out that the print statement or the print() function, adds a newline.

That's how we end up with blank lines. The text from the file already has newline at the end of each line and then the print statement did once more and so then we ended up with new blank lines shown above.


Question: How do we deal with this?

Answer: Well, we have a function, a function we talked about in the last lecture, called rstrip, which strips off whitespaces, newlines are part of whitespaces because you don't see them.

** rstrips() - Removes whitespace (or specified characters) from the end (right side) of a string. **
'''

'''
shand = open('mbox-short.txt', 'r')
for line in shand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line) 
'''
'''
Output: 
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: zqian@umich.edu and so on ...
'''

'''
$ Skiping with 'continue':
--------------------------
• We can convenienty skip through a file using the 'continue' statement.
'''
'''
fhand = open('mbox-short.txt', 'r')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From: '):
        continue
    print(line)
'''
'''
Output: 
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: zqian@umich.edu and so on ...

Here, we are getting the same output.
'''

'''
$ Using 'in' to Select Lines:
-----------------------------
• We can look for a string anywhere in a line as our selection criteria. 
'''
'''
fhand = open('mbox-short.txt', 'r')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
'''
'''
Output: 
-------
From david.horwitz@uct.ac.za Fri Jan  4 04:33:44 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f 
and so on ...
'''

# Exercise: Prompt to the user for a file name and then count the number of "subject:" lines.
'''
fname = input('Enter the name of the file: ') 
fhand = open(fname, 'r')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
'''
'''
Output 01:
Enter the name of the file: mbox.txt
There were 1797 subject lines in mbox.txt

Output 02:
Enter the name of the file: mbox-short.txt
There were 27 subject lines in mbox-short.txt
'''

# Dealing with bad file name ->
fname = input('Enter file name: ')

try:
    fhand = open(fname, 'r')
except:
    print('File can not be opend: ', fname)
    quit()

count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

'''
Output:
Enter the name of the file: abc.txt
File can not be opend: abc.txt
'''