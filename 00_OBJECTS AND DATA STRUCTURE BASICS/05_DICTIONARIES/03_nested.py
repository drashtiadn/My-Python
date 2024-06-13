#We started off with an empty dictionary, we could continually add to it
d={}
d['animal']='Dogs'
d['answer']=42
print(d)

#Nesting with Dictionaries
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d['key1']['nestkey']['subnestkey'])