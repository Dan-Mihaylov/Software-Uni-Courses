from collections import deque

green_timer = int(input())
free_timer = int(input())
passed_cars = list()
waiting_cars = deque()
crash = False
command = input()

while command != "END":
    if command != "green":
        waiting_cars.append(command)
    else:
        curr_green_timer = green_timer

        while curr_green_timer > 0 and waiting_cars:

            curr_car = waiting_cars.popleft()

            total_time = curr_green_timer + free_timer
            if len(curr_car) > total_time:
                crash = True
                print(f"A crash happened!")
                print(f"{curr_car} was hit at {curr_car[total_time]}.")
                break

            curr_green_timer -= len(curr_car)
            passed_cars.append(curr_car)
    if crash:
        break
    command = input()

if not crash:
    print("Everyone is safe.")
    print(f"{len(passed_cars)} total cars passed the crossroads.")

