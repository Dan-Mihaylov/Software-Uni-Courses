iterations = int(input())

piece_by_composer = dict()
piece_by_key = dict()

for _ in range(iterations):
    piece, composer, key = input().split("|")
    piece_by_composer[piece] = composer
    piece_by_key[piece] = key

line = input()

while line != "Stop":
    data = line.split("|")
    command = data[0]
    piece = data[1]

    if command == "Add":
        composer = data[2]
        key = data[3]
        if piece in piece_by_composer:
            print(f"{piece} is already in the collection!")
        else:
            piece_by_composer[piece] = composer
            piece_by_key[piece] = key
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == "Remove":
        if piece in piece_by_composer:
            del piece_by_composer[piece]
            del piece_by_key[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = data[2]
        if piece in piece_by_composer:
            piece_by_key[piece] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    line = input()

for piece in piece_by_composer:
    composer = piece_by_composer[piece]
    key = piece_by_key[piece]
    print(f"{piece} -> Composer: {composer}, Key: {key}")

