#random
#Python comes with a built in random library. 
#There are a lot of functions included in this random library.
#Some useful function for now
my_list = [10,20,30,40,100]
from random import shuffle
# This shuffles the list "in-place" meaning it won't return
# anything, instead it will effect the list passed
# shuffle(my_list)
print(my_list)

from random import randint
# Return random integer in range [a, b], including both end points.
randint(0,100)
print(randint(0,100))
'''NOT WORKING'''
