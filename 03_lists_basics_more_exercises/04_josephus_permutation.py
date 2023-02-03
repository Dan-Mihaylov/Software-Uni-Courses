people_in_circle = input().split()
people_in_circle = [int(x) for x in people_in_circle]
kill_sequence = int(input())
next_kill = kill_sequence
output = []

while len(people_in_circle) > 0:
    if next_kill > len(people_in_circle):
        while next_kill > len(people_in_circle):
            next_kill = abs(len(people_in_circle) - next_kill)
        output.append(int(people_in_circle.pop(next_kill - 1)))  # -1 because I kill the index, not the length
    else:
        output.append(int(people_in_circle.pop(next_kill - 1)))
    next_kill += kill_sequence - 1  # -1 because when u kill one person, next person takes his place
output_str = [str(x) for x in output]

print("[", end="")
print(f",".join(output_str), end="")
print(f"]")
