SUBJECT_COUNT = 3

students = [["Rahul", 78, 88, 92], ["Priya", 65, 71, 69],
            ["Amit", 90, 94, 85], ["Sneha", 55, 60, 58],
            ["Vikram", 82, 79, 88]]


def total_marks(student):
    """Returns the sum of a student's marks."""
    total = 0
    for mark in student[1:]:
        total = total + mark
    return total


def average_marks(student):
    """Returns the average of a student's marks."""
    return total_marks(student) / SUBJECT_COUNT


def get_grade(average):
    """Returns the letter grade for an average."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


print("REPORT")
for student in students:
    total = total_marks(student)
    average = average_marks(student)
    print(f"{student[0]} {total} {average} {get_grade(average)}")

average_sum = 0
for student in students:
    average_sum = average_sum + average_marks(student)
print(f"Class average: {average_sum / len(students)}")

topper_name = ""
topper_average = 0
for student in students:
    average = average_marks(student)
    if average > topper_average:
        topper_average = average
        topper_name = student[0]
print(f"Topper: {topper_name} {topper_average}")