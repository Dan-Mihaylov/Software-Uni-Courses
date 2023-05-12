iterations = int(input())

longest_length = 0
intersection = []

for _ in range(iterations):
    first, second = input().split("-")
    first_start, first_end = map(int, first.split(","))
    second_start, second_end = map(int, second.split(","))

    first_set = {x for x in range(first_start, first_end + 1)}
    second_set = {j for j in range(second_start, second_end + 1)}

    curr_intersection = first_set.intersection(second_set)

    if len(curr_intersection) > longest_length:
        longest_length = len(curr_intersection)
        intersection = list(curr_intersection)

print(f"Longest intersection is {intersection} with length {longest_length}")

