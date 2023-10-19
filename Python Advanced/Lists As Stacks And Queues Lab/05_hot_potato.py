from collections import deque


# queue = deque(input().split())
# n = int(input())
# count = 0
#
# while len(queue) != 1:
#     count += 1
#     if count == n:
#         print(f"Removed {queue.popleft()}")
#         count = 0
#     else:
#         person = queue.popleft()
#         queue.append(person)
#
# print(f"Last is {queue.popleft()}")

players = deque(input().split())
rotations = int(input()) -1 # minus one, because the last rotation, the guy burns

while len(players) > 1:
    players.rotate(-rotations)
    print(f"Removed {players.popleft()}")

print(f"Last is {players.popleft()}")

