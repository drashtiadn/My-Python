#Accepting parameters (arguments)
def greeting(name):
    print(f'Hello {name}')   #using f-string

greeting('Monica')

#print
def greetings(name):
    print ("Hello "+name)    #using print 

greetings('Rachel')

#return
def greetings(name):
    return ("Hello "+name)    #using return 

print(greetings('Ross'))