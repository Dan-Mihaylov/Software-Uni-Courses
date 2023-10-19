import re


def match_full_name(names: str):
    regex = r"\b([A-Z]{1}[a-z]{1,}) ([A-Z]{1}[a-z]{1,})\b"
    matches = re.findall(regex, names)
    return matches


test_string = input()
print(" ".join([name for match in match_full_name(test_string) for name in match]))


# Soft Uni solution, not working

# names = input()
# regex = r"\b([A-Z]{1}[a-z]{1,}) ([A-Z]{1}[a-z]{1,})\b"
# matches = re.findall(regex, names)
# print(" ".join(matches))
