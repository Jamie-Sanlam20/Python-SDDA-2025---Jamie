# convert to lambda expression if function body 1 line


def greet(name):
    return f"Hi, {name}"


greet1 = lambda name: f"Hi, {name}"  # doesn't like us naming lambda

print(greet("Jevan"))
print(greet1("Jevan"))

# lambda name -> parameter
# f"Hi, {name} -> return statement (do not have to say return - implicit return)


def add(n1, n2):
    return n1 + n2


add1 = lambda n1, n2: n1 + n2

# Why is it useful?

# map & filter
# map -> function -> takes another function as argument
# map -> Higher order functions

# map calls function to each element
# dbl (10) -> first
# dbl (30) -> second
# dbl (60) -> third

# answers gets passed into list

# filter -> Higher order function (HOF)
# HOF -> map, filter

# filter calls function to each element
gt1 = lambda x: x > 10
# gt(10) -> False
# gt(30) -> True
# gt(60) -> True
# [30, 60]

# if the result is true -> add to output | false gets removed
# gt1 -> Predicate: Returns boolean (if func returns boolean)

# WHEN to use:

# map
# 1. len(input_list) == len(output_list) -> not removing values
# 2. Transform datatype (e.g., list of str -> list of int)
# 3. Doesn't affect Input (original) list -> Output is a copy

player_stats = [10, 30, 60]
boosted_stats = map(lambda x: x * 2, player_stats)
print(boosted_stats, list(boosted_stats))  # Output needs to go in a list
print(player_stats)  # Original list isn't affected

# filter
# 1. len(input_list) >= len(output_list) -> removing some values
# 2. Input data_type == Output data_type -> Cannot transform datatype ❌
# 3. Doesn't affect Input (original) list -> Output is a copy
