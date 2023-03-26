number_of_plants = int(input())

plants_info = {}

for plant in range(number_of_plants):
    plant_name, rarity = input().split("<->")
    plants_info[plant_name] = [rarity, []]


def check_plant_exist(plant):
    if plant in plants_info:
        return True
    print("error")


def rate(info):
    plant, rating = info.split(" - ")
    plants_info[plant][1].append(int(rating))


def update(info):
    plant, new_rarity = info.split(" - ")
    plants_info[plant][0] = new_rarity


def reset(info):
    plant = info
    plants_info[plant][1] = []


def show_result():
    print("Plants for the exhibition:")
    for plant in plants_info:
        average_rating = 0
        if sum(plants_info[plant][1]) != 0:
            average_rating = sum(plants_info[plant][1]) / len(plants_info[plant][1])
        print(f"- {plant}; Rarity: {plants_info[plant][0]}; Rating: {average_rating:.2f}")


command_func = {
    "Rate": rate,
    "Update": update,
    "Reset": reset
}

command = input()
while command != "Exhibition":
    command_type, info = command.split(": ")
    if check_plant_exist(info.split(" - ")[0]):
        command_func[command_type](info)
    command = input()

show_result()