events = input().split("|")
total_coins = 100
total_energy = 100
still_open = True

for event in events:
    event_items = event.split("-")
    type_event = event_items[0]
    event_value = int(event_items[1])

    if type_event == "rest":
        temp_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
            gained_energy = 100 - temp_energy
            print(f"You gained {gained_energy} energy.")
        else:
            print(f"You gained {event_value} energy.")
        print(f"Current energy: {total_energy}.")

    elif type_event == "order":

        if total_energy >= 30:
            total_coins += event_value
            total_energy -= 30
            print(f"You earned {event_value} coins.")

        else:
            total_energy += 50
            if total_energy > 100:
                total_energy = 100
            print(f"You had to rest!")

    else:
        product = type_event
        price = event_value

        if price <= total_coins:
            total_coins -= price
            print(f"You bought {product}.")

        else:
            print(f"Closed! Cannot afford {product}.")
            still_open = False
            break

if still_open:
    print(f"Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")


