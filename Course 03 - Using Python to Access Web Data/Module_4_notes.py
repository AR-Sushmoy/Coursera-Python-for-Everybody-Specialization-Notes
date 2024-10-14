'''
Video: 12.3
Topic: Unicode Characters and Strings
'''

'''
Please Watch the video for detailed explanation on ASCII code, Unicode (UTF-16, UTF-32, and UTF-8).
'''




'''
==============================00==========================
'''






'''
Video: 12.4
Topic: Retrieving Web Pages
'''

'''
$ Making HTTP (even) Easier with urllib in Python:
--------------------------------------------------
• Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file.

• So there's a library that wraps that socket stuff and does it for us automatically, called urllib.
'''

# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

'''
Output:
------- 
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
'''

'''
• Now you'll notice the headers aren't here and it just shows you the data. So you'd know that there were headers, then turns out URL open eats them and remembers them, and you can actually ask for them later. You can say, "hey, give me the headers" if you want, but most of the time you're not interested in the headers. It just skips down to the data.

• So that's I think really and truly amazingly beautiful and simple, to take this whole internet architecture and HTTP and all that stuff, and roll it into one import statement (urllib) and three lines of code.
'''


# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()
# for line in fhand:
#     line = line.strip()
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

'''
Output: 
-------
{'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'It': 1, 'is': 3, 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2, 'Arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'Who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}
'''


'''
$ Reading Web Pages:
--------------------
'''

# handle = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

# for line in handle:
#     print(line.decode().rstrip())

'''
Output: 
-------
<h1>The First Page</h1>
<p>
If you like, you can switch to the
<a href="http://www.dr-chuck.com/page2.htm">
Second Page</a>.
</p>
'''







'''
==============================00==========================
'''







'''
Video: 12.5
Topic: Parsing Web Pages
'''


'''
$ Parsing HTML (a.k.a Web Scraping):
------------------------------------
• So up next we're going to talk about how we can more efficiently take apart the HTML and look for various things and print those things out.
'''

'''
$ What is Web Scraping?
----------------------
• One of the common uses of the urllib capability in Python is to scrape the web. Web scraping is when we write a program or script that pretends to be a web browser and retrieves web pages, then examines the data in those pages looking for patterns, and then looks at more web pages. 

• As an example, a search engine such as Google will look at the source of one web page and extract the links to other pages and retrieve those pages, extracting links, and so on. Using this technique, Google spiders its way through nearly all of the pages on the web.

• Search engines scrape web pages - we call this “spidering the web” or “web crawling”.

• Google also uses the frequency of links from pages it finds to a particular page as one measure of how “important” a page is and how high the page should appear in its search results.
'''


'''
$ Parsing HTML using BeautifulSoup:
-----------------------------------
• Regular expressions work very nicely when your HTML is well formatted and predictable. But since there are a lot of “broken” HTML pages out there, a solution only using regular expressions might either miss some valid links or end up with bad data.

• This can be solved by using a robust HTML parsing library.
'''


'''
$ BeatifulSoup Installation:
----------------------------
# To run this, you can install BeautifulSoup
https://pypi.python.org/pypi/beautifulsoup4

# Or download the file (Preferable)
http://www.py4e.com/code3/bs4.zip
and unzip it in the same directory as the Python file
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
handle = urllib.request.urlopen(url)

for line in handle:
    print(line.decode().strip())

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

print(tags) # [<a href="http://www.dr-chuck.com/page2.htm">Second Page</a>]

for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0].strip())
    print('Attrs:', tag.attrs)

'''
Output:
Enter - http://www.dr-chuck.com/page1.htm

<h1>The First Page</h1>
<p>
If you like, you can switch to the
<a href="http://www.dr-chuck.com/page2.htm">
Second Page</a>.
</p>

TAG: <a href="http://www.dr-chuck.com/page2.htm">
Second Page</a>
URL: http://www.dr-chuck.com/page2.htm
Contents: Second Page
Attrs: {'href': 'http://www.dr-chuck.com/page2.htm'}
'''
