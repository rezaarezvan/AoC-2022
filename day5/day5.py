import re

def ints(string):
    return list(map(int, re.findall(r"-?[0-9]+", string)))

with open("input") as f:
    lines = iter(f.read().splitlines())
    stack = [[] for _ in range(10)]
    
    '''
    Annoying input parsing...
    '''
    for line in lines:
        if not line:
            break

        if line.startswith("1"):
            continue

        for i, c in enumerate(line[1::4]):
            if not c.isspace():
                stack[i + 1].insert(0, c)

    stack_2 = [s[:] for s in stack]
    
    for line in lines:
        _count, _from, _to = ints(line)

        # Part 1
        for _ in range(_count):
            stack[_to].append(stack[_from].pop())

        # Part 2
        stack_2[_to].extend(stack_2[_from][-_count:])

        # Remove old elements, since we don't pop
        stack_2[_from] = stack_2[_from][:-_count]

print("Part 1:", "".join(s[-1] for s in stack[1:]))
print("Part 2:", "".join(s[-1] for s in stack_2[1:]))
