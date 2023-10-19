from collections import deque


programmers_times = deque([int(x) for x in input().split()])
tasks = deque([int(x) for x in input().split()])

# Will iterate over the key value pairs and check the ranges, if it is in range, add the key, to got rew.
# on index 2 will always have the count will append 1

rewards = {
    "Darth Vader Ducky": (0, 60, []),
    "Thor Ducky": (61, 120, []),
    "Big Blue Rubber Ducky": (121, 180, []),
    "Small Yellow Rubber Ducky": (181, 240, []),
}

while programmers_times and tasks:
    curr_time = programmers_times.popleft()
    curr_task = tasks.pop()
    res = curr_time * curr_task

    for key, value in rewards.items():
        start_range = value[0]
        end_range = value[1]

        if res in range(start_range, end_range + 1):
            rewards[key][2].append(1)
            break

    else:
        tasks.append(curr_task - 2)
        programmers_times.append(curr_time)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for reward, values in rewards.items():
    print(f"{reward}: {len(values[2])}")
