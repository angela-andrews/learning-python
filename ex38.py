# Doing things to lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not ten things in that list. Let's fix that.")

# splitting ten_things on the space delimiter and assigning to list called stuff
stuff = ten_things.split(' ')
#print(stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# while the lenght of the stuff list is not 10...
# pop off of more_stuff and assign it to the next_one var
while len(stuff) != 10:
    next_one = more_stuff.pop()
    #printing out the item popped off of more stuff and assigned to next_one
    print("Adding: " , next_one)
    # append next_one to the stuff list
    stuff.append(next_one)
    #print out the growing stuff list. each append increased the list.
    print(f"There are {len(stuff)} items now.")
# print out the stuff list
print("There we go", stuff)

print("Let's do some things with stuff.")

# print the 1st index of stuff: Oranges
print(stuff[1])
# print the last index of stuff: corn
print(stuff[-1])
# pop off the last itme in stuff and print it out: corn
print(stuff.pop())
# join takes an iterable object, like a list and each element is 'joined' by a space
print(' '.join(stuff))
# join will iterate the list from the 3rd index up to but not including the 5th index and each element is 'joined' by a #
print("#".join(stuff[3:5]))

print("------print more stuff--------")
# for loop for each item left in the more_stuff list, print each item
for each in more_stuff:
    print(each)

