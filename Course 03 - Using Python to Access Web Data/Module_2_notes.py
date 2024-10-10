import re

'''
Video: 11.1
Topic: Regular Expressions
'''

'''
* Regular expression is a form of a language, and meaning it's a way to say that a set of strings match or don't match a regular expression.

* And from the 1960s to today, lots of operating systems have used regular expressions as a more intelligent form of search. So it's like, look for this expression, but it's not just like, hello, it's like h, followed by one letter, followed by ll, followed by a vowel, or something like that.

* It ends up being a programming language, but it's not like an iteration programming language, it's a programming language that's like match, match, match, match, question mark, question mark, question mark.

* So if you think about you search through stuff all the time, we just search through documents, we search through emails, we search through things, it just is a really, really smart way to look through lots of text. And they're powerful and cryptic.

* It's a programming language for string matching.
'''

'''
* The key to regular expressions is that instead of programming with lines, you're programming actually with characters.
'''

'''
$ Regular Expression Quick Guide:
---------------------------------
Python Regular Expression Quick Guide ->

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character (except a newline)
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
'''

'''
$ The Regular Expression Module:
--------------------------------
• So inside Python, regular expressions are not built into the base language, like strings or lists or dictionaries.

• Before you can use regular expressions in your program, you must import the library using "import re"

• You can use re.search() to see if a string matces a regular expression, similar to using the find() method for strings.

• You can use re.findall() to extract portions of a string that match your regular expression, similar to a combination of find() and slicing: var[5:10]
'''

'''
$ Using re.search() like find():
-------------------------------
'''

fhand = open('mbox-short.txt', 'r')

'''
for line in fhand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
'''

# After using Regex library
# import re -> already imported it at line 01
hand = open('mbox-short.txt', 'r')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
            print(line)

'''
Output: 
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: gsilver@umich.edu
From: gsilver@umich.edu
From: zqian@umich.edu
From: gsilver@umich.edu
From: wagnermr@iupui.edu
From: zqian@umich.edu
From: antranig@caret.cam.ac.uk
From: gopal.ramasammycook@gmail.com
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: louis@media.berkeley.edu and so on ....

• Explanation: we have to pass in the line that we're searching within and then the string 'From:' that we're searching for.
'''

'''
$ Using re.search() like startswith():
--------------------------------------
'''

'''
 for line in fhand:
       line = line.rstrip()
       if line.startswith('From:'):
             print(line)
'''

for line in fhand:
      line = line.rstrip()
      if re.search('^From:', line):
            print(line)

'''
Output: 
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: gsilver@umich.edu
From: gsilver@umich.edu
From: zqian@umich.edu
From: gsilver@umich.edu
From: wagnermr@iupui.edu
From: zqian@umich.edu
From: antranig@caret.cam.ac.uk
From: gopal.ramasammycook@gmail.com and so on ....

Explanation: So, we can also use search like the startswith function, and previously we're using find(). And now we're going to use startswith(). And so we say oh, it's this prefix, does it match a prefix, because that's what startswith does for strings. 

And so this code is pretty straightforward. We know how this works. And if starts with from, we're going to print it, otherwise, we're going to skip it. 

To do that with regular expressions, it's a little different. 

In regular expressions, what we do is we tweak the matching string, so the only thing we do to indicate that we want this search to match the beginning of the line, is we add a special character '^', we add this caret character '^'.

And that caret character '^' is not really a caret. What it says is, I want the F to be the first character of the line, so caret '^F' means F at the beginning of the line. So that's a way of matching, not 'From:' anywhere in the line. 

So this returns a true, if the 'From:' is at the beginning of the line, 
and a false, if there is no 'From:' at the beginning of the line. 

'From:' can be somewhere else in the line, you'll still get a false, right?
'''

