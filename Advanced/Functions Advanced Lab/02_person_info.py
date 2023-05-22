# Kwargs will give us a dictionary, you can pack a dictionary into kwargs, and access the keys in the
# function, but the keys have to have the same names as outside.


def get_info(**kwargs):

    return f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))

