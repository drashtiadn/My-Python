#Creating of tuple using()
t=(1,2,4,'five')
print(len(t))    #length of tuple

z=()             #Empty tuple
#z=(1)         # Wrong way to declare a Tuple with Single element
z=(1,)           #Tuple with single element
print(z)

#Printing the elements of tuple
print(t[0])       # Use indexing just like we did in lists
print(t[-1])      # Slicing just like a list

#Cannot update the values of tuple
#t[0]=34         #throws an error