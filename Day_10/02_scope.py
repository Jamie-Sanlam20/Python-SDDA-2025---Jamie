# Scope of variable
# Defined: Lifetime of variable
# Area in which the variable is alive (which line no. to which line no.)

# t1 = 100

# def simple():
#     t2 = 10
#     print(t2)  # t2 can only be accessed inside the function

# simple()
# print(t1) # ✅ -> can be accessed
# print(t2) # ❌ error --> cannot access t2 because it's scope/lifetime is IN the simple function
# # NameError: name 't2' is not defined

# t2 -> simple function scope

price = 100


# Case 1:
def get_price():
    print("The price of the book is: ", price)


get_price()

# get_price
# 1. First checks for local 'price' variable -> if there's a 'price' variable in the function
# 2. Then goes to outer scope (Lexical scope)

# Variables in a function, cannot be accessed outside
# Variables outside the function can be accessed inside the function.

# Lexical scope -> just outside of the function
# Closure == Lexical scope + function scope
