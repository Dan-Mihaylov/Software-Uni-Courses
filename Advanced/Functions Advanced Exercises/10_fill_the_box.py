def fill_the_box(h, l, w, *args):
    total_space = h * l * w

    for arg in args:
        if arg == "Finish":
            break
        else:
            total_space -= arg

    if not total_space >= 0:
        return f"No more free space! You have {abs(total_space)} more cubes."

    return f"There is free space in the box. You could put {total_space} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
