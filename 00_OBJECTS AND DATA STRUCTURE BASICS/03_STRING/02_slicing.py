#String 
greetings="Good Morning,"
name="Amit"
print(type(name))

#Concetating two strings
c=greetings+name
print(c)

#Multiplication/Repetition
a=name*10
print(a)

#String Slicing
name="David"       
print(len(name))                 #Length is 5 
print(name[4])                   #Index counting starts from 0
#name[3]="f"                     #Replacing does not work

print(name[1:4])                 #starts from 1 till 3 does not include 4th character
print(name[:4])                  #is same as name[0:4]
print(name[1:])                  #is same as name[1:5]

#Negative Indices [length - negative indices]
print(name[-4:-1])               #is same as name[1:4]
'''Here, print(name[-4:-1]), means that, name is of 5 characters therefore 5-4= 1, and 5-1= 4....
It will be like this •print(name[1:4]), including 1 and not 4!!'''
print(name[-5:-1])               #is same as name[0:4]

#Slicing with skip value    [start index:end index:skip value]
print(name[0:6:2])               #is skip 1 character
print(name[1::])                 #is same as name[1:5]
print(name[0::-1])
print(name[:0:-1])
print(name[::-1])                #backwards
print(name[-1])