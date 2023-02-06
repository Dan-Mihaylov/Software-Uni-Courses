def odd_even_check(number_as_string):
    sum_even = 0
    sum_odd = 0
    for char_num in number_as_string:
        num = int(char_num)
        if num % 2 != 0:
            sum_odd += num
        else:
            sum_even += num

    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")
    # return [sum_even, sum_odd]


nums_as_string = input()
odd_even_check(nums_as_string)
