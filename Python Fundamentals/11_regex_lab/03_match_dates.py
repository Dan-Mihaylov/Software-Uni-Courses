import re


def find_matches(initial_string : str):
    regex = r"([0-9]{2})(?P<separator>[/.-])([A-Z]{1}[a-z]{2})(?P=separator)([\d]{4})"
    pattern = re.compile(regex)
    matches = re.findall(pattern, initial_string)
    return matches


input_line = input()
for match in find_matches(input_line):
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
