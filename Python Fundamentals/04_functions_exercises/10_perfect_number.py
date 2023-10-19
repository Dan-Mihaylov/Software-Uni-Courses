def check_if_perfect(number):
    summary = 0
    for num in range(number - 1, 0, -1):
        if number % num == 0:
            summary += num
    if summary == number:
        print(f"We have a perfect number!")
    else:
        print(f"It's not so perfect.")


initial_input = int(input())
check_if_perfect(initial_input)
