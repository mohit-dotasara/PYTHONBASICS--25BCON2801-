"""Factorial - loop, recursion, and math module."""
import math

FACTORIAL_OF_ZERO_AND_ONE = 1


def factorial_loop(number):
    """Return the factorial of number, computed with a loop."""
    # Method 1: multiply numbers from 2 to number using a loop
    result = FACTORIAL_OF_ZERO_AND_ONE  # 0! and 1! are both 1
    for factor in range(2, number + 1):
        result *= factor
    return result


def factorial_recursive(number):
    """Return the factorial of number, computed with recursion."""
    # Method 2: function calls itself with a smaller number
    if number <= FACTORIAL_OF_ZERO_AND_ONE:  # base case: stops the recursion
        return FACTORIAL_OF_ZERO_AND_ONE
    return number * factorial_recursive(number - 1)


def main():
    """Run the prompt-and-print flow and return None."""
    # Ask the user for a number and make sure it is an integer
    try:
        user_number = int(input("Enter a non-negative number: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Factorial is not defined for negative numbers
    if user_number < 0:
        print("Factorial is not defined for negative numbers.")
        return

    # Print the result from all three methods to compare them
    print(f"Loop           : {user_number}! = {factorial_loop(user_number)}")
    print(f"Recursion      : {user_number}! = {factorial_recursive(user_number)}")
    print(f"math.factorial : {user_number}! = {math.factorial(user_number)}")


if __name__ == "__main__":
    main()