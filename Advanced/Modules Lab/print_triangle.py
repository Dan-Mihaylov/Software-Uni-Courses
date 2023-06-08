def create_triangle(number: int):
    result = []

    for i in range(1, number + 1):
        current = ""

        for j in range(1, i + 1):
            current += str(j)
        result.append(current + "\n")

    for i in range(number - 1, 0, -1):
        current = ""

        for j in range(i, 0, -1):
            current += str(j)
        result.append(current + "\n")

    return "".join(result)
