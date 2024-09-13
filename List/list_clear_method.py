# Python List clear()
# The clear() method removes all items from the list.

# Syntax of List clear()
# list.clear()

prime_numbers = [2, 3, 5, 7, 9, 11]

# remove all elements
prime_numbers.clear()

# Updated prime_numbers List
print('List after clear():', prime_numbers)

# Output: List after clear(): []

""" Example 1: Working of clear() method """
# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
list.clear()

print('List:', list)

""" Example 2: Emptying the List Using del """

# Defining a list
list = [{1, 2}, ('a'), ['1.1', '2.2']]

# clearing the list
del list[:]

print('List:', list)