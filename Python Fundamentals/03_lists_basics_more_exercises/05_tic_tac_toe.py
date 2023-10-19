f_line = input().split()
s_line = input().split()
th_line = input().split()

f_line, s_line, th_line = [int(x) for x in f_line], [int(x) for x in s_line], [int(x) for x in th_line]

# Create all instances of 1st player winning
if f_line[0] == 1 and f_line[1] == 1 and f_line[2] == 1:
    print(f"First player won")
elif s_line[0] == 1 and s_line[1] == 1 and s_line[2] == 1:
    print(f"First player won")
elif th_line[0] == 1 and th_line[1] == 1 and th_line[2] == 1:
    print(f"First player won")
elif f_line[0] == 1 and s_line[0] == 1 and th_line[0] == 1:
    print("First player won")
elif f_line[1] == 1 and s_line[1] == 1 and th_line[1] == 1:
    print("First player won")
elif f_line[2] == 1 and s_line[2] == 1 and th_line[2] == 1:
    print("First player won")
elif f_line[0] == 1 and s_line[1] == 1 and th_line[2] == 1:
    print("First player won")
elif f_line[2] == 1 and s_line[1] == 1 and th_line[0] == 1:
    print("First player won")

# Create all instances on second player winning
elif f_line[0] == 2 and f_line[1] == 2 and f_line[2] == 2:
    print(f"Second player won")
elif s_line[0] == 2 and s_line[1] == 2 and s_line[2] == 2:
    print(f"Second player won")
elif th_line[0] == 2 and th_line[1] == 2 and th_line[2] == 2:
    print(f"Second player won")
elif f_line[0] == 2 and s_line[0] == 2 and th_line[0] == 2:
    print("Second player won")
elif f_line[1] == 2 and s_line[1] == 2 and th_line[1] == 2:
    print("Second player won")
elif f_line[2] == 2 and s_line[2] == 2 and th_line[2] == 2:
    print("Second player won")
elif f_line[0] == 2 and s_line[1] == 2 and th_line[2] == 2:
    print("Second player won")
elif f_line[2] == 2 and s_line[1] == 2 and th_line[0] == 2:
    print("Second player won")
else:
    print("Draw!")
