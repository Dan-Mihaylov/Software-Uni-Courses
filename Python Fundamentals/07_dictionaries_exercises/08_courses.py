courses_info = dict()

input_line = input().split(" : ")

while len(input_line) > 1:
    course = input_line[0]
    student = input_line[1]
    courses_info[course] = courses_info.get(course, [])
    courses_info[course].append(student)

    input_line = input().split(" : ")

for course in courses_info.keys():
    total_students = len(courses_info[course])
    print(f"{course}: {total_students}")
    for student in courses_info[course]:
        print(f"-- {student}")


