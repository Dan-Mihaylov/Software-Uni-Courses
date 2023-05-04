from math import ceil

students_count = int(input())
total_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
lectures_attended = 0

for _ in range(students_count):
    attendances = int(input())
    total_bonus = attendances / total_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        lectures_attended = attendances

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {lectures_attended} lectures.")
