"""List operations in Python - basic to useful."""

def main():
    fruits = ["apple", "banana", "mango"]
    print("Original:", fruits)

    # Add items
    fruits.append("orange")          # end me add
    fruits.insert(1, "grapes")       # index 1 pe add
    fruits.extend(["kiwi", "papaya"])
    print("After adding:", fruits)

    # Remove items
    fruits.remove("banana")          # value se remove
    last = fruits.pop()              # last item nikalo
    print("Popped:", last)
    print("After removing:", fruits)

    # Access & slicing
    print("First:", fruits[0])
    print("Last:", fruits[-1])
    print("First 3:", fruits[:3])
    print("Reversed:", fruits[::-1])

    # Sort
    numbers = [5, 2, 9, 1, 7]
    numbers.sort()
    print("Ascending:", numbers)
    numbers.sort(reverse=True)
    print("Descending:", numbers)

    # Loop
    for index, fruit in enumerate(fruits, start=1):
        print(f"{index}. {fruit}")

    # List comprehension
    squares = [n ** 2 for n in range(1, 6)]
    evens = [n for n in range(1, 11) if n % 2 == 0]
    print("Squares:", squares)
    print("Evens:", evens)

    # Useful built-ins
    print("Length:", len(numbers))
    print("Sum:", sum(numbers))
    print("Max:", max(numbers), "| Min:", min(numbers))


if __name__ == "__main__":
    main()