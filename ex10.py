# Escaping characters and newlines and tabs and multi-line strings

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list.
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

line = "-----------------------------------------------"
print(line)
print("Escape\tWhat it does.")
print(line)
print("\\\\\tBackslash(\\)")
print(line)
print("\\'\tSingle-quote(')")
print(line)
print("\\\"\tDouble-quote(\")")
print(line)
print("\\r\tCharage Return(CR)")
print(line)
print("\\t\tHorizontal Tab (TAB)")
print(line)