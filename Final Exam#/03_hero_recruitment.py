heroes_info = dict()


def enroll(inp_line: str):
    inp_line = inp_line.split()
    hero_name = inp_line[1]
    if hero_name in heroes_info:
        print(f"{hero_name} is already enrolled.")
    else:
        heroes_info[hero_name] = list()


def learn(inp_line: str):
    hero_name, spell_name = inp_line.split()[1], inp_line.split()[2]
    if hero_name not in heroes_info:
        print(f"{hero_name} doesn't exist.")
    elif spell_name in heroes_info[hero_name]:
        print(f"{hero_name} has already learnt {spell_name}.")
    else:
        heroes_info[hero_name].append(spell_name)


def unlearn(inp_line: str):
    hero_name, spell_name = inp_line.split()[1], inp_line.split()[2]
    if hero_name not in heroes_info:
        print(f"{hero_name} doesn't exist.")
    elif spell_name not in heroes_info[hero_name]:
        print(f"{hero_name} doesn't know {spell_name}.")
    else:
        heroes_info[hero_name].remove(spell_name)


command_dict = {"Enroll": enroll,
                "Learn": learn,
                "Unlearn": unlearn
                }

while True:
    line = input()
    if line == "End":
        break
    command_dict[line.split()[0]](line)

print(f"Heroes:")
for hero in heroes_info:
    print(f"== {hero}: {', '.join(heroes_info[hero])}")
