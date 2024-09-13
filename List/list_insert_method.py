# The insert() method inserts an element to the list at the specified index.

# Syntax of List insert()
# list.insert(i, elem)
# Here, elem is inserted to the list at the ith index. All the elements after elem are shifted to the right.


# create a list of vowels
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')

print('List:', vowel)

""" Example 1: Inserting an Element to the List """

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# insert 11 at index 4
prime_numbers.insert(4, 11)

print('List:', prime_numbers)


""" Example 2: Inserting a Tuple (as an Element) to the List """
mixed_list = [{1, 2}, [5, 6, 7]]

# number tuple
number_tuple = (3, 4)

# inserting a tuple to the list
mixed_list.insert(1, number_tuple)

print('Updated List:', mixed_list)

