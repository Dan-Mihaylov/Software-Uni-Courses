food_quant, hay_quant, cover_quant, pig_weight = [float(input()) * 1000 for x in range(4)]

ran_out_of = False
for day in range(1, 31):
    food_quant -= 300
    if day % 2 == 0:
        hay_quant -= food_quant * 0.05
    if day % 3 == 0:
        cover_quant -= pig_weight / 3
    if food_quant <= 0 or hay_quant <= 0 or cover_quant <= 0:
        print("Merry must go to the pet store!")
        ran_out_of = True
        break

if not ran_out_of:
    print(f"Everything is fine! Puppy is happy! Food: {food_quant / 1000:.2f}, Hay: {hay_quant / 1000:.2f}, Cover: "
          f"{cover_quant / 1000:.2f}.")
