"""Factorial - loop, recursion, and math module."""
import math


def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def main():
    try:
        n = int(input("Enter a non-negative number: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if n < 0:
        print("Factorial negative number ka nahi hota.")
        return

    print(f"Loop      : {n}! = {factorial_loop(n)}")
    print(f"Recursion : {n}! = {factorial_recursive(n)}")
    print(f"math.factorial : {n}! = {math.factorial(n)}")


if __name__ == "__main__":
    main()