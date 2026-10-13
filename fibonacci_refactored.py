"""Fibonacci series - loop, recursion, and generator."""

FIBONACCI_FIRST_TERM = 0
FIBONACCI_SECOND_TERM = 1
RECURSION_BASE_INDEX = 1


def fibonacci_loop(term_count):
    """Return a list of the first term_count Fibonacci numbers, using a loop."""
    series = []
    previous_term, current_term = FIBONACCI_FIRST_TERM, FIBONACCI_SECOND_TERM
    for _ in range(term_count):
        series.append(previous_term)
        previous_term, current_term = current_term, previous_term + current_term
    return series


def fibonacci_recursive(term_index):
    """Return the Fibonacci number at term_index (0-indexed), using recursion."""
    if term_index <= RECURSION_BASE_INDEX:
        return term_index
    return fibonacci_recursive(term_index - 1) + fibonacci_recursive(term_index - 2)


def fibonacci_generator(term_count):
    """Return a memory-efficient generator of the first term_count Fibonacci numbers."""
    previous_term, current_term = FIBONACCI_FIRST_TERM, FIBONACCI_SECOND_TERM
    for _ in range(term_count):
        yield previous_term
        previous_term, current_term = current_term, previous_term + current_term


def main():
    """Run the prompt-and-print flow and return None."""
    try:
        term_count = int(input("How many terms? "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if term_count <= 0:
        print("Number positive hona chahiye.")
        return

    print(f"Loop      : {fibonacci_loop(term_count)}")
    print(f"Recursion : {[fibonacci_recursive(term_index) for term_index in range(term_count)]}")
    print(f"Generator : {list(fibonacci_generator(term_count))}")


if __name__ == "__main__":
    main()