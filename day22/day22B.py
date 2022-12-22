DATA = open('input').read()
MAP, PATH = DATA.split("\n\n")
MAP = MAP.split("\n")

position = MAP[0].index(".")
dir = 0
dirs = [1, 1j, -1, -1j]
dirn = [">", "v", "<", "^"]
PATH = PATH.replace("R", "\nR\n").replace("L", "\nL\n")

firstx = {}
lastx = {}
firsty = {}
lasty = {}

for y, line in enumerate(MAP):
    for x, c in enumerate(line):
        if c != " ":
            if y not in firstx:
                firstx[y] = x
            lastx[y] = x
            if x not in firsty:
                firsty[x] = y
            lasty[x] = y


def at(p):
    return MAP[int(p.imag)][int(p.real)]


def wrapx(p):
    x = int(p.real)
    y = int(p.imag)
    if x > lastx[y]:
        x = firstx[y]
    if x < firstx[y]:
        x = lastx[y]
    return x + y * 1j


def wrapy(p):
    x = int(p.real)
    y = int(p.imag)
    if y > lasty[x]:
        y = firsty[x]
    if y < firsty[x]:
        y = lasty[x]
    return x + y * 1j


def wrapx2(p, d):
    x = int(p.real)
    y = int(p.imag)
    if 0 <= y < 50:
        if x >= 150:
            x = 99
            y = 149 - y
            d = (d + 2) % 4
        elif x < 50:
            x = 0
            y = 149 - y
            d = (d + 2) % 4
    elif 50 <= y < 100:
        if x >= 100:
            x = y + 50
            y = 49
            d = (d + 3) % 4
        elif x < 50:
            x = y - 50
            y = 100
            d = (d + 3) % 4
    elif 100 <= y < 150:
        if x >= 100:
            x = 149
            y = 149 - y
            d = (d + 2) % 4
        elif x < 0:
            x = 50
            y = 149 - y
            d = (d + 2) % 4
    elif 150 <= y < 200:
        if x < 0:
            x = y - 100
            y = 0
            d = (d + 3) % 4
        elif x >= 50:
            x = y - 100
            y = 149
            d = (d + 3) % 4
    return x + y * 1j, d


def wrapy2(p, d):
    x = int(p.real)
    y = int(p.imag)
    if 0 <= x < 50:
        if y < 100:
            y = x + 50
            x = 50
            d = (d + 1) % 4
        elif y >= 200:
            y = 0
            x += 100
    elif 50 <= x < 100:
        if y < 0:
            y = x + 100
            x = 0
            d = (d + 1) % 4
        elif y >= 150:
            y = x + 100
            x = 49
            d = (d + 1) % 4
    elif 100 <= x < 150:
        if y < 0:
            x -= 100
            y = 199
        elif y >= 50:
            y = x - 50
            x = 99
            d = (d + 1) % 4
    return x + y * 1j, d


for c in PATH[:-1].split("\n"):
    try:
        dist = int(c)
        for i in range(dist):
            new_pos = position + dirs[dir]
            if dir % 2 == 0:
                new_pos, nextdir = wrapx2(new_pos, dir)
            else:
                new_pos, nextdir = wrapy2(new_pos, dir)
            if at(new_pos) != "#":
                position = new_pos
                dir = nextdir
    except ValueError:
        rl = c
        if rl == "R":
            dir = (dir + 1) % 4
        else:
            dir = (dir + 3) % 4

x = int(position.real) + 1
y = int(position.imag) + 1
print(y * 1000 + x * 4 + dir)
