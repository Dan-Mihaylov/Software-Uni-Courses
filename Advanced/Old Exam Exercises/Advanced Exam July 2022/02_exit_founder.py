from collections import deque


SIZE = 6
turns = deque(input().split(", "))

maze = [[x for x in input().split()] for _ in range(SIZE)]

tom_rest = False
jerry_rest = False

while True:

    player = turns.popleft()
    turns.append(player)
    info = input()
    coordinates = tuple(map(lambda x: int(x), filter(lambda x: x.isnumeric(), info)))
    row, col = coordinates

    if (player == "Tom" and tom_rest) or (player == "Jerry" and jerry_rest):
        if player == "Tom":
            tom_rest = False
        else:
            jerry_rest = False
        continue

    if maze[row][col] == "E":
        print(f"{player} found the Exit and wins the game!")
        break

    elif maze[row][col] == "T":
        winner = turns.popleft()
        print(f"{player} is out of the game! The winner is {winner}.")
        break

    elif maze[row][col] == "W":

        if player == "Tom":
            tom_rest = True
        else:
            jerry_rest = True

        print(f"{player} hits a wall and needs to rest.")






