lines = [l.strip() for l in open('input', 'r') if l.strip()]
CUBES = set(map(eval, lines))


def adj(p):
    for axis in range(3):
        for dir in (-1, 1):
            q = list(p)
            q[axis] += dir
            yield tuple(q)


def part_1():
    sum = 0

    for cube in CUBES:
        for adj_cube in adj(cube):
            if adj_cube not in CUBES:
                sum += 1

    print(sum)

# Cool one-liner
# print(sum(1 for p in P for q in adj(p) if q not in P))


def part_2():
    CUBES_MIN = tuple(min(p[axis] for p in CUBES) - 1 for axis in range(3))
    CUBES_MAX = tuple(max(p[axis] for p in CUBES) + 1 for axis in range(3))

    stack = [CUBES_MIN]
    visited = set()
    sum = 0

    while stack:
        cube = stack.pop()

        if cube in visited:
            continue

        visited.add(cube)

        for adj_cube in adj(cube):
            if adj_cube in CUBES:
                sum += 1
            if (adj_cube not in CUBES and adj_cube not in visited and
                    all(min <= c <= max for min, c, max in zip(CUBES_MIN, adj_cube, CUBES_MAX))):

                stack.append(adj_cube)
    print(sum)


part_1()
part_2()
