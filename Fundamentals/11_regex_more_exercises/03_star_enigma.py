import re

num_lines = int(input())
decrypted_lines = list()

for _ in range(num_lines):
    line = input()
    line_up = line.upper()
    key = 0
    for char in "STAR":
        key += line_up.count(char)
    decrypt = str()
    for char in line:
        decrypt += chr(ord(char) - key)
    decrypted_lines.append(decrypt)

# escape every character in the separation group

regex = r"@(?P<name>[A-Z-a-z]+)([^\@\!\-\:\>]*):(?P<pop>[0-9]+)([^\@\!\-\:\>]*)\!" \
        r"(?P<att>[AD])\!([^\@\!\-\:\>]*)->(?P<sol>[0-9]+)"

# pattern = re.compile(r"@(?P<name>[A-Za-z]+)([^\@\-\!\:\>]*)"
#                      r":(?P<pop>[0-9]+)([^\@\-\!\:\>]*)"
#                      r"(\!)(?P<att>[AD])\5([^\@\-\!\:\>]*)"
#                      r"->(?P<sol>[0-9]+)")
pattern = re.compile(regex)

attacked_planets = list()
destroyed_planets = list()

for line in decrypted_lines:
    matches = re.finditer(pattern, line)

    for match in matches:
        if match["att"]:
            if match["att"] == "A":
                attacked_planets.append(match["name"])
            else:
                destroyed_planets.append(match["name"])

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets, key= lambda x: x):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets, key=lambda x: x):
    print(f"-> {planet}")
