import re

iterations = int(input())

pattern = re.compile(r"(.+)>(?P<num>[0-9]{3})\|(?P<low>[a-z]{3})\|(?P<up>[A-Z]{3})\|(?P<sym>[^<>]{3})<\1")

for _ in range(iterations):
    password = input()
    matches = re.finditer(pattern, password)
    decrypted = str()
    for match in matches:
        one = match["num"]
        two = match["low"]
        three = match["up"]
        four = match["sym"]
        decrypted += one + two + three + four

    if len(decrypted) > 1:
        print(f"Password: {decrypted}")
    else:
        print(f"Try another password!")
