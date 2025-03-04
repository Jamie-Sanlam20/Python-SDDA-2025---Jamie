def add(t1, t2):
    return t1 + t2


# Good practice
def main():
    print("Hello, from f1")
    print(__name__)


if __name__ == "__main__":
    main()

# Good practice, if you're putting something under an if statement, put it under:
# Create a main function, then call it if __name__ == __main__
