# Python Variables Scope
# In Python, we can declare variables in three different scopes: local scope, global, and nonlocal scope.

""" 1. Python Local Variables """

def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()

# try to access message variable 
# outside greet() function
# print(message)

""" 2. Python Global Variables"""

# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)


""" 3. Python Nonlocal Variables """
# In Python, the nonlocal keyword is used within nested functions to indicate that a variable is not local to the inner function, but rather belongs to an enclosing function’s scope.

