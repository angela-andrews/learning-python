# Strings and Text
# setting a variable to a number
types_of_people = 10
# setting a variable to a string with format string inside
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# .format()syntax: format an already created string
hilarious = False 
joke_evauluation = "Isn't that joke so funny!?!? {}"

print(joke_evauluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# string contcatenation 
print(w + e)