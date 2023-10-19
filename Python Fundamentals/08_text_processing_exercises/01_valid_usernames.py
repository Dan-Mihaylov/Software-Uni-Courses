username_list = input().split(", ")

valid_usernames = list()

for username in username_list:
    if 3 <= len(username) <= 16:
        allowed = ["-", "_"]
        is_valid = True
        for letter in username:
            if not letter.isalnum() and letter not in allowed:
                is_valid = False
                break
        if is_valid:
            valid_usernames.append(username)

for username in valid_usernames:
    print(username)
