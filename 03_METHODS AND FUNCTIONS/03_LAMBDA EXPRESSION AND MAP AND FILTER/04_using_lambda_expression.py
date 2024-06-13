# Examples of Lambda Expression:

#Example 1:Squares
my_nums = [1,2,3,4,5]
print(list(map(lambda num:num**2,my_nums)))

#Example 2:Even Number
print(list(filter(lambda num:num%2==0,my_nums)))

#Example 3:Lambda expression for grabbing the first character of a string
print(lambda s:s[0])

#Example 4:Lambda expression for reversing a string
print(lambda s:s[::-1])

#Example 5:Pass in multiple arguments into a lambda expression
print(lambda x,y:x+y)