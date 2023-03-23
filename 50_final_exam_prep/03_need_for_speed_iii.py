iterations = int(input())

mileage_info = {}
fuel_info = {}

for _ in range(iterations):
    car, mileage, fuel = input().split("|")
    mileage_info[car] = mileage_info.get(car,0)
    mileage_info[car] = int(mileage)
    fuel_info[car] = fuel_info.get(car,0)
    fuel_info[car] = int(fuel)

line = input()

while line != "Stop":
    data = line.split(" : ")
    command = data[0]

    if command == "Drive":
        car = data[1]
        distance = int(data[2])
        fuel = int(data[3])
        if fuel_info[car] < fuel:
            print(f"Not enough fuel to make that ride")
        else:
            fuel_info[car] -= fuel
            mileage_info[car] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if mileage_info[car] >= 100000:
            del(fuel_info[car])
            del(mileage_info[car])
            print(f"Time to sell the {car}!")

    elif command == "Refuel":
        car = data[1]
        fuel = int(data[2])
        starting_fuel = fuel_info[car]
        if starting_fuel + fuel > 75:
            fuel_info[car] = 75
            print(f"{car} refueled with {75 - starting_fuel} liters")
        else:
            fuel_info[car] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif command == "Revert":
        car = data[1]
        kilometers = int(data[2])
        mileage_info[car] -= kilometers
        if mileage_info[car] < 10000:
            mileage_info[car] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    line = input()

for car in mileage_info:
    print(f"{car} -> Mileage: {mileage_info[car]} kms, Fuel in the tank: {fuel_info[car]} lt.")
