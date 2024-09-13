# The list pop() method removes the item at the specified index. The method also returns the removed item.

# Syntax of List pop()
# list.pop(index)

# The pop() method takes a single argument (index).
# The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
# If the index passed to the method is not in range, it throws IndexError: pop index out of range exception


prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)

print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)

"""" Example 1: Pop item at the given index from the list """
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)

print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)

"""" Example 2: pop() without an index, and for negative indices"""

# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:') 
print('Return Value:', languages.pop())

print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:') 
print('Return Value:', languages.pop(-1))

print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:') 
print('Return Value:', languages.pop(-3))

print('Updated List:', languages)
