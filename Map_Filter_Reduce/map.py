# The map function applies a function to each element in a sequence and returns a new sequence containing the 
# trasnfared elements. 

# syntax
# map(function, iterable)

def cube(x):
    return x*x*x
print(cube(2))

""" Iterate through for loop"""
l = [1, 2, 4, 6, 4, 3]
newl = []
for item in l:
    newl.append(cube(item))
    print(newl)

""" USE Map"""
l = [1, 2, 4, 6, 4, 3]
newl = list(map(cube, l))
print(newl)

