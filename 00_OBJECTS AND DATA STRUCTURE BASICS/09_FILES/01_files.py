# Use open function to read the content of a file!
# By default, the open() function will only allow us to read the file.
# f = open('sample.txt', 'r')
# or you can copy the path of .txt file but make sure to use double \\ instesd of single \
f = open('C:\\Users\\Gaurav\\Downloads\\OneDrive\\Desktop\\My Python Stuff\\FILES\\sample.txt')    # by default the mode is r
data = f.read()
print(data)

# Seek to the start of file (index 0)
# This happens because you can imagine the reading "cursor" is at the end of the file after having read it. 
# So there is nothing left to read. We can reset the "cursor" like this:
f.seek(0)
data = f.read()
print(data)

f.seek(0)
data=f.read(5) # reads first 5 characters from the file
print(data)
f.close() # Make sure to close the file once you have finish