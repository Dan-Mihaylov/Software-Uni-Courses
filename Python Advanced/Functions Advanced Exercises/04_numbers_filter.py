def even_odd_filter(**kwargs):
    result = kwargs
    for key, values in result.items():

        if key == "even":
            result[key] = list(filter(lambda x: x % 2 == 0, values))

        elif key == "odd":
            result[key] = list(filter(lambda x: x % 2 == 1, values))

    return dict(sorted(result.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

