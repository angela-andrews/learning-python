# ex 16 study drill

# similar script to #16 that uses the text file
from sys import argv
script, filename = argv

print(f"Let's erase the file you just wrote in the last program.")
print(f"If you don't want that to happen, hit ctrl+c")
print(f"If you do want to erase {filename}, hit return")
input('<return> or ctrl+c: ')

print('First, we open it...')
target = open(filename, 'w') # 'w' is needed when you're writing to a file that exists
print('Then we erase it...')
target.truncate()
print('Now that we have an empty file, lets write to it.')
line1 = input('What is your full name? : ')
line2 = input('What is your favorite ice cream? : ')
line3 = input('What is your favorite song? : ')
newLine = '\n'


#wrong
#target.write(line1.format('\n') + line2.format('\n') + line3.format('\n'))

#target.write(line1 + newLine + line2 + newLine + line3)

target.close()
#print(f"{line1}\n{line2}\n{line3}\n")
