iterations = int(input())

vip_guests = set()
regular_guests = set()

for _ in range(iterations):
    reservation = input()
    if reservation[0].isnumeric():
        vip_guests.add(reservation)
    else:
        regular_guests.add(reservation)

command = input()

while command != "END":
    if command in vip_guests:
        vip_guests.remove(command)
    elif command in regular_guests:
        regular_guests.remove(command)
    command = input()

print(len(vip_guests) + len(regular_guests))
[print(guest) for guest in sorted(vip_guests)]
[print(guest) for guest in sorted(regular_guests)]
