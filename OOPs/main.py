# In Programming mainly there are two approaches that are two approaches that are used to write program or code.
# 1. Procedural Programming
# 2. Object Oriented Programming
# The basic idea of object oriented programming (OOPs) is use to classes and objects to represent the real-world 
# conepts and entities


# Class: A class is a blueprint or template for creating the objects. It defines the properties and methods that an object
# of that class will have. Properties are the data or state of an object, and methods are the actions or behaviour
# that an object can perform.

# Object: An object is an instance of class, and it contains its own data and methods. For example you can create
# a class called "Person" that has properties such as name and age, and methods such as speak() and walk(). Each instance 
# of the person class would be a unique object with its own name and age, but they would all have the same methods to speak and walk.

# An object is any entity that has attributes and behaviors. For example, a parrot is an object. It has

# attributes - name, age, color, etc.
# behavior - dancing, singing, etc.
# Similarly, a class is a blueprint for that object.

class Parrot:

    # class attribute
    name = ""
    age = 0

# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")