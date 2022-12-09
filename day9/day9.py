with open("input") as f:
    IN = f.read().strip().split("\n")

moves = [(line[0], int(line[1:])) for line in IN]
dz    = {"R": 1, "L": -1, "U": 1j, "D": -1j}

def sign(a):
    return (a > 0) - (a < 0)

def new_tail(head, tail):
    if abs(head - tail) < 2:
        return tail

    tail += sign(head.real - tail.real)
    tail += sign(head.imag - tail.imag) * 1j

    return tail

def part1():
    head = 0
    tail = 0
    visited = {0}

    for direction, distance in moves:
        for _ in range(distance):
            head += dz[direction]
            tail = new_tail(head, tail)
            visited.add(tail)

    return len(visited)

def part2():
    knots = [0 for _ in range(10)]
    visited = {0}

    for direction, distance in moves:
        for _ in range(distance):
            knots[0] += dz[direction]

            for i in range(1, 10):
                knots[i] = new_tail(knots[i - 1], knots[i])

            visited.add(knots[-1])

    return len(visited)

print(f"Part one: {part1()}")
print(f"Part two: {part2()}")
