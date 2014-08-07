# assignment 10.2
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for 
# each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting 
# the string a second time using a colon. Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.


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
    wd = words[5]
    wd = wd[0:2]
    lst.append(wd)

# Count the 'words' and sort them by key
words = lst
counts = dict()
for word in words:
    counts[word]= counts.get(word,0)+1
sorted(counts.items())  

# Print the keys and the values
for key, val in sorted(counts.items()):
    print key, val