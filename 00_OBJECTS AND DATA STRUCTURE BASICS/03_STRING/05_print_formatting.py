# .format() Method
print('My name is {}'.format("David"))
print('There {} {} {}'.format('is','a','tiger'))
print('The {2} {1} {0}'.format("angry","is","tiger"))   #Inserted objects can be called by index position
print('The {t} {g} {h}'.format(h="angry",g="is",t="tiger"))   #Inserted objects can be assigned keywords
print('A {p} saved is a {p} earned.'.format(p='penny'))  #Inserted objects can be reused, avoiding duplication
print('The {2} {2} {2}'.format("angry","is","tiger"))

#f-string Method
name='Fred'
print(f"He said his name is {name}.")
print(f"He said his name is {name!r}.")       #Pass !r to get the string representation

#Float formatting follows ------->   "result: {value:{width}.{precision}}"
num=23.45678
print("My 10 character,four decimal number is:{0:10.4f}".format(num))

#f-string formatting follows ------->   "result: {value:{width}.{precision}}"
num=23.45678
print(f"My 10 character,four decimal number is:{num:{5}.{6}}") #Note that with f-strings, precision refers to the total number of digits, not just those following the decimal.

#Use .format() method syntax inside an f-string
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")