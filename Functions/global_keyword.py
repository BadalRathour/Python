""" Python Global Keyword"""
# In Python, the global keyword allows us to modify the variable outside of the current scope.

# global variable
c = 1 

def add():

     # increment c by 2
    c = c + 2

    print(c)

add() 
# UnboundLocalError: local variable 'c' referenced before assignment

""" Example: Changing Global Variable From Inside a Function using global"""

# global variable
c = 1 

def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2 

    print(c)

add()