'''
$ Wild-Card Characters:
-----------------------
For Example: ^X.*:

• Explanation: Let’s break it down step by step:

1) '^' This symbol is called a caret. In regular expressions, it signifies the start of a line. So, '^' means that whatever follows must be at the beginning of the line.

2) X This is just the character X. The regular expression is looking for lines that start with the character X.

3) .*: This part is a bit more complex:

    • The . (dot) matches any single character except a newline.

    • The * (asterisk) means repeating zero or more times of the preceding element (in this case, any character cuz we used . (dot)). So, '.*' together means any sequence of characters (including an empty sequence or whitespaces).

4) : This is just the colon character. The regular expression is looking for a colon : to appear after any sequence of characters.

Putting it all together, ^X.*: matches any line that:

• Starts with the character X
• Followed by any sequence of characters (including whitespace)
• And has a colon : somewhere after the X

For example, it would match lines like:
X-Sieve: CMU Sieve 2.3
X-DSPAM-Result: Innocent
X-DSPAM-Confidence: 0.8475
X-Content-Type-Message-Body: text/plain
'''

'''
$ Fine-Tuning Your Match:
-------------------------
• Depending on how clean your data is and the pupose of your application, you may want to narrow your match down a bit.

For example: You want to match lines like,
X-Sieve: CMU Sieve 2.3
X-DSPAM-Result: Innocent

But, want to skip lines like this,
X-Plane is behind schedule: two weeks


Inorder to do that, we can use,
^X-\S+:

• Explanation: ^X-\S+:  -> This regular expression refers to line that starts with X-, greater than or equal to one (>= 1) non-blank character, followed by a colon.

• \S matches any non-whitespace characters.

• + repeates any character one or more times. 
'''






'''
===========================00==========================
'''







'''
Video: 11.2
Topic: Extracting Data
'''

'''
• Up to now, we've just been playing with the search which gives us back a true or a false depending on whether it matches or not. But now we're going to actually pull stuff out. 

• So, now we're going to talk about extracting data.
'''

'''
$ Matching and Extracting Data:
-------------------------------
• Previously, We used re.search() that returns a True/False depending on whether the string matches the regular expression.

• Now, If we want the matching strings to be extracted, we use re.findall().

• When we use re.findall(), it returns a list of zero or more sub-strings that match the regular expression.
'''

x = 'My 2 favorite numbers are 8 and 23'
y = re.findall('[0-9]+', x)
print(y) # Output: ['2', '8', '23']
z = re.findall('[aeiou]+', x)
print(z) # Ouput: ['a', 'o', 'i', 'e', 'u', 'e', 'a', 'e', 'a']
t = re.findall('[AEIOU]+', x)
print(t) # Ouput: []
'''
• Explanation: Here '[0-9]+' -> means One or more digits.

The square bracket indicates that it is one character. So, that -> '[0-9]' is describing in between the square brackets what we mean by a single character?

We can have a range in here like '[0-9]' or '[a-z]'. We can have a list of things like '[aeiou]' would be vowels. 

'[0-9]' -> Zero through nine is digit. So, bracket zero dash nine bracket closed is a single digit. 

But then, we added a plus to it '[0-9]+' and that says one or more digits basically that means there is gotta be more than one. Now, if we put a star that will be zero or more digits which is kind of silly. 

Now we're going to use a function in the regular expression library called findall(). 

So, y = re.findall('[0-9]+', x) -> what we're saying here is, this is the string we're looking through, x, and we're looking for the pattern, one or more digits. 

Then it's going to look through the sequence of charachters in the string and say, "Oh let me see, one or more digits." Oh! 2 looks good I like that one. Let's keep looking. then 8 is also good and let's keep looking and 23 is also good. 

It may find zero, it may find one, or it may find more than one. So, what it does is it runs all the way through the texts that you've asked it to look for, checking to see when '[0-9]+' this matches, and it gives us back a list of the matches. 

So, it extracts out the pieces. So, previously we did something similar but we used a split in a for loop, and checking to see if it's a number and a whole bunch of stuff but now becuse of regular expressions all rolled into one little line.

Because findall(), if it gives us nothing, will give us an empty list but in this case, it's given us three strings. Now they're not numbers, this is the string '2', this is the string '8', and that's the string '23'.
'''


'''
$ Warning: Greedy Matching
--------------------------
• The repeat characters (* and +) push outward <- -> in both directions (greedy) to match the largest possible string.
'''

text = 'From: Using the: character'
c = re.findall('^F.+:', text)
print(c) # Output: ['From: Using the:']


'''
$ Non-Greedy Matching
---------------------
'''

