from collections import deque

name = input()
customers = deque()

while name != "End":
    if name == "Paid":
        while customers:
            print(customers.popleft())
        name = input()
        continue

    customers.append(name)
    name = input()

print(f"{len(customers)} people remaining.")
