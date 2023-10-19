from string import punctuation


def count_letters_and_marks(lines_matrix: list):
    result_lines = []

    for i in range(1, len(lines_matrix) + 1):

        curr_line = lines_matrix[i - 1]    # - 1 because i the range to print the correct line which starts from 1
        letters = 0
        punc = 0

        for char in curr_line:
            if char.isalpha():
                letters += 1
            elif char in punctuation:
                punc += 1

        result_lines.append(f"Line {i}: {curr_line[:-2]}. ({letters})({punc})")

    return result_lines


def write_result_to_file(result: list):

    with open("files/output.txt", "w") as output_file:
        output_file.write(f"\n".join(result))


try:
    with open("files/text.txt", "r") as file:
        all_lines = []

        for line in file.readlines():
            all_lines.append(line)

        result_lines = count_letters_and_marks(all_lines)
        write_result_to_file(result_lines)

except FileNotFoundError as error:
    print(error)


