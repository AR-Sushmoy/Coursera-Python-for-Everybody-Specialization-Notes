'''
Assignment-11.1: We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_2043770.txt (There are 115 values and the sum ends with 747)
'''

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

'''
Output: 
Enter File Name: regex_sum_2043770.txt 
544747

Enter File Name: regex_sum_42.txt
445833
'''