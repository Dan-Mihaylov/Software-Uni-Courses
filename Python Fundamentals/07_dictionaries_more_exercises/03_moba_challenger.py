tier_info = dict()
# will be a nested dictionary again
command = input()


def add_player(player_, position_, skill_):
    tier_info[player_] = tier_info.get(player_, {})
    tier_info[player_][position_] = tier_info[player_].get(position_, 0)
    tier_info[player_][position_] = max(tier_info[player_][position_], skill_)


def battle(pl_one, pl_two):
    if pl_one in tier_info and pl_two in tier_info:
        can_fight = False
        pos = ""
        for position in tier_info[pl_one]:
            if position in tier_info[pl_two]:
                can_fight = True
                pos = position
                break
        if can_fight:
            if tier_info[pl_one][pos] > tier_info[pl_two][pos]:
                del tier_info[pl_two]
            elif tier_info[pl_two][pos] > tier_info[pl_one][pos]:
                del tier_info[pl_one]


while command != "Season end":
    if " -> " in command:
        command = command.split(" -> ")
        pl_name, pl_position, pl_skill = command[0], command[1], int(command[2])
        add_player(pl_name, pl_position, pl_skill)

    elif " vs " in command:
        command = command.split(" vs ")
        player_one, player_two = command[0], command[1]
        battle(player_one, player_two)

    command = input()

players_total_skill = dict()

for plr, role in tier_info.items():
    for sk in role.values():
        players_total_skill[plr] = players_total_skill.get(plr, 0)
        players_total_skill[plr] += sk

players_total_skill = dict(sorted(players_total_skill.items(), key=lambda x: -x[1]))
# sorting the first dict to be displayed by players skills
for key, value in tier_info.items():
    tier_info[key] = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))

for player, total_points in players_total_skill.items():
    print(f"{player}: {total_points} skill")
    for pos, points in tier_info[player].items():
        print(f"- {pos} <::> {points}")
