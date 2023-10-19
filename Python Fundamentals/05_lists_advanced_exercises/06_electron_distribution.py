# available_electrons = int(input())
#
# electrons_list = []

# for cell in range(1, available_electrons + 1):
#     electrons_needed = 2 * (cell ** 2)
#     if available_electrons >= electrons_needed:
#         electrons_list.append(electrons_needed)
#         available_electrons -= electrons_needed
#     else:
#         electrons_list.append(available_electrons)
#         break
# if 0 in electrons_list:
#     electrons_list.remove(0)
# print(electrons_list)


available_electrons = int(input())
electrons_list = []
cell = 1
while available_electrons > 0:
    next_cells_electrons = min(available_electrons, 2 * (cell ** 2))
    electrons_list.append(next_cells_electrons)
    available_electrons -= next_cells_electrons
    cell += 1

print(electrons_list)
