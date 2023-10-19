language_info = dict()
submission_count = dict()
input_line = input()


def ban_student(name_):
    for language_ in language_info:
        if name_ in language_info[language_]:
            del language_info[language_][name_]
            continue


def enter_submission(student_, language_, grade_):
    language_info[language_] = language_info.get(language_, {})
    language_info[language_][student_] = language_info[language_].get(student_, 0)
    language_info[language_][student_] = max(language_info[language_][student_], grade_)
    submission_count[language_] = submission_count.get(language_, 0)
    submission_count[language_] += 1


while input_line != "exam finished":
    command = input_line.split("-")
    student = command[0]
    if command[1] == "banned":
        ban_student(student)
    else:
        language = command[1]
        grade = int(command[2])
        enter_submission(student, language, grade)

    input_line = input()

print(f"Results:")
for language, student_info in language_info.items():
    for name, grade in student_info.items():
        print(f"{name} | {grade}")
print(f"Submissions:")
for language, submissions in submission_count.items():
    print(f"{language} - {submissions}")
