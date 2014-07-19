## Assignment 7.1 
## Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in 
## upper case. You can download the sample data at http://www.pythonlearn.com/code/words.txt

fname = raw_input("Enter file name: ")
fh = open(fname)
for lines in fh:
    lines = lines.upper()
    lines = lines.rstrip()
    print lines


## Assignment 7.2 
## Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
## X-DSPAM-Confidence:    0.8475. Count these lines and extract the floating point values from each of the lines and compute the average 
## of those values and produce an output as shown below. You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt.

fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count + 1
    text = line;
    pos = text.find(':')
    num = float(text[pos+1:])
    sum = sum + num
print "Average spam confidence:", sum / count



## Assignment 8.4 
## Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the 
## split() function. The program should build a list of words. For each word on each line check to see if the word is 
## already in the list and if not append it to the list. When the program completes, sort and print the resulting words 
## in alphabetical order. You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word not in lst:
            wd = word
            lst.append(wd)
    
lst.sort()
print lst


## Assignment 8.5 
## Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
## From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
## You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
## Then print out a count at the end.
## You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt


fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if line == '' : continue
    words = line.split()
    if words[0] != 'From': continue
    print words[1]
    count = count + 1
print "There were", count, "lines in the file with From as the first word"