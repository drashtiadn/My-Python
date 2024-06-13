# filter syntax:
# filter(function, iterable) --> filter object

def check_even(num):
    return num%2 == 0

number = [0,1,2,3,4,5,6,7,8,9,10]
print(filter(check_even,number))
print(list(filter(check_even,number)))