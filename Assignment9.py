# assignment 9.4.
# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program 
# creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Get and open a file
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname, 'r')

# This loop is searching for the parts of the text in which we are interested and puts it in the list 'lst'.
lst = list()
for line in fh:
    line = line.rstrip()
    if line == '' : continue
    words = line.split()
    if words[0] != 'From': continue
    wd = words[1]
    lst.append(wd)

# Counting the words in the list 'lst' and puts it in the dictionary 'counts'.
words = lst
counts = dict()
for word in words:
    counts[word]= counts.get(word,0)+1

# Now the programme is looking for the biggest count and word and print it at the end
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount