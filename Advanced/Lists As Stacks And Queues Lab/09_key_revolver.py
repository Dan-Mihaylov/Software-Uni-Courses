from collections import deque

bullet_price = int(input())
size_gun_barrel = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
bullets_shot = 0

# bullets back to front
# locks front to back
# if finishing bullets print reloading in barrel
curr_mag = size_gun_barrel
while bullets and locks:
    curr_mag -= 1
    curr_bullet = bullets.pop()
    bullets_shot += 1
    curr_lock = locks.popleft()
    if curr_bullet <= curr_lock:
        print(f"Bang!")
    else:
        print(f"Ping!")
        locks.appendleft(curr_lock)
    if curr_mag == 0 and bullets:
        print(f"Reloading!")
        curr_mag = size_gun_barrel

bullets_cost = bullets_shot * bullet_price
money_earned = intelligence_value - bullets_cost

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

