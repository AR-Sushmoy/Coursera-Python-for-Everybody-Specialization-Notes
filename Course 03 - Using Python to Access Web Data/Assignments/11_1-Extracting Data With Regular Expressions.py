import re
fname = input('Enter File Name: ')

try:
    fhand = open(fname, 'r')
except:
    print('Please Enter a Valid File Name!')
    quit()

numbers = list()
for line in fhand:
    line = line.rstrip()
    numlist = re.findall('[0-9]+', line)
    for num in numlist:
        numbers.append(int(num))
print(sum(numbers))
