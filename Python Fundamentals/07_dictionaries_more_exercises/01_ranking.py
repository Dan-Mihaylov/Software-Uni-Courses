contest_info = dict()
users_info = dict()

input_line = input()


def check_validity_and_pass(contest_info_, contest_, password_):
    if contest_ in contest_info_:
        if password_ == contest_info_[contest_]:
            return True


def add_user(username_, contest_, points_):
    users_info[username_] = users_info.get(username_, {})
    users_info[username_][contest_] = users_info[username_].get(contest_, 0)
    users_info[username_][contest_] = max(users_info[username_][contest_], points_)


def best_candidate(users_info_: dict):
    best_user = ""
    best_score = 0

    for user, subjects in users_info_.items():
        curr_grade = 0
        for subject, grade in subjects.items():
            curr_grade += grade
        if curr_grade > best_score:
            best_score = curr_grade
            best_user = user

    return best_user, best_score


# we populate the contest_info dict with the contest and the password as value

while input_line != "end of contests":
    contest, password = input_line.split(":")
    contest_info[contest] = contest_info.get(contest, "")
    contest_info[contest] = password

    input_line = input()

input_line = input()

while '=>' in input_line:
    contest, password, username, points = input_line.split('=>')
    points = int(points)
    if check_validity_and_pass(contest_info, contest, password):
        add_user(username, contest, points)

    input_line = input()

# sorting the dict by users, it returns a tuple, so we convert to dict again.

sorted_users = sorted(users_info.items(), key=lambda x: x[0])
sorted_users = dict(sorted_users)

# here we sort the nested dict, by values descending order.

for user, value in sorted_users.items():
    sorted_nested_dict = sorted(value.items(), key=lambda x: -x[1])
    sorted_users[user] = dict(sorted_nested_dict)

best_cand, best_score = best_candidate(users_info)

print(f"Best candidate is {best_cand} with total {best_score} points.")
print(f"Ranking:")
for name, value in sorted_users.items():
    print(f"{name}")
    for course, score in value.items():
        print(f"#  {course} -> {score}")
