# variable_name = value
name = "Jamie"
age = 24
balance = 10000000.50
is_rich = True

# print(name)
# print(age)
# print(balance)

# Dynamically typed --> Python smart
# means it will pick up what the datatype is based on the value

print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(balance))  # <class 'float'>
print(type(is_rich))  # <class 'bool'>

print("My name is " + name)

# str + int (mixing datatypes) --> ❌

# print("My age is " + age)
# Type conversions
# str, int, float

# print("My age is " + str(age))

# You can also use fstring to concatenate
# Fstring auto converts for us (we wont have to do conversions)
# {} -> interpolation (substitution) --> avoid str() conversions

print(f"my age is {age}")

# {} -> expressions are allowed in interpolation
# print(f"She has {2 * 1000} followers")

name = input("Enter your name: ")
print(f"Hi, {name}")
