'''
10.2 - Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

# Solution: 
fname = input('Enter file name: ')

try: 
    fhand = open(fname, 'r')
except:
    print('Invalid file name')
    quit()

hour_dictionary = dict()
hr_list = list()

for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    t = words[5].split(':')
    hr_list.append(t[0])

print(hr_list)

for i in hr_list:
    hour_dictionary[i] = hour_dictionary.get(i, 0) + 1

tupl_list = list()
print(hour_dictionary)

'''
for k,v in hour_dictionary.items():
    tupl_list.append((k, v))
tupl_list = sorted(tupl_list)
'''

tupl_list = sorted( [ (k,v) for k,v in hour_dictionary.items() ] )
print(tupl_list)

for key,val in tupl_list:
    print(key, val)