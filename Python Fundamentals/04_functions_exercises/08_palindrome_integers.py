def check_palindrome(char_list):
    for number in char_list:
        if number == number[::-1]:
            print("True")
        else:
            print("False")


initial_input = input().split(", ")
check_palindrome(initial_input)
