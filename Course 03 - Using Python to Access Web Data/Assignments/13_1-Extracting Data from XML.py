'''
Assignment-13.1: In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/xml3.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_2043774.xml (Sum ends with 82)



Sample Execution: 
$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...
'''

import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as et

url = input('Enter URL - ')

if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print(f'Retrieving {url}')
data_xml = urllib.request.urlopen(url).read()

print(f'Retrieved {len(data_xml)} characters')
tree = et.fromstring(data_xml)

lst = tree.findall('comments/comment')
num = list()
for item in lst:
    num.append(int(item.find('count').text))

print('Count:', len(lst))
print('Sum:', sum(num))