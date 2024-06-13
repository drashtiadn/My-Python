#Dictionaries Method
mydict={
    "fast":"In a Quick Manner",
    "harish":"A Coder",
    "marks":[1,2,5],
    "anotherdict":{'harish':'Player'},
    1:2
}

print(list(mydict.keys())) # Prints the keys of the dictionary
print(mydict.values()) # Prints the keys values of the dictionary
print(mydict.items()) # Prints the (key, value) for all contents of the dictionary
print(mydict)

updatedict={
    "Ross":"Friend",
    "Rachel":"Friend",
    "David":"Friend",
    "Disco":"A Dancer"
}
mydict.update(updatedict) # Updates the dictionary by adding key-value pairs from updatedict
print(mydict)
print(mydict.get("Disco")) # Prints value associated with key "Disco"
print(mydict["Disco"]) # Prints value associated with key "Disco"

# The difference between .get and [] sytax in Dictionaries?
print(mydict.get("Disco2")) # Returns None as Disco2 is not present in the dictionary
print(mydict["Disco2"]) # throws an error as Disco2 is not present in the dictionary