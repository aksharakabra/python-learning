# a dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value.
#  In Python, dictionaries are implemented as hash tables, allowing for efficient lookups, insertions, and deletions.

#it is mutable
marks={
    "akshara": 100,
    "aou" :92,
    "ceri": 65
}

                #methods in dictionary
print(marks, type(marks))

print(marks["akshara"])  
# accessing the value associated with the key "akshara"
# here, we cant write marks[0] because dictionary is not indexed like list.

print(marks.get("aou"))
# another way to access the value associated with the key "aou"

print(marks.keys())
# returns a view object that displays a list of all the keys in the dictionary.

print(marks.values())
# returns a view object that displays a list of all the values in the dictionary.

print(marks.items())
# returns a view object that displays a list of tuples, where each tuple contains a key-value

print(update := {"akshara": 95, "mia": 98})
# updates the values associated with the keys "akshara" and "mia" in the marks dictionary.

print(marks)