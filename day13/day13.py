from functools import cmp_to_key

IN = open('input').read().strip()
DATA = [x for x in IN.split('\n')]


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0

        return 1
    elif isinstance(left, list) and isinstance(right, list):
        i = 0

        while i < len(left) and i < len(right):
            c = compare(left[i], right[i])

            if c == -1:
                return -1
            if c == 1:
                return 1
            i += 1

        if i == len(left) and i < len(right):
            return -1

        elif i == len(right) and i < len(left):
            return 1

        return 0

    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)

    else:
        return compare(left, [right])

# Part 1
packets = []
part_1 = 0

for i, group in enumerate(IN.split('\n\n')):
    p1, p2 = group.split('\n')

    p1 = eval(p1)
    p2 = eval(p2)

    packets.append(p1)
    packets.append(p2)

    if compare(p1, p2) == -1:
        part_1 += 1+i

print(part_1)

# Part 2:
packets.append([[2]])
packets.append([[6]])

packets = sorted(packets, key=cmp_to_key(lambda p1, p2: compare(p1, p2)))

part_2 = 1
for i, p in enumerate(packets):
    if p == [[2]] or p == [[6]]:
        part_2 *= i+1

print(part_2)
