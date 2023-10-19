# This is one way with list slicing, the other way it to generate the matrix, and alter the elements into it

from collections import deque

rows, cols = [int(x) for x in input().split()]

queue = deque([x for x in input()])

for row in range(rows):
    curr_list = []
    for col in range(cols):
        curr_letter = queue.popleft()
        curr_list.append(curr_letter)
        queue.append(curr_letter)
    if row % 2 == 0:
        print(*curr_list, sep="")
    else:
        print(*curr_list[::-1], sep="")

# Second Solution


# from collections import deque
#
#
# rows, cols = [int(x) for x in input().split()]
#
# word = list(input())
# word_copy = deque(word)
#
# for row in range(rows):
#     while len(word_copy) < cols:
#         word_copy.extend(word)
#
#     if row % 2 == 0:
#         print(*[word_copy.popleft() for _ in range(cols)], sep="")
#     else:
#         print(*[word_copy.popleft() for _ in range(cols)][::-1], sep="")


