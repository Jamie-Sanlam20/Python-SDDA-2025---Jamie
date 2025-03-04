# In python
# Function treated as first class citizen (value)


# Rules (for variables)
# 1. Assign to variable
# 2. Pass as argument
# 3. Returned

# Rules (functions)
# 1. Function: Assign to variable
# 2. Function: Pass as argument
# 3. Function: Returned

# 1. Variable: Assign to variable

# x = 1


# # 1. Function: Assign to variable

# def greet(name):
#     return f"Hi, {name}"


# print(type(greet))  # <class 'function'>
# # print(type(greet("Jevan")))

# y = greet  # function

# print(y("Jamie"))  # Hi, Jamie


# 2. Function: Pass as argument


def say_hello():
    return "Hello, "


# # 2. Function: Pass as argument - say_hello (function) is passed as argument
def greeting(hello_msg, name):
    print(
        hello_msg() + name
    )  # hello_msg acts as placeholder to show that function datatype is parsed


greeting(say_hello, "Python!")

# Functional languages - F#, Haskell, Scala - Recursion

# print(say_hello())


# 3. Function: Returned


def f1():
    def f2():
        return "Hi 😀👋"

    return f2  # -> returning function


# Make it print - "Hi 😀👋"
# f1 is returning f2 -> call f1 --> == f2, then () to call function

# Sol 1 -> assign to variable x
x = f1()  # f2
print(x())  # f2()

# Sol 2
print(f1()())  # --> to print Hi

# Summary:
# Rules
# 1. Function: Assign to variable
# 2. Function: Pass as argument
# 3. Function: Returned
