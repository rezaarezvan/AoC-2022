IN = open('input').read().strip()
DATA = [x for x in IN.split('\n')]

GRID = set()
for line in DATA:
    prev = None
    for point in line.split('->'):
        x, y = point.split(',')
        x, y = int(x), int(y)
        if prev is not None:
            dx = x - prev[0]
            dy = y - prev[1]
            length = max(abs(dx), abs(dy))
            for i in range(length + 1):
                xx = prev[0] + i * (1 if dx > 0 else (-1 if dx < 0 else 0))
                yy = prev[1] + i * (1 if dy > 0 else (-1 if dy < 0 else 0))
                GRID.add((xx, yy))
        prev = (x, y)

ground = 2 + max(r[1] for r in GRID)
lo_x = min(r[0] for r in GRID)-1000
hi_x = max(r[0] for r in GRID)+1000

for x in range(lo_x, hi_x):
    GRID.add((x, ground))

part_1 = False
for _ in range(1000000):
    sand = (500, 0)
    while True:
        if sand[1] + 1 >= ground and (not part_1):
            part_1 = True
            print(_)
        if (sand[0], sand[1] + 1) not in GRID:
            sand = (sand[0], sand[1] + 1)
        elif (sand[0] - 1, sand[1] + 1) not in GRID:
            sand = (sand[0] - 1, sand[1] + 1)
        elif (sand[0] + 1, sand[1] + 1) not in GRID:
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            break
    if sand == (500, 0):
        print(_ + 1)
        break
    GRID.add(sand)
