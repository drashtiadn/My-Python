#Opening a file with 'w' or 'w+' anything that was in the original file is deleted!
f=open('C:\\Users\\Gaurav\\Downloads\\OneDrive\\Desktop\\My Python Stuff\\FILES\\another.txt','w')
f.write("I am writing")
f.close()