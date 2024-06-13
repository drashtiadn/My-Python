# Using with you don't need to close your file
with open('C:\\Users\\Gaurav\\Downloads\\OneDrive\\Desktop\\My Python Stuff\\FILES\\another.txt','r') as f:
    a=f.read()
with open('C:\\Users\\Gaurav\\Downloads\\OneDrive\\Desktop\\My Python Stuff\\FILES\\another.txt','w') as f:
    a=f.write("me")
print(a)