text_input = input().split()

filtered_list = [x for x in text_input if len(x) % 2 == 0]
print("\n".join(filtered_list))
