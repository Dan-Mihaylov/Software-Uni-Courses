company_info = dict()

input_line = input()

while input_line != "End":
    company, employee_id = input_line.split(" -> ")
    company_info[company] = company_info.get(company, [])

    if employee_id not in company_info[company]:
        company_info[company].append(employee_id)

    input_line = input()

for company, id_s in company_info.items():
    print(f"{company}")
    for em_id in id_s:
        print(f"-- {em_id}")


