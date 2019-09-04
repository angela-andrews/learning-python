# prompting and passing
#using agrv and input together

from sys import argv
#don't forget this line
script, user_name = argv
# this changes the prompt from a blank to a greater than
prompt = '> '

# the user_name comes from the commandline as does the script
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives= input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)
# these variables come from input and are saved to variables
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
You have a {computer} computer. Nice.
""")