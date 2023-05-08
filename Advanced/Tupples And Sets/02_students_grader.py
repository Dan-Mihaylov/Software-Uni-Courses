iterations = int(input())

students_info = dict()

for _ in range(iterations):
    info = input().split()
    name = info[0]
    grade = float(info[1])
    students_info[name] = students_info.get(name, [])
    students_info[name].append(grade)
a = 1
for student, grades in students_info.items():
    average = sum(grades) / len(grades)
    print(f"{student} -> ", end="")
    [print(f"{x:.2f}", end=" ") for x in grades]
    print(f"(avg: {average:.2f})")

