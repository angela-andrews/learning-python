# classes are like modules
# A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"
    # apple function
    def apple(self):
        print("I am classy apples!")

# classes are mini-modules.  Instead of an import, you istantiate a class. When you istantiate a class, you get an object.

# You create a class by calling the class like it's a function like this:

thing = MyStuff() # an object created from the MyStuff class.
thing.apple #prints "A am classy apples"
print(thing.tangerine) # since tangerine is a var in the class, you can use dot notaion to print the variable.




