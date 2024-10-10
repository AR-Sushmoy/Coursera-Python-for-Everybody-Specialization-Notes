'''
7.2 - Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

Desired Output: Average spam confidence: 0.7507185185185187

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''

fname = input('Enter the file name: ')

try:
    fhand = open(fname, 'r')
except:
    print("File Can Not Be Found: ", fname)
    quit()

count = 0
add = 0.0
for line in fhand:
    # if not line.startswith('X-DSPAM-Confidence'):
    if not 'X-DSPAM-Confidence' in line:
        continue
    count = count + 1
    npos = line.find('0')
    val = float(line[npos: ])
    add = add + val
print(f"Average spam confidence: {add/count}")


