# checking the datatype
a="3"
print(type(a))

# converting string into float
b="31"
t=float(b)
print(type(t))
print(t)

# taking input from user
c=input("enter a number: ")
print("You entered this number:", c)

# making the input into integer
d=int(input("enter a number: "))
e=int(input("enter another number: "))
print("The sum of the two numbers is:", d + e)
print("is d bigger than e?", d > e)

# Taking input with f-string
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")
# Here, writting f is imp and the curly braces {} are used to display the values of variables given by users

#  without f-string
print("Hello, {name}! You are {age} years old.") 
# the {name} are not replaced by values and directly got written as it is