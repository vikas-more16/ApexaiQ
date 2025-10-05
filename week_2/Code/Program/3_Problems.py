

# Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    print(f"Fibonacci series ({n} terms): {series}")
fibonacci(10)

# Palindrome
def is_palindrome(s):
    if s == s[::-1]:
        print(f"{s} is a palindrome")
        return True
    else:
        print(f"{s} is not a palindrome")
        return False
is_palindrome("radar")
is_palindrome("hello")

# Patterns 
# 1) Right Triangle Pattern
def right_triangle(n):
    print("Right Triangle:")
    for i in range(1, n+1):
        print("* " * i)
    print("\n")

# 2) Inverted Right Triangle Pattern
def inverted_triangle(n):
    print("Inverted Right Triangle:")
    for i in range(n, 0, -1):
        print("* " * i)
    print("\n")

# 3) Pyramid Pattern
def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)
    print("\n")

# 4) Inverted Pyramid Pattern
def inverted_pyramid(n):
    print("Inverted Pyramid Pattern:")
    for i in range(n, 0, -1):
        print(" " * (n-i) + "* " * i)
    print("\n")

# 5) Diamond Pattern
def diamond(n):
    print("Diamond Pattern:")
    # Top pyramid
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)
    # Bottom inverted pyramid
    for i in range(n-1, 0, -1):
        print(" " * (n-i) + "* " * i)
    print("\n")

# 6) Number Triangle Pattern
def number_triangle(n):
    print("Number Triangle:")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    print("\n")

# 7) Inverted Number Triangle
def inverted_number_triangle(n):
    print("Inverted Number Triangle:")
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    print("\n")

# Run all patterns
n = 5
right_triangle(n)
inverted_triangle(n)
pyramid(n)
inverted_pyramid(n)
diamond(n)
number_triangle(n)
inverted_number_triangle(n)



