money_available = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count

for idx in range(len(money_available)):
    beggars_idx = idx % beggars_count
    money = int(money_available[idx])
    beggars[beggars_idx] += money

print(beggars)



# money_available = input().split(", ")
# money_as_integers = [int(x) for x in money_available]
#
# beggars = int(input())
#
# total_received = []
# a = 0
#
# while a < beggars:
#
#     current_received = 0
#
#     for i in range(a, len(money_as_integers), beggars):     # Using the beggars as step, since the first one has to
#         current_received += money_as_integers[i]            # leave enough spaces for the next ones
#
#     total_received.append(current_received)
#     a += 1
#
# print(total_received)