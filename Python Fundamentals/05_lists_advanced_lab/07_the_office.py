employees_happiness = input().split()
employees_happiness= [int(x) for x in employees_happiness]
improvement_factor = int(input())

employees_improved = list(map(lambda x: x * improvement_factor, employees_happiness))

filtered_list = list(filter(lambda x: x > sum(employees_improved) / len(employees_happiness), employees_improved))

if len(filtered_list) >= len(employees_happiness) / 2:
    print(f"Score: {len(filtered_list)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_list)}/{len(employees_happiness)}. Employees are not happy!")