text = 'From: Using the: character'
c1 = re.findall('^F.+?:', text)
print(c1) # Output: ['From:']

'''
• So, now we have a three character sequence. To the '+' or the '*', we can add a question mark '?'. 

This '^F.+?:' -> says any character, one or more times, but don't be greedy. 

So, now it looks at it and says "Okay, I've got a beginning F, and I can stop at the first colon, or I can stop at the last colon, but I am not greedy." So, the Non-Greedy prefers the shortest.
'''

'''
$ Fine-Tuning String Extraction
-------------------------------
'''
text2 = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# For Example:
f = re.findall(r'\S+@\S+', text2)
print(f) # Output: ['stephen.marquard@uct.ac.za']

'''
• You can separately determine which portion of the match is to be extracted by using parentheses ().

• Parentheses are not part of the match - but they tell where to start and stop what string to extract.

Regarding the SyntaxWarning:
The warning SyntaxWarning: invalid escape sequence '\S' is shown because \S is an escape sequence in regex, but Python treats backslashes (\) as escape characters in strings too (e.g., \n for a newline).
To avoid this warning, you should use raw strings by adding an r in front of the string. This tells Python to treat the backslashes as literal characters rather than escape sequences in the string itself.
This will prevent Python from interpreting \S as an escape sequence, avoiding the warning.
'''
r = re.findall(r'^From (\S+@\S+)', text2)
print(r) # Output: ['stephen.marquard@uct.ac.za']


'''
$ Extracting a host name - using find method and string slicing [The Old way without using Regular Expressions]
'''

atpos = text2.find('@')
sppos = text2.find(' ', atpos)
host = text2[atpos+1:sppos]
print(host) # Output: uct.ac.za

'''
But we can do a similar thing with regular expressions with dual split.
'''

'''
$ The Double Split Pattern:
---------------------------
• So, With this approach we can get the same output with four lines of code. That's more elegent.
'''

words = text2.split()
emailAddress = words[1]
pieces = emailAddress.split('@')
print(pieces[1]) # Output: uct.ac.za


'''
$ The Regex Version:
--------------------
'''
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

mail = re.findall('@([^ ]*)', line)
print(mail) # Ouput: ['uct.ac.za']

'''
'@([^ ]*)' -> Look through the string until you find an at sign.
'''


'''
$ Even Cooler Regex Version:
----------------------------
'''

mail_address = re.findall('^From .*@([^ ]*)', line)
print(mail_address) # Ouput: ['uct.ac.za']

'''
Explanation: We can fine tune this by saying I want to start with from in the line, I want a space, but I want any number of characters up to an @, and then I want to begin extracting all the non-blank characters, and then end extracting. 
'''


'''
Exercise: Spam Confidence
'''
handle = open('mbox-short.txt', 'r')
numlist = list()
for line in handle:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print(numlist) # Output: [0.8475, 0.6178, 0.6961, 0.7565, 0.7626, 0.7556, 0.7002, 0.7615, 0.7601, 0.7605, 0.6959, 0.7606, 0.7559, 0.7605, 0.6932, 0.7558, 0.6526, 0.6948, 0.6528, 0.7002, 0.7554, 0.6956, 0.6959, 0.7556, 0.9846, 0.8509, 0.9907]
print('Maximum: ', max(numlist)) # Output: Maximum:  0.9907

'''
Explanation: We're going to look for lines says X-DSPAM-Confidence: space, and then a floating point number. 

So, we'll open the data, we'll read through the lines, we're going to strip the data, and now we're going to use, findall(), to look for lines that start with X-DSPAM-Confidence: followed by a blankspace, then start extracting, take zero to nine and period '.' 
    because we're looking for floating point numbers,
so, we want to get the period, bracket, one or more times, and that's what we're interested in end extraction. 
'''


'''
$ Escape Charater:
------------------
• If you want a special regular expression character to just behave normally (most of the time) you prefix it with '\'
'''

y = 'We just received $10.00 for books'
o = re.findall('\$[0-9.]+', y)
print(o[0]) # Output: $10.00


'''
Question: What does the "[0-9]+" match in a regular expression?
Ans: One or more digits
'''

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
mail = re.findall(r'\S+?@\S+', line)
print(mail)