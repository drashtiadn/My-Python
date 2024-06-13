#.readline()
f = open ('C:\\Users\\Gaurav\\Downloads\\OneDrive\\Desktop\\My Python Stuff\\FILES\\sample.txt')
#read first line
data = f.readline()
print(data)

#Read second line
data = f.readline()
print(data)

#Read third line
data = f.readline()
print(data)

#Read fourth line... and so on...
data = f.readline()
print(data)
f.close()

'''  '''    '''      OR     '''     '''   '''    
      
#.readlines()                                                              
#You can read a file line by line using the readlines method.
f = open ('C:\\Users\\Gaurav\\Downloads\\OneDrive\\Desktop\\My Python Stuff\\FILES\\sample.txt')
data = f.readlines()
print("\n",data)
f.close()

#NOTE:You can readline from starting by using .seek(0)