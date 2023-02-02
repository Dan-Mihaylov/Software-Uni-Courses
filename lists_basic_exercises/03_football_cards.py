info = input().split()

total_a_players = 11
total_b_players = 11

players_received_cards = []
terminated = False

for player in info:
    if player not in players_received_cards:
        players_received_cards.append(player)

        if player.startswith("A"):
            total_a_players -= 1
        elif player.startswith("B"):
            total_b_players -= 1

    if total_a_players < 7 or total_b_players < 7:
        terminated = True
        break

print(f"Team A - {total_a_players}; Team B - {total_b_players}")

if terminated:
    print(f"Game was terminated")

