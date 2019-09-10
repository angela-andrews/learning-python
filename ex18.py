# this one is like your scripts with argv
# 4 space & don't forget the colon:
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#  ok, *args is pointless, just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this takes 1 argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this takes NO argument
def print_none():
    print("I got nothing for you.")


print_two("Angela", "Andrews")
print_two_again("Scooter","Phoenix")
print_one("Butter Almond")
print_none()

    