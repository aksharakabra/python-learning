# tuple is an immutable list.
# its written in () brackets.

a=(1, 2, False, "ram", 5.36 ,1)

b=()  #empty tuple

c=(1,)  #tuple with single element
# but it cant be written as a=(1) because it will be considered as an integer.

                # TUPLE METHODS
print(a)

print(type(a))

print(a.index("ram"))    
# returns the index of the first occurrence of a specified element in the tuple. 

print(a.count(1))                
# returns the number of occurrences of a specified element in the tuple.

print(a[0])
# accessing the first element of the tuple.

print(a[1:4])
# slicing the tuple to get elements from index 1 to 3 (4 is excluded).

print(2 in a)
# checks if the element 2 is present in the tuple and returns True or False.

print(a*3)
# repeats the elements of the tuple 3 times.