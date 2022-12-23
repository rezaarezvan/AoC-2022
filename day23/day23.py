from collections import Counter

DATA = open('input').read().rstrip().split('\n')

ELF_GRID = {x + 1j * y for y, row in enumerate(DATA)
            for x, c in enumerate(row) if c == '#'}

ADJ_8 = [1, 1 + 1j, 1j, 1j - 1, -1, -1 - 1j, -1j, 1 - 1j]

DIRECTIONS = [-1j, 1j, -1, 1]


def move(elves, p, curr_dir):
    is_adj = elves & {p + adj for adj in ADJ_8}

    if not is_adj:
        return p

    for t in range(4):
        d = DIRECTIONS[(curr_dir + t) % 4]
        is_adj = elves & {p + d, p + d + d * 1j, p + d - d * 1j}

        if not is_adj:
            return p+d

    return p


def empty_ground(elves):
    xs = [elf.real for elf in elves]
    ys = [elf.imag for elf in elves]

    return (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1) - len(elves)


def update(elves, r):
    want = {elf: move(elves, elf, r % 4) for elf in elves}
    c = Counter(want.values())
    canhave = {elf for elf in want if c[want[elf]] == 1}
    canthave = elves - canhave
    return canthave | {want[elf] for elf in canhave}


i = 0
pelfs = {}
while ELF_GRID != pelfs:
    pelfs = ELF_GRID
    ELF_GRID = update(ELF_GRID, i)

    i += 1

    # Part 1
    if i == 10:
        print(empty_ground(ELF_GRID))

# Part 2
print(i)
