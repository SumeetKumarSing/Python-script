def greet():
    print("Hello")


greet()



def greet(i):
    print("Hello", i)

greet("Rahul")



def add(a,b):
    return(a+b)


result = add(5,6)

print(result)

#----------------------
# Postion funcation


def greet(name,age):
    print("Name", name)
    print("age", age)

greet("Ravi",12)


#===========================

# keyword function

def greet(name,age):
    print("Name", name)
    print("age", age)

greet(age=12,name="Ravi")


#=======================

# Default function

def greet(name,age=10):
    print("Name", name)
    print("age", age)

greet("Sumeet")

greet("Sumeet",15)

#=================
# variable 

def show(*no):
    for i in no:
        print(i)

show(12,13,14)