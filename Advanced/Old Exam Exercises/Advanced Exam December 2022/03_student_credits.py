def students_credits(*args):

    credits_needed = 240
    diyans_courses = {}
    result = []
    total_credits = 0

    for arg in args:
        course_name, credits_, max_test_points, diyan_points = arg.split("-")
        credits_for_course = (int(diyan_points) / int(max_test_points)) * int(credits_)
        total_credits += credits_for_course
        diyans_courses[course_name] = credits_for_course

    if total_credits >= credits_needed:
        print(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        print(f"Diyan needs {credits_needed - total_credits:.1f} credits more for a diploma.")

    the_sorted_dict = sorted(diyans_courses.items(), key=lambda x: -x[1])
    for course, cred in the_sorted_dict:
        result.append(f"{course} - {float(cred):.1f}")

    return '\n'.join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)

