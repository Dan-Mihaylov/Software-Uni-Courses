initial_deck = input().split()
shuffles = int(input())

for _ in range(shuffles):
    shuffled_deck = []
    left_deck = initial_deck[:len(initial_deck) // 2]
    right_deck = initial_deck[len(initial_deck) // 2:]

    for index in range(len(initial_deck) // 2):
        shuffled_deck.append(left_deck[index])
        shuffled_deck.append(right_deck[index])
        initial_deck = shuffled_deck

print(initial_deck)
