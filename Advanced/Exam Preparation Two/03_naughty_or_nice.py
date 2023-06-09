def naughty_or_nice_list(kids_info: list, *args, **kwargs):
    santa_list = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }

    for arg in args:
        num, which_list = arg.split("-")
        num = int(num)

        found_kids = list(filter(lambda x: x[0] == num, kids_info))
        if len(found_kids) == 1:
            kid_info = found_kids.pop()
            kids_info = list(filter(lambda x: x != kid_info, kids_info))    # Remove the kid from the list
            santa_list[which_list].append(kid_info[1])

    for name, which_list in kwargs.items():

        found_kids = list(filter(lambda x: x[1] == name, kids_info))
        if len(found_kids) == 1:
            kid_info = found_kids.pop()
            kids_info = list(filter(lambda x: x != kid_info, kids_info))
            santa_list[which_list].append(name)

    if kids_info:
        for kid_info in kids_info:
            santa_list["Not found"].append(kid_info[1])

    result = ""

    for which_list, kids in santa_list.items():
        if kids:
            result += f"{which_list}: {', '.join(kid for kid in kids)}\n"

    return result.strip()




print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))

"""
Create a dict with santa's list

Iterate through all the args and see if the number is present ONLY once in the kids_info list, and if it is, add it to
the Santa's list in the correct  category and remove it from the kids_info list. Else skip this step

Iterate through the kwargs, and check if the kids name is present only once. If it is add it to santa's list in the
correct category and remove it from the kids_info list. Else skip this step.

If there are any kids remaining in the kids_info list, add them to santa's not found list.

return the string

"""