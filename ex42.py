# Is-A, Has-A, Objects, and Classes
# is-a: When you talk about objects and classes being related to each other by a class relationship
# Has-a: Whe you talk about objects and classes that are related only because they reference each other

## Animal is-a object
class Animal (object): # object is optional, but is better to be explict than implicit
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        self.name = name

        ## person has-a pet of some kind
        self.pet = None

## Employee is-a class
class Employee(Person):

    def __init__(self, name, salary):
        ## ???
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salar = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat('Satan')

## mary is a person
mary = Person("Mary)


## mary has-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee('Frank', 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()