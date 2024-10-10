'''
Video: 10
Topic: Tuples
'''

'''
$ Tuples are like Lists:
------------------------
• Tuples are a limited version of lists, and the sum total of this is that, tuples are sort of a more efficient version of lists that you can't modify. So they're really unmodifiable lists.

• Tuples are another kind of sequence that functions much like a list - they have elements which are indexed starting at 0.

• Tuples are not changeable. They're immutable.
'''

x = ['Glenn', 'Sally', 'joseph']
print(x[2]) # Output: joseph

y = (1, 9, 3)
print(max(y)) # Output: 9

for i in y:
    print(i)
'''
# Output:
1
9
3 
'''

'''
$ Tuples Are More Efficient:
---------------------------
• Since Python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terms of memory use and performance than lists.

• So in our program when we are making “temporary variables” we prefer tuples over lists.
'''

'''
$ Tuples and Assignment:
------------------------
• We can also put a tuple on the left-hand side of an assignment statement.

• We can even omit the parentheses.
'''

(s, f) = (4, 'fred')
print(f) # Output: fred

(a, b) = (99, 98)
print(a) # Output: 99

'''
$ Tuples and Dictionaries:
--------------------------
• We have already seen that the items() method in dictionaries returns a list of (key, value) tuples.
'''
d = dict()
d['csev'] = 2
d['cwen'] = 4

for (k,v) in d.items():
    print(k,v)
'''
# Output:
csev 2
cwen 4
'''

tups = d.items()
print(tups) 
# Output: dict_items([('csev', 2), ('cwen', 4)])

'''
$ Tuples are Comparable:
--------------------------
• The comparison operators work with tuples and other sequences. If the first item is equal, Python goes on to the next element, and so on, until it finds elements that differ.
'''

print((0, 1, 2) < (5, 1, 2))
# Output: True
print((0, 1, 2000000) < (0, 3, 4))
# Output: True
print(('jones', 'sally') < ('jones', 'sam'))
# Output: True
print(('jones', 'sally') > ('Adams', 'sam'))
# Output: True

'''
$ Sorting Lists of Tuples:
--------------------------
• We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary.

• First we sort the dictionary by the key using the items() method and sorted() function.
'''

u = {
    'a': 10,
    'c': 22,
    'b': 1
}
print(sorted(u.items())) 
# Output: [('a', 10), ('b', 1), ('c', 22)]

for k,v in sorted(u.items()):
    print(k, v)
'''
# Output:
a 10
b 1
c 22
'''

'''
$ Sort by Values Instead of Key:
-------------------------------
• If we could construct a list of tuples of the form (value, key) we could sort by value.

• We do this with a for loop that creates a list of tuples.
'''

c = {
    'a': 10,
    'b': 1,
    'c': 22
}

tmp = list()
for k, v in c.items():
    tmp.append( (v, k) )
print(tmp)
# Output: [(10, 'a'), (1, 'b'), (22, 'c')]

tmp = sorted(tmp, reverse=True)
print(tmp)
# Output: [(22, 'c'), (10, 'a'), (1, 'b')]


'''
Exercise: Find the top 5 most common words from a text file.
'''
# Solution (The OG way):
fhand = open('romeo.txt', 'r')
rand_dictionary = dict()

for line in fhand:
    words = line.split()
    for word in words:
        rand_dictionary[word] = rand_dictionary.get(word, 0) + 1

# print(rand_dictionary)

temp_lst = list()
for key, val in rand_dictionary.items():
    tmp = (val, key)
    temp_lst.append(tmp)

# print(temp_lst)
temp_lst = sorted(temp_lst, reverse=True)
for val, key in temp_lst[ :5]:
    print(key, val)

'''
# Output: 
the 3
is 3
and 3
sun 2
yonder 1
'''

# Even Shorter Version (Using List comprehension):
c = {
    'a': 10,
    'b': 1,
    'c': 22
}

print(sorted( [ (v,k) for k,v in c.items() ], reverse=True ))
# output: [(22, 'c'), (10, 'a'), (1, 'b')]

# Solution (The succinct way):
file_handle = open('romeo.txt', 'r')
r = dict()
for line in file_handle:
    words = line.split()
    for word in words:
        r[word] = r.get(word, 0) + 1
print(r)

new_lst = sorted( [ (val, key) for key, val in r.items() ], reverse=True )

for v, k in new_lst[:5]:
    print(k, v)
'''
# Output:
the 3
is 3
and 3
sun 2
yonder 1
'''

'''
Explanation: List comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.
'''

# Another way of sorting a list:
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days.sort(reverse=True)
print(days) 
# Output: ['Wed', 'Tue', 'Thu', 'Sun', 'Sat', 'Mon', 'Fri']























