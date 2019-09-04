# input
# end = ' ' tell print not to end the line with a newline character and go to the next line
print("How old are you?", end=' ')
age = int(input())
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#input()
# the function pauses your program and waits for the use to enter some text
# Once the input is recived, it assigns it to a variable.--python crash course page114
# example
message = input("Tell me your name: ")
print(f"Hello, {message}. Nice to meet you.")

