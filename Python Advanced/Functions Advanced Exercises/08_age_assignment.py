def age_assignment(*args, **kwargs):
    result_dict = {}
    result_string = ""
    for name in args:
        result_dict[name] = kwargs[name[0]]
    for key, value in dict(sorted(result_dict.items(), key=lambda x: x[0])).items():
        result_string += f"{key} is {value} years old.\n"

    return result_string


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
