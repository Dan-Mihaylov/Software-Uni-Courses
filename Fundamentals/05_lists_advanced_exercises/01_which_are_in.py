def solve_exercise(list_1, list_2):
    result = list()
    for i in range(len(list_1)):

        for element in list_2:
            if list_1[i] in element:
                result.append(list_1[i])
                break
    return result


first_string = input().split(", ")
second_string = input().split(", ")
print(solve_exercise(first_string, second_string))
