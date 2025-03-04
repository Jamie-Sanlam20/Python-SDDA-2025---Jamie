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


# Why error -> you're trying to access the value before it's being declared/assigned

# Case 4: Python knows that locally the price variable is present

# python doesn't consider 200 (almost like it dosn't exist), because local price is preferred

# When you call the function -> it checks whether there are declarations (price = ..)
# price (name) -> noted -> value isn't noted
