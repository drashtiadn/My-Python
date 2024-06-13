#zip
#Notice the format enumerate actually returns, let's take a look by transforming it to a list()
print(list(enumerate('abcde')))

#can use the zip() function to quickly create a list of tuples by "zipping" up together two lists.
my_list1=[1,2,3,4,5]
my_list2=['a','b','c','d','e']
# This one is also a generator!
print(zip(my_list1,my_list2))
print(list(zip(my_list1,my_list2)))

#To use the generator, we could just use a for loop
for item1,item2 in zip(my_list1,my_list2):
    print('For this tuple,first item was {} and second item was {}'.format(item1,item2))