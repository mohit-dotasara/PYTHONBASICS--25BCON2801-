NUM_SUBJECTS = 3

class_data = [["Rahul", 78, 88, 92], ["Priya", 65, 71, 69],
              ["Amit", 90, 94, 85], ["Sneha", 55, 60, 58],
              ["Vikram", 82, 79, 88]]


def calc_total(record):
    """Returns the total of all subject marks in a record."""
    marks_sum = 0
    for score in record[1:]:
        marks_sum = marks_sum + score
    return marks_sum


def calc_average(record):
    """Returns the average marks for a record."""
    return calc_total(record) / NUM_SUBJECTS


def assign_grade(avg):
    """Returns the letter grade for an average."""
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"


print("REPORT")
for record in class_data:
    total_score = calc_total(record)
    avg_score = calc_average(record)
    print(f"{record[0]} {total_score} {avg_score} {assign_grade(avg_score)}")

all_averages_sum = 0
for record in class_data:
    all_averages_sum = all_averages_sum + calc_average(record)
print(f"Class average: {all_averages_sum / len(class_data)}")

best_name = ""
best_average = 0
for record in class_data:
    avg_score = calc_average(record)
    if avg_score > best_average:
        best_average = avg_score
        best_name = record[0]
print(f"Topper: {best_name} {best_average}")
