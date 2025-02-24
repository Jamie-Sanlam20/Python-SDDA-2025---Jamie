# Task 1.1

stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "tin roof"
stock4 = "cookie dough"

# Output
# Case 1
# Please enter your fav 🍧?: VAnilla
# Yes, we have vanilla in stock

# Case 2
# Please enter your fav 🍧?: salted Caramel
# Sorry, we ran out of Salted Caramel

# Task 1.1
# Clue: if..elif..else


# Task 1.2
#  Clue: or

fav_flavour = input("Please enter your fav 🍧?: ").lower().strip()

# Taking into account whether it will be lowercase or have leading/trailing spaces

# if fav_flavour == stock1:
#     print(f"Yes, we have {fav_flavour}")
# elif fav_flavour == stock2:
#     print(f"Yes, we have {fav_flavour}")
# elif fav_flavour == stock3:
#     print(f"Yes, we have {fav_flavour}")
# elif fav_flavour == stock4:
#     print(f"Yes, we have {fav_flavour}")
# else:
#     print(
#         f"We do not have {fav_flavour} in stock"
#     )


if fav_flavour == stock1 or stock2 or stock3 or stock4:
    print(f"Yes, we have {fav_flavour}")
else:
    print(f"We do not have {fav_flavour} in stock")

# less code -> less things goes wrong

# Task 1.3
# in is simplified version of or

if fav_flavour in (stock1, stock2, stock3, stock4):
    print(f"Yes, we hav {fav_flavour} in stock")
else:
    print(f"No, {fav_flavour} is not in stock")
