from collections import deque

daily_food_supply = deque([int(x) for x in input().split(", ")])    # last portion
daily_stamina = deque([int(x) for x in input().split(", ")])    # first stamina

mountain_peaks ={
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70,
}

climbed_peaks = []

while daily_food_supply and daily_stamina and mountain_peaks:
    food = daily_food_supply.pop()
    stamina = daily_stamina.popleft()

    for peak in mountain_peaks:
        if mountain_peaks[peak] <= food + stamina:
            mountain_peaks.pop(peak)
            climbed_peaks.append(peak)
            break
        else:
            break

if not mountain_peaks:
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if climbed_peaks:
    print(f"Conquered peaks:")
    [print(*climbed_peaks, sep="\n")]
