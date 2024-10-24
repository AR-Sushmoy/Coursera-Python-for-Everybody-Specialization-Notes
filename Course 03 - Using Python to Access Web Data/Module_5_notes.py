'''
Video: 13.1
Topic: Data on the Web
'''

'''
$ Sending Data Across the (NET):
--------------------------------

* Web Services:

   - We're going to talk about web services. And we've been talking about moving data using the request/response cycle and HTTP and urllib. Web services is adding a layer of formalism on top of that. Where we're just being a little more formal about how we do this and basically, at some point we'll just switch from it's moving data back and forth to these are APIs (Application Program Interfaces).

   - Let's assume that, we have two programs and they're going to communicate across the Internet. So we might have a Python program that's producing the data. Maybe it's reading a database, maybe it's reading a file. Who knows what it is. But inside it has a Python data structure, like a dictionary. And we want to send that data across the network. And so we have worked out, over the years, what we call the " Wire Protocol ", or how the data leaves one system, transits  through a network, and then enters another system. 
   
   - Now at the other end in the destination system, it's not always gonna be Python. It could be another program (For example: Java). And so, perhaps, our Python dictionary in this other system needs to be a Java HashMap. So, we can't say that we're going to send Python data across the network, and we can't say that we're going to send Java data across the network. We just have to send Data through the network on some format that we agree on. 
   
   - And so we have to argue about what the format is and say, okay we're going to do this, and this is XML, which is one of the wire formats. In the context of web services, the wire format or serialization format refers to the agreed-upon format in which data is sent and received between programs over the network. 

   - Okay we're going to take the data that's in a Python dictionary and we're going to convert it into XML. XML looks kind of like HTML and it has less thans (<) and greater thans (>) as tags.

   - So, XML is our wire format. It is an agreed on intermediate protocol that is just text. When two programs communicate with each other, they may be written in different programming languages and have different internal data structures. The wire format acts as an intermediate format that both programs can understand and use to exchange data.

        - Serialization: The process of converting the internal data structure (Python Dictionary) of a program into the wire format is called serialization. This involves transforming the data into a format that can be easily transmitted over the network, such as a string or a document. 

        - De-Serialization: Once the data is serialized and sent across the network, it needs to be converted back into the appropriate data structure in the receiving program (Like: Java). This process is called deserialization.

    - Two commonly used wire formats/serialization formats are XML and JSON: 

        - XML (Extensible Markup Language) is a more complex format that uses tags to define the structure of the data. It is often used for exchanging structured data between different systems.

        - JSON (JavaScript Object Notation) is a lighter-weight format that represents data as key-value pairs. It is commonly used for transmitting data between web applications and APIs.

    - In a nutshell, So you take your Python dictionary, you produce JSON. You send JSON across the network as a string or a document, and then you receive the document, and then you turn it into whatever it is it's going to be (Java HashMap) on that far side. So that's the basic idea of agreeing on data formats or wire formats. 

    - By agreeing on a common wire format, programs can effectively communicate and exchange data, regardless of the programming languages they are written in.
'''









'''
==============================00==========================
'''







'''
Video: 13.2
Topic: eXtensible Markup Language (XML)
'''

'''
This video was an introduction to XML. Re-watch the Slide for a refresher. 
'''










'''
==============================00==========================
'''








'''
Video: 13.3
Topic: XML Schema
'''

'''
XML Schema: A set of rules that defines the structure, content, and data types of XML documents, ensuring that the data exchanged between applications is valid and understood correctly.

    - XML schemas and validation, which are like rules for how data should be structured when two applications communicate.

    - Imagine you and a friend are playing a game where you have to send secret messages to each other. To avoid confusion, you both agree on a specific format for your messages—like always starting with "Hello," followed by your name, and then the message itself. This agreement is similar to an XML schema. It defines what the message should look like, ensuring that both of you understand it correctly. If one of you sends a message that doesn’t follow the agreed format, the other won’t understand it, just like how an application might "blow up" if it receives unexpected data.

    - In technical terms, validation is the process of checking if the data you send matches the rules set by the schema. If it does, great! If not, you know there’s a problem. This way, both applications can confidently exchange information without misunderstandings.

    - What is the purpose of XML Schema?
    Ans: To eshtablish a contract as to what is valid XML.

    - XML Schema is the notion that there is this syntax that's used to establish a contract so that you can resolve disagreements between cooperating applications. 

Re-watch the Video for a refresher.

'''





'''
==============================00==========================
'''







'''
Video: 13.4
Topic: Parsing XML
'''

import xml.etree.ElementTree as ET


'''
* later we'll be pulling XML, and Jason from the web, but for now we're going to put it in a triple-quoted string,
'''


data = '''<person>
 <name>Chuck</name>
 <phone type="intl">
 +1 734 303 4456
 </phone>
 <email hide="yes"/>
 </person>'''

tree = ET.fromstring(data)

print('Name:', tree.find('name').text)
print('Email:', tree.find('email').get('hide', None))

'''
Output: 
Name: Chuck
Email: yes
'''

input = '''<stuff>
 <users>
    <user x="2">
        <id>001</id>
        <name>Chuck</name>
    </user>
    <user x="7">
        <id>009</id>
        <name>Brent</name>
    </user>
 </users>
 </stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')

print(lst) 
# Output: [<Element 'user' at 0x000002D53E2F4950>, <Element 'user' at 0x000002D53E2F4A40>]

print('User Count:', len(lst))

'''
Output: 
User Count: 2
'''

for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attribute:', item.get('x', None))

'''
Output: 
Name: Chuck
ID: 001
Attribute: 2
Name: Brent
ID: 009
Attribute: 7
'''