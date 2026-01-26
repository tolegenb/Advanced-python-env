import json

with open("students.json.txt", "r", encoding="utf-8") as file:
    students = json.load(file)

new_students = []

for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    new_student = student.copy()
    new_student["average_grade"] = round(avg, 2)
    new_students.append(new_student)

with open("students_with_average.json", "w", encoding="utf-8") as file:
    json.dump(new_students, file, indent=2)
