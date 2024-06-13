#Lets slowly break down a lambda expression by deconstructing a function:

# Step 1:
def square(num):
    result = num**2
    return result
print(square(2))

# Step 2(Simplify):

def square(num):
    return num**2
print(square(2))

# Step 3(More Simplify):

def square(num): return num**2
print(square(2))

# Step 4(lambda replace def and func):
lambda num:num**2

# Step 5(You wouldn't usually assign a name to a lambda expression, this is just for demo):
square = lambda num:num**2
print(square(2))