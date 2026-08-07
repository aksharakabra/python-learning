# String slicing
name= "akshara"
n= name[0:4]
print(n)

a= name[:5]
print(a)

b= name[2:]
print(b)

# negative indexing
c= name[-4:-1]     
print(c)

# Slicing with skip value
d= name[0:7:2]
print(d)

# string as an array
print(name[0])
print(name[3])

            # string functions

print(len(name))

print(name.endswith("ra"))
print(name.endswith("ka"))   #false


print(name.startswith("ak"))
print(name.startswith("ka"))  #false
print(name.startswith("Ak"))  #false because of case sensitivity

print(name.capitalize())
# it capitalizes the first letter of the string and converts all other letters to lowercase.

print(name.count("a"))
print(name.count("A"))

print(name.find("s"))
print(name.find("a"))  #index start from 0
s="hello world"
finding= s.find("world")
print(finding)

print(name.replace("a", "t"))
print(s.replace("world", "universe"))
st="i am a good good girl"
print(st.replace("good", "bad"))  #replaces all occurrences
print(st.replace("good", "bad", 1))  #replaces only the first occurrence

print(name.upper())
# this function converts the string to uppercase.

print(name.lower())
# this function converts the string to lowercase.

print(name.isalpha())
# this function checks whether the string contains only alphabets or not.
#  If it contains only alphabets, it returns True, else it returns False.

print(name.isdigit())
# this function checks whether the string contains only digits or not.


                     # chaining of string functions
print(name.replace("a", "t").replace("k", "p"))

print(s.upper().replace("WORLD", "UNIVERSE").capitalize())

        # checking the accidental double spaces in a string 
print(s.find("  ")) 
 # returns -1 if no double space is found