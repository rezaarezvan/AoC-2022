from functools import cmp_to_key

IN = open('input').read().strip()
DATA = [x for x in IN.split('\n')]


def compare(left, right):
    match left, right:
        case int(), int():  return (left>right) - (left<right)
        case int(), list(): return compare([left], right)
        case list(), int(): return compare(left, [right])
        case list(), list():
            for z in map(compare, left, right):
                if z: return z
            return compare(len(left), len(right))


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

packets = sorted(packets, key=cmp_to_key(compare))

part_2 = 1
for i, p in enumerate(packets):
    if p == [[2]] or p == [[6]]:
        part_2 *= i+1

print(part_2)
