
lines = int(input())

bracket = {
    "current": "(",
    "false": ")",
    "next": ")"
}
balanced = True


for _ in range(lines):
    curr_input = input()

    if curr_input in bracket["current"]:

        bracket["false"] = bracket["current"]
        bracket["current"] = bracket["next"]
        bracket["next"] = "("

    elif curr_input in bracket["false"]:
        balanced = False

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
