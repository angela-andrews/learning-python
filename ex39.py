# dictionaries
#This is a list
things = ['a', 'b', 'c', 'd']
# How you grab an item from a list via it's index
print(things[1])
# assigning a string to index 1
things[1]= 'z'
print(things[1])
# the list has been updated
print(things)
print('-------------------------------------------------')
#create a dictionary
stuff = {
    'name': 'Angela',
    'age': 28,
    'height' : 5 * 12 + 6
    }
# print the value of the name key
print(stuff['name'])
#print the value of the age key
print(stuff['age'])
# print the value of the height key
print(stuff['height'])
# assign a new key called city and give it a value
stuff['city']= "Illadelph"
print(stuff['city'])
# a key can be a number
stuff[1] = "wow"
print(stuff[1])
stuff[2]= "that's lit"
print(stuff[2])
print(stuff)
print('-------------------------------------------------')

# deleting from a dict
del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)
print('-------------------------------------------------')
# creating  a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 50)
print('NY state has: ', cities['NY'])
print('OR state has: ', cities['OR'])

# print some states
print('-' * 50)
print('Michigan\'s abbreviation is: ', states['Michigan'])
print('Florida\'s abbreviation is: '), states['Florida']

# do it by using the state then city dict
print('-' * 50)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

# print every state abbrevation
print('-' * 50)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

# print every city in state
print('-' * 50)
for abbrev, city in list (cities.items()):
    print(f'{abbrev} has the city {city}')

# now do both at the same time
print('-'* 50)
for state, abbrev in list(states.items()):
    print(f'{state} state is abbreviated {abbrev}')
    print(f'and has city {cities[abbrev]}')

print('-' * 50 )
# safely get an abbreviation of a state that's not there
state = states.get('Texas')
if not state:
    print('Sorry, no Texas.')

# get a city with a default value
# cities is a dict and the get() method will get the value for that key
# the string after the comma is what's returned if the key doesn't exist
city = cities.get('TX', 'Does NOT Exist')
print(f"The city for the state 'TX' is: {city}")

print('=' * 50)
# study drills
# adding my city and state
states['Pennsylvania'] = 'PA'
cities['PA'] = "Philadelphia"
states['Georgia'] = 'GA'
cities['GA'] = "Atlanta"
print(states)
print(cities)

# deleting a key:value pair
del states['Georgia']
del cities['GA']
print('*' * 30)
# listing out a dict and making a list of the keys
print(list(cities))
print('*' * 30)
# sorting a dict keys in alphabetical order and returning a list
print(sorted(states))

# does something really exist in a list if so, it prints true
# if not, it prints false
print('Panama' in states)
print('Oregon' in states)
print('*' * 30)
# dict() constructor builds dictionaries directly from sequences of key-value pairs:
myCurrentFaves = dict([('book', 'Blue Moon'),('audioboook', 'Fever Dream'), ('song', 'Money')])
print(myCurrentFaves)
dashes = '=' * 15
print(f'{dashes}Looping a dict{dashes}')
for key, value in myCurrentFaves.items():
    print(f'The key is: "{key}" : The value is: "{value}"')

# adding some list looping in here 
# you can loop through a list and pull out both the index and the value using enumerate()
print(f'{dashes}Using enumerate to loop a list & get the index{dashes}')
for index, value in enumerate(['pillow', 'satin bonnet', 'toothbrush', 'eye mask']):
    print(index, value)
niteNite = ['pillow', 'satin bonnet', 'toothbrush', 'eye mask']
print(f'{dashes}Using enumerate by name of list{dashes}')
for index, value in enumerate(niteNite):
    print(index, value)
print(f'{dashes}Looping over 2 lists with zip {dashes}')

print(f'{dashes}create a dictionary from 2 lists{dashes}')
main = ['salmon', 'steak', 'black beans', 'meatballs']
side = ['broccoli', 'baked potato', 'rice', 'spaghetti']
meal= {}
for m, s in zip(main, side):
    print(f'I like {s} with my {m}.')
    meal[m]=s

print(f'My dict from 2 lists \n{meal}')

print(f'{dashes}testing out collections.OrderedDict{dashes}')
# Ordered dictionaries are just like regular dictionaries but they remember the order that items were inserted. When iterating over an ordered dictionary, the items are returned in the order their keys were first added.
# best explaination of key=lambda
#https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
from collections import OrderedDict
# sort by key
meals = OrderedDict(sorted(meal.items(), key=lambda m: m[0]))
print(meals)