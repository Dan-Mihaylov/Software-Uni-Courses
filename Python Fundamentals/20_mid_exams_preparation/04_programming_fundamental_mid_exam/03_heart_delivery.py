def give_hearts(some_list, current_idx, jumped):
    next_index = current_idx + jumped
    if next_index not in range(len(some_list)):
        next_index = 0
    if some_list[next_index] == 0:
        print(f"Place {next_index} already had Valentine's day.")
    else:
        some_list[next_index] -= 2
        if some_list[next_index] == 0:
            print(f"Place {next_index} has Valentine's day.")
    return some_list, next_index


neighbourhood = [int(x) for x in input().split("@")]

curr_index = 0   # He always starts at 0 house.

while True:
    line = input()
    if line == "Love!":
        break
    jump = int(line.split()[1])

    neighbourhood, curr_index = give_hearts(neighbourhood, curr_index, jump)

print(f"Cupid's last position was {curr_index}.")
if neighbourhood.count(0) == len(neighbourhood):
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(neighbourhood) - neighbourhood.count(0)} places.")
