def f1():
    def f2():
        return "Hi 😀👋"

    return f2  # -> returning function


# f1 is returning f2 -> call f1 --> == f2, then () to call function


print(f1()())  # --> to print Hi
