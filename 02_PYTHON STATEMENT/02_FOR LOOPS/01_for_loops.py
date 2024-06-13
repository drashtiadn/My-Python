#Iterating through a List
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)

#Even or Odd Number
for num in list1:
    if num % 2 == 0:
        print("Even Number:",num)
    else:
        print("Odd Number:",num)

#Sum of a Number
list_sum = 0
for num in list1:
    list_sum = list_sum + num
    print(list_sum)  #See the difference in print indentation after (This show each sum number once it is add)
print(list_sum)  #See the difference in print indentation before (This show direct total sum number)

#Iterating through a String
for letter in "This is String.":
    print(letter)

#Iterating through a Tuple
tup = (1,2,3,4,5)
for t in tup:
    print(t)

# Tuple Unpacking from list
list2 = [(1,2),(3,4),(5,6),(7,8)]
for tup in list2:
    print(tup)
# Now with unpacking
for (t1,t2) in list2:
    print(t1)

#Iterating through a Dictionary
d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)

# We're going to introduce three new Dictionary methods: .keys(), .values() and .items()
print(d.items())
# Dictionary unpacking 
for k,v in d.items():
    print(k)
    print(v)
# If you want to obtain a true list of keys, values, or key/value tuples, you can cast the view as a list:
print(list(d.keys()))
# Dictionaries are unordered,so to sort
print(sorted(d.values()))