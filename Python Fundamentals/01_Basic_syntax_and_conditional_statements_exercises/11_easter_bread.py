
budget = float(input())
price_1kg_flour =  float(input())

price_pack_eggs = price_1kg_flour * 0.75
price_liter_milk = price_1kg_flour * 1.25
price_milk_needed_for_one = price_liter_milk / 4     # only 0.250 ml needed to make a loaf
price_for_one_loaf = price_1kg_flour + price_milk_needed_for_one + price_pack_eggs

coloured_eggs = 0
bread_made = 0

while budget >= price_for_one_loaf:

    budget -= price_for_one_loaf
    bread_made += 1
    coloured_eggs += 3

    if bread_made % 3 == 0:
        coloured_eggs -= bread_made - 2

print(f"You made {bread_made} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
