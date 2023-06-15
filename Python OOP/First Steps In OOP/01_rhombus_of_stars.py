def print_rhombus(num: int):
    res = []
    
    for row in range(1, num + 1):
        if row == 1:
            res.append((num - row) * " " + row * "*")
        else:
            res.append((num - row) * " " + row * "* ")
    for rows in range(0, num - 1):
        if rows == 0:
            res.append((num - (row - 1)) * " " + (num - 1) * "* ")
        else:
            res.append((rows + 1) * " " + (num - rows - 1) * "* ")

    return "\n".join(res)


print(print_rhombus(int(input())))
