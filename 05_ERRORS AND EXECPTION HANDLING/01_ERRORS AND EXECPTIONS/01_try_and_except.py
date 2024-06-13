# try and except
try:
    f = open('testfile','w')
    f.write('Test write this')
except IOError:                     # You can or cannot specify error
    # This will only check for an IOError exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()

## Now let's see what would happen if we did not have write permission (opening only with 'r'):

try:
    f = open('testfile','r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()