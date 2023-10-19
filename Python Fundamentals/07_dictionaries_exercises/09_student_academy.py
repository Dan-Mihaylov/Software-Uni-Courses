students_info = dict()

iterations = int(input())

for _ in range(iterations):
    student = input()
    grade = float(input())

    students_info[student] = students_info.get(student, [])
    students_info[student].append(grade)

for name, grades in students_info.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
