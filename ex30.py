# else and if
# just like 29 but with else and elif

people = 30
cars = 40
trucks = 15

if cars < people:
    print("We should take the cars.")
elif (cars > people) and (cars >= trucks):
    print("We should NOT take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could still take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
