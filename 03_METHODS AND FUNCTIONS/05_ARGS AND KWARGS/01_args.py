# *args
# When a function parameter starts with an asterisk(*), it allows for an arbitrary number of arguments, and the function takes them in as a tuple of values.

def myfunc(*args):
    return sum(args)*.05

print(myfunc(40,60,20))

# Notice how passing the keyword "args" into the sum() function did the same thing as a tuple of arguments.
# It is worth noting that the word "args" is itself arbitrary - any word will do so long as it's preceded by an asterisk. 
#For example:

def myfunc(*spam):
    return sum(spam)*.05

print(myfunc(100,40,60))