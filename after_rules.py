def count_above_average(data):
    """Returns how many students scored above the class average."""
    class_average = sum(calc_average(record) for record in data) / len(data)
    students_above_average = 0
    for record in data:
        if calc_average(record) > class_average:
            students_above_average = students_above_average + 1
    return students_above_average