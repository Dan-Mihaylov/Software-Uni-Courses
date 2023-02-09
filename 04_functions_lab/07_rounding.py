def rounding(num: float):
    return round(num)


numbers_list = input().split()
rounded_list = []

for n in numbers_list:
    rounded_list.append(rounding(float(n)))

print(rounded_list)

