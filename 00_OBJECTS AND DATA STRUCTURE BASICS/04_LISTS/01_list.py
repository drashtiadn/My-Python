#Creating a list using[]
a=[2,3,43,90,8]

#Print the list using print() function
print(a)

#Access using index using a[0], a[1] , a[2]
print(a[2])
print(a[4])      

#Change the value of the list using
a[0]=98           #List are mutuable
print(a)

#We can create a list with items of different types
c=[45,"Amit",False,6.9]
print(c)

#Add/Multiply the list
a=[1,2,3]
b=[4,5,6]
print(a+b)
print(a*3)

#Sum of list
a = [2, 4, 56, 7]

print(a[0] + a[1] + a[2] + a[3])    #1st way
print(sum(a))                       #2nd way