import re


def match_sofia_phone(input_string: str):
    regex = r"\+359(?P<a1>[ -])2(?P=a1)([0-9]{3})(?P=a1)([0-9]{4})\b"
    numbers = re.compile(regex)
    result_list = list()
    result = re.finditer(numbers, input_string)

    for show in result:
        result_list.append(show[0])

    print(", ".join(result_list))


initial_input = input()
match_sofia_phone(initial_input)
