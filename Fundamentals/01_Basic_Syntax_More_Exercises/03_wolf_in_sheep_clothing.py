animals = input()

animal_list = animals.split()
animal_list.reverse() # now you can call the sheep with its index number

if animal_list[0] == "sheep":
    wolf_position = animal_list.index("wolf,")
    print(f"Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!")
else:
    print(f"Please go away and stop eating my sheep")
