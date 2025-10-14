"""
Python Practice Program

This program demonstrates multiple basic programming concepts:

1. Fibonacci Series:
   - Generates and prints the first n terms of the Fibonacci series.

2. Palindrome Check:
   - Checks whether a given string is a palindrome and prints the result.

3. Patterns:
   - Prints various patterns using stars (*) and numbers:
     1) Right Triangle
     2) Inverted Right Triangle
     3) Pyramid
     4) Inverted Pyramid
     5) Diamond
     6) Number Triangle
     7) Inverted Number Triangle
"""

def fibonacci(n):
    """
    Generates and prints the first n terms of the Fibonacci series.

    Args:
        n (int): Number of terms to generate.

    Returns:
        list: A list containing the first n Fibonacci numbers.

    Prints:
        The generated Fibonacci series.
    """
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    print(f"Fibonacci series ({n} terms): {series}")
    return series


def is_palindrome(s):
    """
    Checks whether a given string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Prints:
        Whether the string is a palindrome or not.
    """
    if s == s[::-1]:
        print(f"{s} is a palindrome")
        return True
    else:
        print(f"{s} is not a palindrome")
        return False


def right_triangle(n):
    """
    Prints a right triangle pattern of stars.

    Args:
        n (int): The number of rows for the triangle.

    Prints:
        A right triangle pattern.
    """
    print("Right Triangle:")
    for i in range(1, n+1):
        print("* " * i)
    print("\n")


def inverted_triangle(n):
    """
    Prints an inverted right triangle pattern of stars.

    Args:
        n (int): The number of rows for the triangle.

    Prints:
        An inverted right triangle pattern.
    """
    print("Inverted Right Triangle:")
    for i in range(n, 0, -1):
        print("* " * i)
    print("\n")


def pyramid(n):
    """
    Prints a pyramid pattern of stars.

    Args:
        n (int): The number of rows for the pyramid.

    Prints:
        A pyramid pattern.
    """
    print("Pyramid Pattern:")
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)
    print("\n")


def inverted_pyramid(n):
    """
    Prints an inverted pyramid pattern of stars.

    Args:
        n (int): The number of rows for the inverted pyramid.

    Prints:
        An inverted pyramid pattern.
    """
    print("Inverted Pyramid Pattern:")
    for i in range(n, 0, -1):
        print(" " * (n-i) + "* " * i)
    print("\n")


def diamond(n):
    """
    Prints a diamond pattern of stars.

    Args:
        n (int): The number of rows for the top half of the diamond.

    Prints:
        A diamond pattern.
    """
    print("Diamond Pattern:")
    # Top pyramid
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)
    # Bottom inverted pyramid
    for i in range(n-1, 0, -1):
        print(" " * (n-i) + "* " * i)
    print("\n")


def number_triangle(n):
    """
    Prints a triangle pattern of numbers.

    Args:
        n (int): The number of rows for the number triangle.

    Prints:
        A number triangle pattern.
    """
    print("Number Triangle:")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    print("\n")


def inverted_number_triangle(n):
    """
    Prints an inverted triangle pattern of numbers.

    Args:
        n (int): The number of rows for the inverted number triangle.

    Prints:
        An inverted number triangle pattern.
    """
    print("Inverted Number Triangle:")
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    print("\n")


# Example Usage
if __name__ == "__main__":
    # Fibonacci
    fibonacci(10)

    # Palindrome
    is_palindrome("radar")
    is_palindrome("hello")

    # Patterns
    n = 5
    right_triangle(n)
    inverted_triangle(n)
    pyramid(n)
    inverted_pyramid(n)
    diamond(n)
    number_triangle(n)
    inverted_number_triangle(n)
