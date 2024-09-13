# The extend() method adds all the items of the specified iterable, such as list, tuple, dictionary, or string , 
# to the end of a list.

# Syntax of List extend()
# list1.extend(iterable)

# The extend() method takes a single argument.
# iterable - such as list, tuple, string, or dictionary
# The extend() doesn't return anything; it modifies the original list.


numbers1 = [3, 4, 5]

numbers2 = [10, 20]

# add the items of numbers1 to the number2 list
numbers2.extend(numbers1)
# print(f"numbers1 = {numbers1}")
# print(f"numbers2 = {numbers2}")

print(numbers1)
print(numbers2)


""" Example 1: Using extend() Method """
languages = ['French', 'English']
languages1 = ['Spanish', 'Portuguese']

# append items of language1 to language
languages.extend(languages1)
print('Languages List:', languages)

""" Example 2: Add Items from Other Iterables """

languages = ['French']

languages_tuple = ('Spanish', 'Portuguese')

# add items of the tuple to the languages list
languages.extend(languages_tuple)
print( languages) 

languages_set = {'Chinese', 'Japanese'}

# add items of the set to the languages list
languages.extend(languages_set)
print(languages)


""" Example 3: Using + to Extend a List"""
a = [1, 2]
b = [3, 4]

a = a + b

print( a) # [1, 2, 3, 4]

""" Example 4: Python extend() Vs append() """
# If you need to add the item itself (rather than its elements), use the append() method.
a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)

# add items of b to the a1 list
a1.extend(b) #  [1, 2, 3, 4]
print(a1)

# add b itself to the a1 list
a2.append(b)
print(a2)

