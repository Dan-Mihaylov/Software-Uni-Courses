def password_validator(password):
    is_valid = True
    if not 5 < len(password) <= 10:
        print(f"Password must be between 6 and 10 characters")
        is_valid = False

    if not password.isalnum():
        print(f"Password must consist only of letters and digits")
        is_valid = False

    digit_count = 0
    for char in password:
        if char.isnumeric():
            digit_count += 1

    if not digit_count >= 2:
        print(f"Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print(f"Password is valid")


user_password = input()
password_validator(user_password)
