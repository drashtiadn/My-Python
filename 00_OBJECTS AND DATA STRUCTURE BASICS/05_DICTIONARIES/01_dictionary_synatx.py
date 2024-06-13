#Dictionary is {'key':'value'}
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(my_dict['key3'])                    #printing the value of the key
print(my_dict['key3'][0])                 
print(my_dict['key3'][0].upper())         #UPPERCASE
print(my_dict['key1'])                    #Value of key1
print(my_dict['key1']-123)                #Subtraction

myDict = {
    "Fast": "In a Quick Manner",
    "Harish": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'Harish': 'Player'}
}

print(myDict['Fast'])
print(myDict['Harish'])
myDict['Marks'] = [45, 78]                 #Replace
print(myDict['Marks'])
print(myDict['anotherdict']['Harish'])      