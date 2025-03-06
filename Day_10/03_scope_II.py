# price = 100


# # Case 1:
# def get_price():
#     print("The price of the book is: ", price)


# get_price()

# get_price
# 1. First checks for local 'price' variable -> if there's a 'price' variable in the function
# 2. Then goes to outer scope (Lexical scope)

# Variables in a function, cannot be accessed outside
# Variables outside the function can be accessed inside the function.

# Lexical scope -> just outside of the function
# Closure == Lexical scope + function scope

# Case 2:
price = 200


def get_price():
    print("The old price is: ", price)
    price = 100
    print("The new price is: ", price)


get_price()

# Why error -> you're trying to access the value before it's being declared/assigned


# # Case 3: Both same variable name (Outside & Inside)
# price = 200  # Live under the shadow
# # Local scope given higher priority


# def get_price():
#     price = 100  # Shadowing # Legend
#     print("The old price is: ", price)  # 100
#     print("The new price is: ", price)  # 100


# get_price()

# python doesn't consider 200 (almost like it dosn't exist), because local price is preferred

# Case 4: Python knows that locally the price variable is present


def get_price():
    print("The old price is: ", price)  # UnboundLocalError
    price = 100  # Assign value
    print("The new price is: ", price)


get_price()


# 2 Phase Execution
# 1. Compilation - Declaration noted
# 2. Execution  - print the value, Assign, Calculation


# Case 2:
# price = 200


# 1. Compilation
def get_price():
    print("The old price is: ", price)  # ❌ skip
    price = 100  # Local variable preference # ✅ price -> name is noted | not value
    print("The new price is: ", price)  # ❌ skip


# When you call the function -> it checks whether there are declarations (price = ..)
# price (name) -> noted -> value isn't noted

get_price()


# # 2. Execution
def get_price():
    print("The old price is: ", price)  # Do we know price? Yes. UnboundLocalError 🤚
    price = 100  # Local variable preference # skip
    print("The new price is: ", price)  # skip


# get_price()

# # Case 3: Both same variable name (Outside & Inside)
# price = 200  # Live under the shadow
# # Local scope given higher priority


# # 1. Compilation
# def get_price():
#     price = 100  # Shadowing # Legend  # ✅ price. name is noted | not value
#     print("The old price is: ", price)  # 100 # ❌ skip
#     print("The new price is: ", price)  # 100 # ❌ skip


# get_price()


# # 2. Execution
# def get_price():
#     price = 100  # Shadowing # Legend  # Do we price. Yes. Value is assigned to 100
#     print("The old price is: ", price) #  Do we price. Yes. ✅ print
#     print("The new price is: ", price)  #  Do we price. Yes. ✅ print


# get_price()

# Case 5:
# price = 200


# def get_price(price):
#     print("The old price is: ", price)
#     price = 100  # Reassignment
#     print("The new price is: ", price)


# get_price(600)


# Summary
# 1. Local gets perfernce
# 2. UnboundLocalError -> If you try access before declaration
# 3. Only functions create new scope


# Case 1:
# t1 = True

# if t1:
#     x = "abc"

# print(x)


# Case 2:


# def cool():
#     t1 = True

#     if t1:
#         x = "abc"


# cool()
# print(x)


# Assignment:
# Write a comparison in terms of scope on keywords
# global vs nonlocal
# with examples
