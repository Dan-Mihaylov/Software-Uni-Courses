from collections import  deque


eggs = deque([int(x) for x in input().split(", ")])
papers = deque([int(x) for x in input().split(", ")])

BOX_SIZE = 50
boxes_filled = 0

while eggs and papers:

    egg = eggs.popleft()

    if egg < 1:
        continue

    paper = papers.pop()

    if egg == 13:
        first_paper = papers.popleft()
        papers.append(first_paper)
        papers.appendleft(paper)
        continue

    if egg + paper <= BOX_SIZE:
        boxes_filled += 1

if boxes_filled > 0:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")


