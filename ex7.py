# More printing

print("Mary had a little lamb.")
# snow is a string that gets placed inside the brackets
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what did that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch  that command at the end. Try removing it to see what happens
# removed the comma and it caused a syntax error
# the end = ' ' will put a space in the string by assigning a space to the variable called, end.
# the comma will put the next print statement on the same line.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)