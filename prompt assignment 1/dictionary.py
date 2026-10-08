"""Dictionary operations in Python."""

def main():
    student = {
        "name": "Mohit",
        "branch": "AI & DS",
        "year": 2,
    }
    print("Original:", student)

    # Access
    print("Name:", student["name"])
    print("City (safe get):", student.get("city", "Not found"))

    # Add / update
    student["city"] = "Jaipur"
    student.update({"year": 3, "college": "JECRC"})
    print("After add/update:", student)

    # Delete
    removed = student.pop("college")
    print("Removed:", removed)
    del student["city"]
    print("After delete:", student)

    # Loop
    for key, value in student.items():
        print(f"{key} -> {value}")

    print("Keys:", list(student.keys()))
    print("Values:", list(student.values()))

    # Check key
    if "branch" in student:
        print("Branch exists")

    # Dict comprehension
    squares = {n: n ** 2 for n in range(1, 6)}
    print("Squares:", squares)

    # Word count (real-world use)
    text = "python is easy python is fun"
    count = {}
    for word in text.split():
        count[word] = count.get(word, 0) + 1
    print("Word count:", count)


if __name__ == "__main__":
    main()