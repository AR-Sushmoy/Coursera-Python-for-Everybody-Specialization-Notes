'''
Video: 12.1
Topic: Network Technology
'''
'''
$ Sockets in Python:
--------------------
• Python has built-in support for TCP Sockets.

• It like creating a connection line with another  device (i.e, server) for futher communications. 
'''

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))

'''
Explanation: 
• So, like always we have to first import something. So, we're going to import the socket library to say, "Hey, we're going to use this library." Like the regular expression, we said Import re, and then we create a socket.

• We say socket.socket. This syntax here, I don't want to explain it. Just type this, the way I tell you to. It's like it creates this endpoint that's inside your computer that's ready to connect out to the far end, but it's not yet connected. It's like a connection point that has not yet been connected and that's what this magic means. We're going to hook a thing across the internet and we're going to use a stream. A stream means it's a series of characters that just keep coming back. So, that's that second line.

• The actual connection happens when we say mysock.connect. So, this returns us an object and then we actually call the connect method in that object and we pass in two things. We passed the host we want to connect to, which is a domain name, and a port that we want to connect to. So, that makes the connection and that's all it takes to make a socket connection. 

• Now, that's not sending any data, that's like dialing the phone. So that's all it takes to make the connection that dials the phone in Python.
'''






'''
===========================00==========================
'''








'''
Video: 12.2
Topic: Hyper Text Transfer Protocol (HTTP)
'''


# How you open a socket, send a command, and then retrieve the data using python:
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# HTTP Request (GET)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

while True:
    data = mysock.recv(512) # 512 means we're going to receive upto 512 characters.
    if (len(data) < 1): break
    print(data.decode())

mysock.close()


'''
Output: 

HTTP/1.1 200 OK
Date: Mon, 14 Oct 2024 15:41:32 GMT
Server: Apache/2.4.52 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already s
ick and pale with grief
'''

'''
Explanation: 

First we're going to import the socket library and we're going to make a socket. Now, this doesn't actually make a connection, think of a socket as a file handle that It doesn’t have any data associated with it yet.

And then what we’re going to do is we’re going to reach out and connect that socket to a destination across the Internet with the domain name of data.pr4e.org. And the second parameter in this tuple, connect() is a function call with a single tuple as a parameter. And so tuple[0] sub zero is 'data.pr4e.org' and tuple[1] sub one is the 80, which says I want to talk to port 80.

So, the next thing we're going to talk about is once we've made the sockets, how we actually communicate to that far off application in Python.

Inside ta HTTP command we have to add this .encode(). And that's because there are strings inside of Python that are in unicode, and we have to send them out is what's called UTF-8. And encode converts from unicode internally to UTF-8.

And after we've made the connection, we're going to send these two things and then we're going to wait. And my sock is like a file handle at that point because its been opened and we've sent data.

We can use a while loop now. recv() is a method in the socket object. We're going to receive up to 512 characters. 

If we get no data, that means end of file or end of transmission, so we break out. 

Then if we did get data, we decode it. And .decode() does 

That's taking data from the outside world and interpreting what it means internally for us. We're going to decode it. This loop is going to run a bunch of times until it hits end of file and then we're going to close the socket, which tears all this stuff down because this actually takes up resources in your computer and the far ends computer as well. Mysock.close closes that and that's it.
'''