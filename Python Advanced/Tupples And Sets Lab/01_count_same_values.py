numbers_list = list(map(float, input().split()))

counter_dict = dict()

for item in numbers_list:
    counter_dict[item] = counter_dict.get(item, 0)
    counter_dict[item] += 1

for item, times in counter_dict.items():
    print(f"{item:.1f} - {times} times")
