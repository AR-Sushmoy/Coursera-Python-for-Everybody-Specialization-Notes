'''
Assignment-12.3: In this assignment you will write a Python program that will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah

Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Rhienna.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: H
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL - ')
try:
    count = int(input('Enter The Number of repetitions - '))
    position = int(input('Position of the link - '))
except:
    print('Somthing\'s wrong with the value')
    quit()

current_url = url
print('Retrieving:', current_url)
for i in range(count):
    html_page = urllib.request.urlopen(current_url).read()
    soup = BeautifulSoup(html_page, 'html.parser')
    tags_list = soup('a')
    current_url = tags_list[position - 1].get('href', None)
    print('Retrieving:', current_url)

print('The answer to the assignment for this execution is:', tags_list[position - 1].contents[0])  


