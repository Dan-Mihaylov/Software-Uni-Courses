iterations = int(input())

parked = set()

for _ in range(iterations):
    info = tuple(input().split(", "))
    goes = info[0]
    reg = info[1]
    if goes == "IN":
        if reg in parked:
            pass
        else:
            parked.add(reg)
    else:
        if reg in parked:
            parked.remove(reg)
        else:
            pass
        
[print(reg) for reg in parked] if parked else print("Parking Lot is Empty")
