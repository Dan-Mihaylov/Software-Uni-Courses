def vowel_filter(function):

    def wrapper():
        res = [x for x in function() if x.lower() in "aeiouy"]
        return res

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())

