'''
9.4 - Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

# Solution:
fname = input('Enter a file name: ')
try: 
    fileHandle = open(fname, 'r')
except:
    print("Please enter a valid file name!")
    quit()

counts_num = dict()
emails = list()
for line in fileHandle:
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    emails.append(email)

for email in emails:
    counts_num[email] = counts_num.get(email, 0) + 1

bigCount = None
bigWord = None
for word, count in counts_num.items():
    if bigCount is None or count > bigCount:
        bigCount = count
        bigWord = word
print(bigWord, bigCount)
    
    


