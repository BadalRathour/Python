# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value)
# and returns a new sequence containing only the elements that meet the predicate.

# syntax
# filter(function, iterable)

l = [1, 2, 4, 6, 4, 3]

def filter_function(a):
    return a>=4

new_list = list(filter(filter_function, l))
print(new_list)

