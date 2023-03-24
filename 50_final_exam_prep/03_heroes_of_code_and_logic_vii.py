iterations = int(input())

heroes_hp = dict()
heroes_mp = dict()

# TODO? Max 100 hp, Max 200 mp

for _ in range(iterations):
    name, hp, mp = input().split()
    heroes_hp[name] = heroes_hp.get(name, 0)
    heroes_hp[name] = int(hp)
    heroes_mp[name] = heroes_mp.get(name, 0)
    heroes_mp[name] = int(mp)

line = input()

while line != "End":
    data = line.split(" - ")
    command = data[0]

    if command == "CastSpell":
        name = data[1]
        mp_needed = int(data[2])
        spell_name = data[3]

        if heroes_mp[name] >= mp_needed:
            heroes_mp[name] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes_mp[name]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        name = data[1]
        damage = int(data[2])
        attacker = data[3]
        heroes_hp[name] -= damage
        if heroes_hp[name] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_hp[name]} HP left!")
        else:
            del heroes_hp[name]
            del heroes_mp[name]
            print(f"{name} has been killed by {attacker}!")

    elif command == "Recharge":
        name = data[1]
        amount = int(data[2])
        temp_mp = heroes_mp[name]
        heroes_mp[name] += amount
        if heroes_mp[name] > 200:
            heroes_mp[name] = 200
            print(f"{name} recharged for {200 - temp_mp} MP!")
        else:
            print(f"{name} recharged for {amount} MP!")

    elif command == "Heal":
        name = data[1]
        amount = int(data[2])
        temp_hp = heroes_hp[name]
        heroes_hp[name] += amount
        if heroes_hp[name] > 100:
            heroes_hp[name] = 100
            print(f"{name} healed for {100 - temp_hp} HP!")
        else:
            print(f"{name} healed for {amount} HP!")

    line = input()

for hero, hp in heroes_hp.items():
    print(hero)
    print(f"  HP: {hp}")
    print(f"  MP: {heroes_mp[hero]}")
