DIRECTIONS = {1, -1, 1j, -1j, 0}

with open('input') as file:
    lines = file.read().splitlines()

BLIZZARDS = {"^": [], "v": [], "<": [], ">": [], "#": [], ".": []}

for y, row in enumerate(lines):
    for x, c in enumerate(row):
        BLIZZARDS[c].append(complex(x, y))

START = min(BLIZZARDS["."], key=lambda z: z.imag)
GOAL = max(BLIZZARDS["."], key=lambda z: z.imag)
SIZE = max(BLIZZARDS["#"], key=abs)
MAX_X = int(SIZE.real-1)
MAX_Y = int(SIZE.imag-1)


def move_blizzards():
    for direction, delta in (("^", -1j), ("v", 1j), ("<", -1), (">", 1)):
        new_list = []
        for blizz in BLIZZARDS[direction]:
            blizz += delta
            x, y = int(blizz.real), int(blizz.imag)
            if x == 0:
                x = MAX_X
            if x > MAX_X:
                x = 1
            if y == 0:
                y = MAX_Y
            if y > MAX_Y:
                y = 1
            new_list.append(complex(x, y))
        BLIZZARDS[direction] = new_list


del BLIZZARDS["."]
BLIZZARDS["#"].extend((START-1j, GOAL+1j))


time = 0
for repeat in range(3):
    current_positions = {START}
    while GOAL not in current_positions:
        time += 1
        move_blizzards()
        full_places = {p for l in BLIZZARDS.values() for p in l}
        next_positions = set()
        for curr in current_positions:
            for delta in DIRECTIONS:
                new = curr + delta
                if new not in full_places:
                    next_positions.add(new)
        current_positions = next_positions

    if repeat == 0:
        print("Part 1:", time)

    START, GOAL = GOAL, START

print("Part 2:", time)
