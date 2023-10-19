from collections import deque

iterations = int(input())
# pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
pumps = deque()
for _ in range(iterations):
    pump_info = [int(x) for x in input().split()]
    pumps.append(pump_info)

for attempt in range(iterations): # will give us on which attempt we got the full circle
    tank = 0
    can_go_around = True
    for fuel, distance in pumps:
        tank += fuel
        if distance > tank:
            can_go_around = False
            break
        else:
            tank -= distance    # if it can cross the distance, we have to remove the fuel from the tank
    if can_go_around:   # If it can go around the whole circle, we finish the program
        print(attempt)
        break
    else:
        pumps.append(pumps.popleft())   # otherwise we take the first pump and put it in the queue



# from collections import deque
#
# total_pumps = int(input())
#
# pumps_info = deque([[int(x) for x in input().split()] for _ in range(total_pumps)])    # 0/ petrol, 1/ distance
#
# for i in range(total_pumps):
#     tank = 0
#     circle = True
#     for pump in pumps_info:
#         petrol = pump[0]
#         distance = pump[1]
#         tank += petrol
#         if tank < distance:
#             pumps_info.append(pumps_info.popleft())
#             circle = False
#             break
#         else:
#             tank -= distance
#     if circle:
#         print(i)
#         break
