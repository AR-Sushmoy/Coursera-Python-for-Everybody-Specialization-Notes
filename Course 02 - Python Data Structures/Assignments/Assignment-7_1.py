'''
7.1 - Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.

You can download the sample data at http://www.py4e.com/code3/words.txt
'''

fname = input("Enter The File Name: ")

try:
    fhand = open(fname, 'r')
except:
    print("file can not be found: ", fname)
    quit()

for line in fhand:
    line = line.rstrip()
    print(line.upper())