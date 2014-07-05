## Assignment 4.6:
## Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
## Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the 
## computation of time-and-a-half in a function called computepay() and use the function to do the computation. 
## The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay 
## should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. 
## Do not worry about error checking the user input unless you want to - you can assume the user types 
## numbers properly. 

def computepay(h,r):
    if h <= 40:
        p = r * h
    else:
        p = r * 40 + (r * 1.5 * (h - 40))
    return p

hrs = raw_input("Enter Hours: ")
hours = float(hrs)
inp = raw_input("Enter Rate: ")
rate = float(inp)

p = computepay(hours, rate)
print p


## Assignment 5.2:
## Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 
## 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other 
## than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
## Enter the numbers from the book for problem 5.1 and Match the desired output as shown. 

largest = -1
smallest = None
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    # Check for empty line
    if len(inp) < 1 : break     
    
    try:
        num = int(inp)
    except:
        print "Invalid input"
        continue
    # find the smallest number
    if smallest is None :
        smallest = num
    elif num < smallest :
        smallest = num
    # find the largest number
    if num > largest :
        largest = num
	

print "Maximum is", largest
print "Minimum is", smallest



## Assignment 6.5:
## Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line 
## below. Convert the extracted value to a floating point number and print it out.


text = "X-DSPAM-Confidence:    0.8475";
firstpos = text.find('0')
secondpos = text.find('5')
number = text[firstpos:secondpos+1]
num = float(number)
print num

## another and shorter code for this would be

text = "X-DSPAM-Confidence:    0.8475";
numpos = text.find('0')
number = float(text[numpos:])
print number
