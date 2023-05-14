from collections import deque

total_food = int(input())

orders = deque(int(x) for x in input().split())
biggest_order = max(orders)
while orders:
    if total_food >= orders[0]:
        curr_order = orders.popleft()
        total_food -= curr_order

    else:
        break

print(biggest_order)
if orders:
    print(f"Orders left:", end=" ")
    for _ in range(len(orders)):
        print(f"{orders.popleft()}", end=" ")
else:
    print(f"Orders complete")
