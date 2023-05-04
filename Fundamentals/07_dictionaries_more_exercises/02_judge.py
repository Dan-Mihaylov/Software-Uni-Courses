judge_info = dict()
users = list()
input_line = input()


def add_user(username_, contest_, points_):
    judge_info[contest_] = judge_info.get(contest_, {})
    judge_info[contest_][username_] = judge_info[contest_].get(username_, 0)
    judge_info[contest_][username_] = max(judge_info[contest_][username_], points_)


def sort_by_points_and_name(dictionary: dict):
    # Nested dict
    for key, value in dictionary.items():
        by_points = sorted(value.items(), key=lambda x: ((-x[1], x[0]), 1))
        dictionary[key] = dict(by_points)
    return dictionary


def get_score(username_, judge_info_:dict):
    total_score = 0
    for key, value in judge_info_.items():
        if username_ in value:
            total_score += value[username_]
    return total_score


while input_line != "no more time":
    username, contest, points = input_line.split(" -> ")
    points = int(points)
    users.append(username)
    add_user(username, contest, points)

    input_line = input()

users_scores = dict()
for i in range(len(users)):
    user = users[i]
    users_scores[user] = get_score(user, judge_info)
users_scores = dict(sorted(users_scores.items(), key=lambda x: -x[1]))

judge_info = sort_by_points_and_name(judge_info)
for contest, participant in judge_info.items():
    count = 1
    print(f"{contest}: {len(participant)} participants")
    for name, score in participant.items():
        print(f"{count}. {name} <::> {score}")
        count += 1

print(f"Individual standings:")
count = 1
for name, score in users_scores.items():
    print(f"{count}. {name} -> {score}")
    count += 1
