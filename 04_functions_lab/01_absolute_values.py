def absolute_value(some_list):
    absolute_list = [abs(float(n)) for n in some_list]
    return absolute_list


string_list = input().split()
print(absolute_value(string_list))

