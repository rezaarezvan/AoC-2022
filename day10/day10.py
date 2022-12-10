IN = [l.strip().replace("addx", "") for l in open('input')]

total_strength = 0
X = 1
cycle = 0

CRT = [[" " for x in range(40)] for y in range(6)]


def handle_cycle():
    global X, cycle, total_strength

    cycle += 1

    if cycle % 40 == 20:
        total_strength += cycle * X

    if abs((cycle - 1) % 40 - X) < 2:
        CRT[(cycle - 1) // 40][(cycle - 1) % 40] = "#"


for add in IN:
    if add == "noop":
        handle_cycle()
        continue

    handle_cycle()
    handle_cycle()
    X += int(add)

# Part 1
print(total_strength)

# Part 2
for line in CRT:
    print("".join(line))
