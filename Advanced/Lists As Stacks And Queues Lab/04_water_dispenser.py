from collections import deque


queue = deque()
water = int(input())

must_end = True
while must_end:
    person = input()
    if person == "Start":
        command = input().split()
        while True:
            if command[0] == "End":
                must_end = False
                break
            if len(command) > 1:        # refill scenario
                liters = int(command[1])
                water += liters
            else:
                liters = int(command[0])
                if water >= liters:
                    water -= liters
                    print(f"{queue.popleft()} got water")
                else:
                    print(f"{queue.popleft()} must wait")
            command = input().split()

    queue.append(person)
print(f"{water} liters left")