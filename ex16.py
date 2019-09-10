# Reading and Writing Files
#  commands to remember:
# close : close the file. 
# read : reads the content of the file. You can assign the result to a var
# readline : Reads just one line of text
# truncate : Empties the file. *watch out for this one*
# write('some string') : Writes the string in quotes to the file
# seek(0) : Move the read/write locatio to the beginning of the file

from sys import argv 

script, filename = argv

print(f"We're going to erase {filename}")
# ctrl+c is the universal 'get me outta here command'
print(f"If you don't want that to happen, hit ctrl+c")
print(f"If you do want to erase {filename}, hit return")

input('?')

print("Opening the file ....")
# the 'w' after the open means to open the file in write mode
target = open(filename, 'w')
print("Truncating the file, Goodbye!")
target.truncate()

print("Now, I'm going to ask you for 3 lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("....And finally, we close it.")
target.close()