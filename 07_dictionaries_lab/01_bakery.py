all_info = input().split()
items_list = [x for x in all_info if all_info.index(x) % 2 == 0]
quant_list = [x for x in all_info if all_info.index(x) % 2 != 0]
stock_table = {}
for i in range(len(items_list)):
    stock_table[items_list[i]] = int(quant_list[i])

print(stock_table)
