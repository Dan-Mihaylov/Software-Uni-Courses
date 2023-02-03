numbers = input().split()


def split_riders(initial_list):
    left = []
    right = []
    for i in range(len(initial_list)):
        if i < len(numbers) // 2:
            left.append(int(initial_list[i]))
        elif i > len(numbers) // 2:
            right.append(int(initial_list[i]))
    return left, right


def faster_rider(left_list, right_list, *win):
    left_time = 0
    right_time = 0
    right_list.reverse()

    for time in left_list:
        if time != 0:
            left_time += time
        else:
            left_time *= 0.8

    for time in right_list:
        if time != 0:
            right_time += time
        else:
            right_time *= 0.8
        if left_time <= right_time:
            win = "left"
        else:
            win = "right"

    return min(left_time, right_time), win


riders = split_riders(numbers)
left_rider = riders[0]
right_rider = riders[1]
faster_time, winner = faster_rider(left_rider, right_rider)[0], faster_rider(left_rider, right_rider)[1]  # Voodoo magic

print(f"The winner is {winner} with total time: {faster_time:.1f}")
