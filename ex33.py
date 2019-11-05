# while loops

i = 0
numbers = []

while i < 6:
    print(f"At the top is {i}")
    numbers.append(i)

    i = i + 1

    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

# convert while-loop to a function

def test_loop(x):
    i = 0
    numbers = []

    while i < x:
        print(f"At the top is {i}")
        numbers.append(i)

        i = i + 1

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

test_loop(11)
#===============================================

def test_loop2(x, y):
    i = 0
    numbers = []

    while i < x:
        print(f"At the top is {i}")
        numbers.append(i)

        i = i + y

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

test_loop2(29,5)

#======================================
# testing out turning a while into a for using a range

def test_loop3(y):
    numbers = []
    numbers = list(range(y))

    print(numbers)

    for i in numbers:
        print(f"Range made it easy to create a list of numbers: {i}")

    

test_loop3(26)
