# An attribute is a characteristic of an object.# A method is an operation we can perform with the object.

'''
# The syntax for creating an attribute is:

           self.attribute = something

# There is a special method called:

__init__()

'''
## Attribute Example

class Dog:

    def __init__(self,breed) :
        self.breed = breed                         #Attribute of object

sam = Dog(breed = 'Lab')
frank = Dog(breed = 'Huskie')

print(sam.breed)
print(frank.breed)


## Class Object Attribute Example

class Dog:

    # Class Object Attribute
    species = 'mammal'

    def __init__(self,breed,name):            
        self.breed = breed                        #Attribute of object
        self.name = name                          #Attribute of object

sam = Dog('Lab','Sam')
print(sam.name)

'''Note that the Class Object Attribute is defined outside of any methods in the class. 
Also by convention, we place them first before the init.'''

print(sam.species)
