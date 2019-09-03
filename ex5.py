name = 'Angela Andrews'
age = 23 # a lie
height = 66 # inches
weight = 150 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Dark Brown'
# print f requires python 3.6+ I had to upgrade on my Ubuntu system.
# format strings aka string interpolation in JavaScript parlance.
print(f"Let's talk about {name}.")
print(f"She's {height} inches tall. ")
print(f"She's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} depending on coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}. ")

in_to_cm = 2.54
height_in_cm = round(height * in_to_cm)
print(f"{name}'s height in centimeters is {height_in_cm}")
kg= round(weight / 2.2046)
print(f"{name}'s weight in kilograms is {kg}.'")

# notes
# inch = 2.54 centimeters
#  in_to_cm = 2.54
# height * in_to_cm
# kg= weight / 2.2046