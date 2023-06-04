# def kwargs_length(**kwargs):
#     len = 0
#
#     for arg in kwargs:
#         len += 1
#
#     return len


def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))

