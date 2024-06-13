# **kwargs
# Python offers a way to handle arbitrary numbers of keyworded arguments. 
# Instead of creating a tuple of values, **kwargs builds a dictionary of key/value pairs.

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")
    else:
        print("I don't like fruit")

myfunc(fruit = 'pineapple')

myfunc()

# It is worth noting that the word "kwargs" is itself arbitrary - any word will do so long as it's preceded by an asterisk twice. 
# For example:

def myfunc(**city):
    if 'place' in  city:
        print(f"My favorite place is {city['place']}")
    else:
        print("I don't like this city")

myfunc(place = 'California')