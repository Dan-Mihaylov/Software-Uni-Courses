item = input()
dictionary = dict()

while item != "stop":
    amount = int(input())
    dictionary[item] = dictionary.get(item, 0)
    dictionary[item] += amount
    item = input()

# The dict[item] = dict.get(item, 0)
# means get this key, if there isnt a key, create it with the default value of 0

for key, value in dictionary.items():
    print(f"{key} -> {value}")

