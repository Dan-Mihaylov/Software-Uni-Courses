from pyfiglet import figlet_format


def make_art(message):

    ascii_art = figlet_format(message)
    return ascii_art


print(make_art(input()))
