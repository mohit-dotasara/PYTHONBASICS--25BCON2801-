"""Factorial - loop, recursion, and math module."""
import math


def factorial_loop(n):
    # Method 1: multiply numbers from 2 to n using a loop
    result = 1  # start at 1 because 0! and 1! are both 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    # Method 2: function calls itself with a smaller number
    if n <= 1:  # base case: stops the recursion
        return 1
    return n * factorial_recursive(n - 1)


def main():
    # Ask the user for a number and make sure it is an integer
    try:
        n = int(input("Enter a non-negative number: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Factorial is not defined for negative numbers
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return

    # Print the result from all three methods to compare them
    print(f"Loop           : {n}! = {factorial_loop(n)}")
    print(f"Recursion      : {n}! = {factorial_recursive(n)}")
    print(f"math.factorial : {n}! = {math.factorial(n)}")


if __name__ == "__main__":
    main()