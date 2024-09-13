# Python List index()
# The index () method returns the indexed of the specified element in the list

# animals = ['cat', 'dog', 'rabbit', 'horse']
# index = animals.index('dog')
# print(index)


""" Example 1: Find the index of the element """

# vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
# index = vowels.index('e')
# print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
# index = vowels.index('i')

# print('The index of i:', index)

""" Example 2: Index of the Element not Present in the List """
# vowels list
# vowels = ['a', 'e', 'i', 'o', 'u']

# index of 'p' is vowels
# index = vowels.index('p')
# print('The index of p:', index)


"""Example 3: Working of index() With Start and End Parameters """
# alphabets list
# alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# # index of 'i' in alphabets
# index = alphabets.index('e')   # 1
# print('The index of e:', index)

# # 'i' after the 4th index is searched
# index = alphabets.index('i', 4)   # 6
# print('The index of i:', index)

# # 'i' between 3rd and 5th index is searched
# index = alphabets.index('i', 3, 5)   # Error!
# print('The index of i:', index)

""" """