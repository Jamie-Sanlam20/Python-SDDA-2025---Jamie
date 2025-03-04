# Lambda expression/ Lambda Function: Function one liner


def greet(name):
    return f"Hi, {name}"


# convert to lambda expression if function body 1 line

greet1 = lambda name: f"Hi, {name}"  # doesn't like us naming lambda

print(greet("Jevan"))
print(greet1("Jevan"))

# Lambda expression
# 1. Anonymous - nameless function
# 2. One liner
# 3. Implicit return (automatically)


# lambda name -> parameter
# f"Hi, {name} -> return statement (do not have to say return - implicit return)


def add(n1, n2):
    return n1 + n2


add1 = lambda n1, n2: n1 + n2

print(add1(9, 8))

# Why is it useful?

player_stats = [10, 30, 60]
boosted_stats = map(lambda x: x * 2, player_stats)
print(boosted_stats, list(boosted_stats))

# map & filter
# map -> function -> takes another function as argument
# map -> Higher order functions

boosted_stats = map(lambda x: x * 2, [10, 30, 60])

dbl = lambda x: x * 2
boosted_stats = map(dbl, [10, 30, 60])

print(boosted_stats, list(boosted_stats))


def dbl1(x):
    return x * 2


boosted_stats = map(dbl1, [10, 30, 60])
print(boosted_stats, list(boosted_stats))


boosted_stats = map(lambda x: x * 2, player_stats)
print(boosted_stats, list(boosted_stats))

# map calls function to each element
# dbl (10) -> first
# dbl (30) -> second
# dbl (60) -> third

# 1. def - Reuse else where
# 2. lambda - one time use, concise

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

player_stats = [10, 30, 60]
result = filter(gt1, player_stats)
print(result, list(result))
print(player_stats)
