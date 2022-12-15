from parse import parse

with open('input') as f:
    GRID = [[int(j) for j in list(parse(
        "Sensor at x={}, y={}: closest beacon is at x={}, y={}\n", l))] for l in f.readlines()]


def f(DEPTH):
    RING = []
    for i in GRID:
        distance = abs(i[2] - i[0]) + abs(i[3] - i[1])
        if abs(DEPTH - i[1]) < distance:
            k = distance - abs(DEPTH - i[1])
            RING.append([i[0] - k, i[0] + k])
    RING.sort()
    i = 0
    while(i < len(RING) - 1):
        if RING[i][1] + 1 >= RING[i + 1][0]:
            RING[i][1] = max(RING[i + 1][1], RING[i][1])
            RING.pop(i + 1)
            continue
        i += 1

    return RING


# Part 1
print(sum(i[1] - i[0] for i in f(2000000)))

# Part 2
TUNE_CONST = 4000000
for i in range(TUNE_CONST):
    RINGS = f(i)
    for j in RINGS:
        if j[0] <= 0 and j[1] >= TUNE_CONST:
            break
    else:
        for j in RINGS:
            if j[0] <= 0 and j[1] >= 0:
                print((j[1] + 1) * TUNE_CONST + i)
