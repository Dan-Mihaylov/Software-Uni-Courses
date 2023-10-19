def concatenate(*args, **kwargs):
    arguments_together = ""
    for arg in args:
        arguments_together += arg

    for key, value in kwargs.items():
        if key in arguments_together:
            arguments_together = arguments_together.replace(key, value)

    return arguments_together



print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

