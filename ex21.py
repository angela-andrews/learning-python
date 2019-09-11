# Functions can return something

def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"Multiplying {a} x {b}")
    return a * b

def divide(a,b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with functions!!!!")

age = add(9, 8)
height = subtract(99,35)
weight = multiply(45, 3)
iq = divide(634,3.2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ {iq}")

# a puzzle for extra credit, type it anyway
print("here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand????")

