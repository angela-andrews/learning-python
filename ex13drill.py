# study drill for ex13
from sys import argv

script, color = argv

print("What is your name?: ", end = ' ') # remeber the end puts the prompt on the same line
name = input()

print(f"Your name is {name} and your favorite color is: ",color)
print("You just ran the script called ", script)


