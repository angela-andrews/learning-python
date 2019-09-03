# printing {} formatting
formatter = "{} {} {} {}"
# passing the format function a tuple to be interpolated into the 4 brackets
# in the formatter variable.
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
# A tuple full of strings
print(formatter.format(
    "Testing my own",
    ".format and printing",
    "Still got to look this up.",
    "Time for bed"
))