def calculate_percentage(target, in_hand):
    return in_hand / target * 100


days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_gathered = 0

for day in range(1, days + 1):
    total_gathered += daily_plunder
    if day % 3 == 0:
        total_gathered += (daily_plunder * 0.5)
    if day % 5 == 0:
        total_gathered -= total_gathered * 0.3

if total_gathered >= expected_plunder:
    print(f"Ahoy! {total_gathered:.2f} plunder gained.")
else:
    print(f"Collected only {calculate_percentage(expected_plunder, total_gathered):.2f}% of the plunder.")
    