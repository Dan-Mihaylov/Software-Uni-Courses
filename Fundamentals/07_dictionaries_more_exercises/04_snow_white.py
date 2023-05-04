input_line = input()

dwarf_info = {}
result_list = []
dwarf_name = "name"
dwarf_hat = "hat"
dwarf_physics = "physic"
length_hat = "hat_len"


def add_dwarf(name_, colour, physics_):
    if colour not in dwarf_info:
        dwarf_info[colour] = {}
    if name_ not in dwarf_info[colour]:
        dwarf_info[colour][name_] = 0
    if dwarf_info[colour][name_] < physics_:
        dwarf_info[colour][name_] = physics_


def add_dwarf_info_to_list():
    for hat in dwarf_info:
        for name_, physic in dwarf_info[hat].items():
            result_list.append({length_hat: len(dwarf_info[hat]), dwarf_name: name_,
                                dwarf_physics: physic, dwarf_hat: hat})


def print_results():
    global result_list
    result_list = list(sorted(result_list, key=lambda item: (-item[dwarf_physics], -item[length_hat])))
    for result in result_list:
        print(f"({result[dwarf_hat]}) {result[dwarf_name]} <-> {result[dwarf_physics]}")


while " <:> " in input_line:
    input_line = input_line.split(" <:> ")
    name = input_line[0]
    dwarf_hat_color = input_line[1]
    dwarf_physics = int(input_line[2])
    add_dwarf(name, dwarf_hat_color, dwarf_physics)
    input_line = input()

add_dwarf_info_to_list()
print_results()


# Petera <:> Red <:> 20000
# Peter1 <:> Red <:> 19000
# Jon <:> white <:> 19000
# Halal <:> aaa <:> 19000
# malaka <:> aaa <:> 19000
# Peter <:> Red <:> 20000
# Once upon a time