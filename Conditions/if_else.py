# If-else in Python

# Example 1 - Person can drive or not - It will give boolean result (True or False)
# a = int(input("Enter your age: "))
# print("Your age is: ", a)
# if(a>18):
#     print("You can drive!")
# else:
#     print("You cannot drive!")

# Example 2
#Conditional Operators: >, <, >=, <=, ==, !=
# a = int(input("Enter your age: "))
# print("Your age is: ", a)
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
# #
# if(a>18):
#     print("You can drive!") #identation - new block is getting start
# else:
#     print("You cannot drive!")


#Example 3
# fruit_price = 120
# budget = 150
# if fruit_price <= budget:
#     print("Add 1 kg fruits to the cart")
# else:
#     print("Do not add fruits in the cart")


# Example 4 - if-elif conditions
# price = 100
# if price > 100:
#     print("price is greater than 100")
# elif price == 100:
#     print("price is 100")
# elif price < 100:
#     print("price is less than 100")

# Example 5 - if-elif-else Conditions
# price = 50
# if price > 100:
#     print("price is greater than 100")
# elif price == 100:
#     print("price is 100")
# elif price < 100:
#     print("price is less than 100")

# Example 6 - Nested if-elif-else Conditions
price = 50
quantity = 5
amount = price*quantity

if amount > 100:
    if amount > 500:
      print("Amount is greater than 500")
    else:
      if amount <= 500 and amount >= 400:
        print("Amount is between 400 and 500")
      elif amount <= 400 and amount >= 300:
        print("Amount is between 300 and 400")
      else:
        print("Amount is between 200 and 300")
elif amount == 100:
    print("Amount is 100")
else:
    print("Amount is less than 100")




