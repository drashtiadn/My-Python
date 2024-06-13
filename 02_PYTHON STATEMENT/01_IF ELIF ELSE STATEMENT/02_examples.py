#Let's create some simple examples for the if, elif, and else statements:
#1st example
person = 'Sammy'
if person == 'Sammy':
    print('Welcome Sammy!')
else:
    print("Welcome, what's your name?")

#2nd example
person = 'George'

if person == 'Sammy':
    print('Welcome Sammy!')
elif person =='George':
    print('Welcome George!')
else:
    print("Welcome, what's your name?")

#3rd example
a = 10

if a<5:
    print("It is less than 5")
elif a==5:
    print("It is equal to 5")
elif a==10:
    print("It is equal to 10")
else:
    print("It is more than 10")

#4th example
age = int(input("Enter your age: "))

if age>18:
    print("Yes")
else:
    print("No")

#5th example(using comparsion and logical operators)
age = int(input("Enter your age: "))

if(age>34 or age<56):
    print("You can work with us")

else:
    print("You cannot work with us")