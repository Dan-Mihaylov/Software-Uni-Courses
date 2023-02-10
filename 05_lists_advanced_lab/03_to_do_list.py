# notes = [0] * 10
#
# while True:
#     command = input()
#     if command == "End":
#         break
#
#     tokens = command.split("-")
#     priority = int(tokens[0]) - 1
#     note = tokens[1]
#     notes.pop(priority)
#     notes.insert(priority, note)
#
# result = [x for x in notes if x != 0]
# print(result)

notes_list = input().split("-")
all_notes = [0] * 10

while notes_list[0] != "End":
    all_notes.insert(int(notes_list[0]) - 1, notes_list[1])
    notes_list = input().split("-")

all_notes = [x for x in all_notes if x != 0]
print(all_notes)