# import f1  # Imports cause Entire file to run # 1.
from f1 import add  # 2.


def main():
    print("Hello, from f2")
    # print("Sum:", f1.add(10, 100))
    print("Sum:", add(10, 100))


if __name__ == "__main__":
    main()


# Summary
# 1. Import entire file
# 2. Import only the required function or values (Preferred)
