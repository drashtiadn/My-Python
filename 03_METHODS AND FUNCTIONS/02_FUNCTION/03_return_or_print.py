# What is the difference between return and print?
'''The return keyword allows you to actually save the result of the output of a function as a variable. 
   The print() function simply displays the output to you, but doesn't save it for future use. '''

#  print
def print_result(a,b):
    print (a+b)

print_result(10,5)

#But what happens if we actually want to save this result for later use?

my_result = (print_result(20,20))
print(my_result)
print(type(my_result))

'''Be careful! Notice how print_result() doesn't let you actually save the result to a variable!
 It only prints it out, with print() returning None for the assignment!'''

#  return
def return_result(a,b):
    return (a+b)

print(return_result(3,11))

#But what happens if we actually want to save this result for later use?
my_result = (return_result(20,20))
print(my_result)
print(type(my_result))