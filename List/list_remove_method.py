# The remove() method removes the first matching element (which is passed as an argument) from the list.

# Syntax of List remove()
# list.remove(element)

# The remove() method takes a single element as an argument and removes it from the list.
# If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.

""" Example 1: Remove element from the list """

# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' is removed
animals.remove('rabbit')

# Updated animals List
print('Updated animals list: ', animals)

""" Example 2: remove() method on a list having duplicate elements """
# If a list contains duplicate elements, the remove() method only removes the first matching element.

# animals list
animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' is removed
animals.remove('dog')

# Updated animals list
print('Updated animals list: ', animals)

""" Example 3: Deleting element that doesn't exist """

# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# Deleting 'fish' element
animals.remove('fish')

# Updated animals List
print('Updated animals list: ', animals)