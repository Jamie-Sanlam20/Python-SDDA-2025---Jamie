# from cool import to_upper_case

# # from file name import function name

# print(to_upper_case("Siya"))

# # it's reprinting Jamie -> print statement from cool file is running also

from cool import to_upper_case


def powerful(n):
    """Squares given number

    Args:
        n (int): provide number

    Returns:
        int: square of the value
    """
    return n * n


print(powerful(5))

print(__name__)  # fun | __main__


def main():
    print(to_upper_case("Siya"))


if __name__ == "__main__":
    main()
