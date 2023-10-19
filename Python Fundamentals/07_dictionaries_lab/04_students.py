"""
students = {}

info = input().split(":")

while len(info) > 1:
    name = info[0]
    idn = int(info[1])
    course = info[2]

# Stores the ids in a key, so its unique every time, even if there are students
    # with same names, they will be under diff id.

    students[idn] = {name: course}

# can use if ":" in info split by it, if "_" in info split by it. It saves me on the for loop to remove "_"

    info = input().split(":")

# There is a case where lectures use _ for input
# I don't know why lecture = info[0]
# lecture.replace("_", " ") didn't work.

lecture = ""
for letter in info[0]:
    if letter.isalpha():
        lecture += letter
    else:
        lecture += " "

# For the key in students
for idn in students:

    # for key in students[key]

    for name in students[idn]:

        if lecture in students[idn][name]:

            print(f"{name} - {idn}")
"""

# SoftUni Solution

students_dict = {}
command = input()
while ":" in command:
    info = command.split(":")
    name, idn, course = info[0], info[1], info[2]
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][idn] = name
    command = input()

course = " ".join(command.split("_"))
for key, value in students_dict.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")

