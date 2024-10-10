'''
Video: 9.1
Topic: Dictionaries
'''

'''
• Dictionaries in Python are Key:Value pair.

• Dictionaries are Python’s most powerful data collection.

• Dictionaries allow us to do fast database-like operations in Python
'''

cabinet = dict()
cabinet['summer'] = 12
cabinet['fall'] = 3
cabinet['spring'] = 75
print(cabinet) # Output: {'summer': 12, 'fall': 3, 'spring': 75}

print(cabinet['fall']) # Output: 3

cabinet['spring'] = cabinet['spring'] + 5
print(cabinet) # Output: {'summer': 12, 'fall': 3, 'spring': 80}

'''
Video: 9.2
Topic: Counting with Dictionaries
'''

'''
$ Counting with dictionaries:
-----------------------------
• One common use of dictionaries is counting how often we “see” something.
'''
# Exercise: Count the elements in a list by using a dictionary

# Solution (The OLD Way):
count = dict()
names1 = ['cwen', 'csev', 'ars', 'sdks', 'cwen', 'ars', 'csev', 'sdks', 'cwen', 'ars']

for name in names1:
    if not name in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1

print(count) # Output: {'cwen': 3, 'csev': 2, 'ars': 3, 'sdks': 2}

'''
$ The get() Method for Dictionaries:
------------------------------------
* The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called get() that does this for us. 

Typically -> 
if name in counts:
    x = counts[name]
else:
    x = 0

And ->
x = counts.get(name, 0) 

* Explanation: Every dictionary has this get() method, and it takes two parameters. One is the key you're looking for, and the second one is what we call the default value if the key is not present but if the key is present then it is going to have its old value.

So, x is either going to be zero or whatever the old value is under the key name.

{'cwen': 3, 'csev': 2, 'ars': 3, 'sdks': 2}

'''
# Solution (Using the get() Method for Dictionaries):
count_list = dict()
names1 = ['cwen', 'csev', 'ars', 'sdks', 'cwen', 'ars', 'csev', 'sdks', 'cwen', 'ars']
for name in names1:
    count_list[name] = count_list.get(name, 0) + 1
    '''
    Explanation: we're going to say count_name = counts.get(name, 0). That says, if it's not there, that part of the right-hand side expression is going to be 0 and then we're adding 1 to it. This solves both the case of the first time we see a name and then later times that we see a name.

    In a nutshell, We can use get() and provide a default value of zero when the key is not yet in the dictionary - and then just add one
    '''
print(count_list) # Output: {'cwen': 3, 'csev': 2, 'ars': 3, 'sdks': 2}

'''
Video: 9.3
Topic: Dictionaries and Files
'''
word_count = dict()
line = input("Enter a paragraph: ")

words = line.split()
print('Words: ', words)

print('Counting...')

for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print('Counts: ', word_count)

'''
Output:
------- 
Enter a paragraph: the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car

Words:  ['the', 'clown', 'ran', 'after', 'the', 'car', 'and', 'the', 'car', 'ran', 'into', 'the', 'tent', 'and', 'the', 'tent', 'fell', 'down', 'on', 'the', 'clown', 'and', 'the', 'car']

Counting...

Counts:  {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 'tent': 2, 'fell': 1, 'down': 1, 'on': 1}
'''


'''
$ Definite Loops and Dictionaries:
---------------------------------
* We've been looping through lists, but eventually, we need to loop through dictionaries.
'''
counts = {
    'ars': 24,
    'sks': 21,
    'twp': 34 
}
for key in counts:
    print(key, counts[key])

'''
Output: 
ars 24
sks 21
twp 34    
'''

'''
$ Retrieving lists of Keys and Values:
--------------------------------------
* You can get a list of keys, values, or items (both)from a dictionary.
'''
jjj = {
    'chuck' : 1,
    'fred' : 42,
    'jun' : 100
}

print(list(jjj)) # Output: ['chuck', 'fred', 'jun']

print(list(jjj.keys())) # Output: ['chuck', 'fred', 'jun']

print(list(jjj.values())) # Output: [1, 42, 100]

print(list(jjj.items())) # Output: [('chuck', 1), ('fred', 42), ('jun', 100)] -> This is a tuple.

'''
$ Bonus: Two Iteration Variables! Pt. 1: (tuple)
------------------------------------------------
* We loop through the key-value pairs in a dictionary using *two* iteration variables.

* Each iteration, the first variable is the key and the second variable is the corresponding value for the key.
'''

ppp = {
    'jhuk' : 112,
    'dred' : 34,
    'apr' : 24
}

for aaa, bbb in ppp.items():
    print(aaa, bbb) 

'''
Output: 
jhuk 112
dred 34
apr 24
'''

# Exercise: Find the most common word in a text file and count how many times it had appeard

# Solution: 
fname = input('Enter file name: ')
fhand = open(fname, 'r')
count_dict = dict()

for line in fhand:
    words = line.split()
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1

bigCount = None
bigWord = None
for word, count in count_dict.items():
    if bigCount is None or count > bigCount:
        bigCount = count
        bigWord = word

print(bigWord, bigCount) 
# Output: Enter file name: words.txt -> to 16










