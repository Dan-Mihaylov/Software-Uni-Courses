def change_symbol_and_order(matrix: list) ->list :  # returns the matrix altered

    new_matrix = []

    for i in range(0, len(matrix), 2):
        curr_line_string = matrix[i][0]    # i to get to the nested list, [0] to extract the content as a string

        for symbol in symbols:
            if symbol in curr_line_string:
                curr_line_string = curr_line_string.replace(symbol, "@")

        reverse_line = [word for word in curr_line_string.split()][::-1]
        new_matrix.append([" ".join(reverse_line)])

    return new_matrix


symbols = [".", "!", "?", ",", "-"]

fp = "files/text.txt"
result = ""

try:
    lines = []

    with open(fp, "r") as file:

        for line in file.readlines():
            lines.append([line])

        lines = change_symbol_and_order(lines)

        [print(' '.join(line)) for line in lines]

except FileNotFoundError as error:
    print(error)