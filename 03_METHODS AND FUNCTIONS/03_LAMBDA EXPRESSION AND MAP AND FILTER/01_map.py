# map syntax:
# map(func, *iterables) --> map object

# Example 1
def square(num):
    return num**2

list_1 = [1,2,3,4,5]
'''METHOD 1 (not using map function)'''
l2 = []
for item in list_1:
    l2.append(square(item))
print(l2)
'''METHOD 2 (using map function)'''
print(list(map(square,list_1)))

# Example 2
def splicer(mystring):
    if len(mystring)%2==0:
        return 'even'
    else:
        return mystring[0]

mynames = ['John','Cindy','Sarah','Kelly','Mike']
print(list(map(splicer,mynames)))