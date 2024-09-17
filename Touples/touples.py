# A tuple is a collection similar to a Python list. The primary difference is that we cannot modify a tuple once it is created.
# We create a tuple by placing items inside parentheses (). For example,

numbers = (1, 2, -5)
print(numbers)

# Output: (1, 2, -5)

# Tuple Characteristics
# Tuples are:

# Ordered - They maintain the order of elements.
# Immutable - They cannot be changed after creation.
# Allow duplicates - They can contain duplicate values.

""" Ex: 1 Access Items Using Index """

languages = ('Python', 'Swift', 'C++')

# access the first item
print(languages[0])   # Python

# access the third item
print(languages[2])   # C++

"""  Ex: 2 Tuple Cannot be Modified """

# cars = ('BMW', 'Tesla', 'Ford', 'Toyota')

# # trying to modify a tuple
# cars[0] = 'Nissan'    # error
       
# print(cars)

""" Ex: 3 Iterate Through a Tuple """
fruits = ('apple','banana','orange')

# iterate through the tuple
for fruit in fruits:
    print(fruit)

    

