## Assignment 1: 
##Write a program that uses a print statement to say 
##'hello world' as shown in 'Desired Output'.

print "hello world"


## Assignment 2.2: 
## Write a program that uses raw_input to prompt a user for their name 
## and then welcomes them. Note that raw_input will pop up a dialog box. 
## Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.

name = raw_input("Enter your name")
print "Hello", name


## Assignment 2.3:
## Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
## Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use 
## raw_input to read a string and float() to convert the string to a number. Do not worry about error checking 
## or bad user data.

hrs = raw_input("Enter Hours:")
hours = float(hrs)
rate = 2.75
pay = hours*rate
print pay


## Assignment 3.2:
## Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Pay the 
## hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours 
## and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string 
## and float() to convert the string to a number. Do not worry about error checking the user input - assume the user 
## types numbers properly. 

hrs = raw_input("Enter Hours:")
hours = float(hrs)
ra = raw_input("Enter Rate:")
rate = float(ra)
if hours <= 40:
    pay = rate * hours
if hours > 40:
    pay = rate * 40 + (rate * 1.5 * (hours - 40))
print pay


## Assignment 3.3:
## Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
## If the score is between 0.0 and 1.0, print a grade using the following table:
## Score Grade
## >= 0.9 A
## >= 0.8 B
## >= 0.7 C
## >= 0.6 D
## < 0.6 F
## If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. 

try:
    inp = raw_input("Enter your Score")
    score = float(inp)
    if score < 0.6:
        print "F"
    elif score >= 0.6:
        if score < 0.7:
            print "D"
        elif score < 0.8:
            print "C"
        elif score < 0.9:
            print "B"
        elif score >= 0.9:
            print "A"
except:
    print "Error, please enter your numeric Score" 