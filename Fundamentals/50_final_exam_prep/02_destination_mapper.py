import re

line = input()

places = list()
travel_points = 0

regex = r"([=/])(?P<place>[A-Z][A-Za-z]{2,})\1"
pattern = re.compile(regex)
matches = re.finditer(pattern, line)

for match in matches:
    place = match["place"]
    travel_points += len(place)
    places.append(place)

print(f"Destinations: {', '.join(places)}")
print(f"Travel Points: {travel_points}")
