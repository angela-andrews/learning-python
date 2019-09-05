# Reading files (drill)
# importing the argv package from the sys module
# sys is a module that provides access to some objext used by the interpreter and to
# functions that interact with the interpreter (pydoc)
# argv is an array of arguments that are passed in on the command line
# argv[0] is the script path
from sys import argv
# this is telling python to unpack the arguments in argv 
# that will be passed in on the command line

# script is argv[0] filename is argv[1]
script, filename = argv

# open() is a function that opens a file. The filename var is
# passed into the  open function 

# It's being saved to a variable txt.
# 5 in drill (commented out argv above)
# filename = input('What is the name of the file? >>')
txt = open(filename)

# print() to return the filename param
print(f"Here's your file {filename}:")

# print() to take the opened file that in the txt var and
# send it to the read() method & prints to the screen
print(txt.read())
# close the file
txt.close()

print("Type the filename again:")

# the input function can prepend text to the blank line that 
# allows for user input
# that input is saved to a var

file_again = input('>>>')

# the input from the user that was saved to the file_again var is 
# being passes to the open function
# then saved to a var
txt_again = open(file_again) 

# read() method on the var will print the file to screen again
print(txt_again.read())