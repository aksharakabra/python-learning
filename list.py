friends=["leo", 1, "CERI", 23.4, True]

print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print(friends)

friends[0]="AKSHARA"
print(friends)
# changing the value of the list at index 0 from "leo" to "AKSHARA"

            # Slicing in list
print(friends[0:3])
print(friends[:3])
print(friends[2:5])

            # LIST METHODS
friends.append('Aou')
print(friends)
# adds an element to the end of the list.

friends.insert(2, 32)
print(friends)
# inserts an element at a specified index in the list.

friends.remove(32)
print(friends)
# removes the first occurrence of a specified element from the list.

value=friends.pop()
friends.pop(1)
print(friends)   # prints the list after popping an element
print("Popped value:", value)
# removes and returns the last element from the list.

friends.clear()
print(friends)
# removes all elements from the list, resulting in an empty list.

list1=[1, 3, 2, 8, 5]
list1.sort()
print(list1)
# sorts the elements of the list in ascending order.

list1.reverse()
print(list1)    
# reverses the order of the elements in the list.

print(sum(list1))
# returns the sum of all elements in the list.

                # real use case of list

# program to take input of fruit names from the user and store them in a list.
fruits=[]
fruits.append(input("enter the fruit name: "))
f2= input("enter second fruit name: ")
fruits.append(f2)
print(fruits)

# to take marks of students and display in a sorted manner.
marks=[]
marks.append(float(input("enter marks of ram: ")))
marks.append(float(input("enter marks of shyam: ")))
marks.append(float(input("enter marks of sita: ")))
marks.sort()
print(marks)