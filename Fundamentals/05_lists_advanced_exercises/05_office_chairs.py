iterations = int(input())

free_chairs = 0
room_number = 1
enough = True
for _ in range(iterations):
    initial_input = input().split()
    chairs = len(initial_input[0])
    people = int(initial_input[1])
    if chairs >= people:
        free_chairs += abs(chairs - people)
    else:
        needed_chairs = abs(chairs - people)
        print(f"{needed_chairs} more chairs needed in room {room_number}")
        enough = False
    room_number += 1
if enough:
    print(f"Game On, {free_chairs} free chairs left")
