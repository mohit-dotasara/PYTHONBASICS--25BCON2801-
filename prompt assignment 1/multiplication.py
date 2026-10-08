"""Multiplication table generator."""


def print_table(number, limit=10):
    print(f"\nMultiplication table of {number}")
    print("-" * 28)
    for i in range(1, limit + 1):
        print(f"{number} x {i:>2} = {number * i}")


def print_full_grid(size=10):
    """Full 1..size multiplication grid."""
    print("\nFull grid:")
    for i in range(1, size + 1):
        print(" ".join(f"{i * j:>4}" for j in range(1, size + 1)))


def main():
    try:
        number = int(input("Enter a number: "))
        limit = int(input("Up to (default 10): ") or 10)
    except ValueError:
        print("Please enter valid integers.")
        return

    print_table(number, limit)
    print_full_grid()


if __name__ == "__main__":
    main()