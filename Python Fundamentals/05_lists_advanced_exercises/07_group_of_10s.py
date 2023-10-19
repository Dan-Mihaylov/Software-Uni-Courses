initial_list = input().split(", ")
integer_list = [int(x) for x in initial_list]
group_lower_boundary = 0
group_up_boundary = 10

while True:
    group_list = list(filter((lambda x: group_lower_boundary < x <= group_up_boundary), integer_list))
    print(f"Group of {group_up_boundary}'s: {group_list}")
    if max(integer_list) <= group_up_boundary:
        break
    group_up_boundary += 10
    group_lower_boundary += 10

    