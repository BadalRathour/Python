# The reverse() method reverses the elements of the list.

# Syntax of List reverse()
# list.reverse()

# The reverse() method doesn't take any arguments.
# The reverse() method doesn't return any value. It updates the existing list.

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()

print('Reversed List:', prime_numbers)

# Output: Reversed List: [7, 5, 3, 2]


""" Example 1: Reverse a List """

# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# List Reverse
systems.reverse()

# updated list
print('Updated List:', systems)

""" Example 2: Reverse a List Using Slicing Operator """

# Operating System List
# systems = ['Windows', 'macOS', 'Linux']
# print('Original List:', systems)

# # Reversing a list	
# # Syntax: reversed_list = systems[start:stop:step] 
# reversed_list = systems[::-1]

# # updated list
# print('Updated List:', reversed_list)

""" Example 3: Accessing Elements in Reversed Order """

# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for shivansh in reversed(systems):
    print(shivansh)
