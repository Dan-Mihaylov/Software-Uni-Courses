import re

runners = input().split(", ")
contest_info = dict()


def extract_runner(text: str):
    regex = r"[A-Za-z]+"
    pattern = re.compile(regex)
    matches = re.finditer(pattern, text)
    name = str()
    for match in matches:
        name += match.group()
    if name in runners:
        contest_info[name] = contest_info.get(name, 0)
        contest_info[name] += extract_distance(text)


def extract_distance(text: str):
    regex = r"[0-9]"
    pattern = re.compile(regex)
    matches = re.finditer(pattern, text)
    total_distance = 0
    for match in matches:
        total_distance += int(match.group())
    return total_distance


line = input()
while line != "end of race":
    extract_runner(line)
    line = input()

contest_info = dict(sorted(contest_info.items(), key=lambda x: -x[1]))
place = 1
end = str()
for contestant in contest_info:
    if place == 1:
        end = "st"
    elif place == 2:
        end = "nd"
    elif place == 3:
        end = "rd"
    if place <= 3:
        print(f"{place}{end} place: {contestant}")
        place += 1
