def fire_correct(size, num):
    if size == "High" and 80 < num <= 125:
        return True
    elif size == "Medium" and 50 < num <= 80:
        return True
    elif size == "Low" and 1 <= num <= 50:
        return True
    else:
        return False


fires = input()
total_water = int(input())
total_fire = 0

current_word = ""
current_num = ""
total_effort = 0

for letter in fires:
    if letter.isalpha():
        current_word += letter
        current_num += " "
    elif letter.isnumeric():
        current_num += letter
        current_word += " "

type_fire_list = current_word.split()
amount_fire_list = current_num.split()  # saved as a string
cells_extinguished = []

for i in range(len(type_fire_list)):

    if fire_correct(type_fire_list[i], int(amount_fire_list[i])):

        if total_water >= int(amount_fire_list[i]):
            total_effort += 0.25 * int(amount_fire_list[i])
            total_fire += int(amount_fire_list[i])
            cells_extinguished.append(int(amount_fire_list[i]))
            total_water -= int(amount_fire_list[i])

print(f"Cells:")
for i in cells_extinguished:
    print(f" - {i}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
