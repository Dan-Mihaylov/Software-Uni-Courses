
def loading_bar(percent):
    num_percents = percent // 10
    num_dots = 10 - num_percents
    per = num_percents * "%"
    dot = num_dots * "."
    result_string = f"[{per}{dot}]"
    if percent != 100:
        return f"{percent}% {result_string}\nStill loading..."
    else:
        return f"{percent}% Complete!\n{result_string}"


ready = int(input())

print(loading_bar(ready))
