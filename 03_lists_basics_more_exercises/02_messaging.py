first_input = input().split()
second_input = input()
second_list = [*second_input]
final_message = []

remove_index = []
for number in first_input:
    sum_index = [int(x) for x in number]
    remove_index.append(sum(sum_index))
for i in range(len(remove_index)):
    if remove_index[i] > len(second_list) - 1:
        remove_index[i] = remove_index[i] - len(second_list)
    final_message.append(second_list.pop(remove_index[i]))

print(f"".join(final_message))
