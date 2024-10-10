'''
8.4 - Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
'''

# My Solution:
fname = input('Enter file name: ')
paragraph = open(fname, 'r')
words = list()
for line in paragraph:
    x = line.split()
    for i in range(len(x)):
        if x[i] in words: continue
        words.append(x[i])
words.sort()
print(words)



