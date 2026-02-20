#Function with Arguments/Parameters AND Return Value
def add(a, b):  # a and b are parameters
    return a + b  # returns the sum

result = add(10, 5)  # arguments 10 and 5
print("Sum is:", result)

#O/P
Sum is: 15

#Function with No Arguments/Parameters BUT Return Value
def greet():
    return "Hello! Welcome to Python"

message = greet()  # No arguments
print(message)

#O/P
Hello! Welcome to Python

#Function with Arguments/Parameters BUT No Return Value
def greet_person(name):
    print("Hello", name)  # Just prints, no return

greet_person("Aqsa")  # argument passed

#output
Hello Aqsa

#Function with No Arguments/Parameters AND No Return Value
def say_hello():
    print("Hello everyone!")  # Just prints

say_hello()

#output
Hello everyone!
