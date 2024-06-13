#enumerate
'''Keeping track of how many loops you've gone through is so common, that enumerate was created so you don't need to worry about creating and 
updating this index_count or loop_count variable'''

index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}\n".format(index_count,letter))
    index_count += 1

# Notice the tuple unpacking!
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))