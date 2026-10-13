"""Fibonacci series - loop, recursion, and generator."""


def fibonacci_loop(n):
    """First n Fibonacci numbers using a loop."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def fibonacci_recursive(n):
    """nth Fibonacci number (0-indexed) using recursion."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_generator(n):
    """Memory-efficient version using a generator."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    try:
        n = int(input("How many terms? "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if n <= 0:
        print("Number positive hona chahiye.")
        return

    print("Loop      :", fibonacci_loop(n))
    print("Recursion :", [fibonacci_recursive(i) for i in range(n)])
    print("Generator :", list(fibonacci_generator(n)))


if __name__ == "__main__":
    main()