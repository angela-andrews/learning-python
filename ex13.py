# import is the same as in JS. adds features and functionality to your script
# argv is the "argument variable". It holds the arguments you pass to your script on the
# command line
from sys import argv
# read the WYSS secion for how to run this
# you must run the script with the arguments passed on the command line
# example > python3.6 ex13.py first 2nd 3rd
# the error will read: valueerror: not enough values to unpack

# this line unpacks argv so it passes out what has been passed in on the cmd line
script, first, second, third = argv

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is:", third)