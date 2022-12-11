from copy import deepcopy

IN = open('input').read().strip()
lines = [x for x in IN.split('\n')]

ITEMS = []
OP = []
TEST = []
TRUE = []
FALSE = []

for monkey in IN.split('\n\n'):
    _, items, op, test, true, false = monkey.split('\n')

    ITEMS.append([int(i) for i in items.split(':')[1].split(',')])

    words = op.split()
    op = ''.join(words[-3:])
    OP.append(lambda old, op=op: eval(op))

    TEST.append(int(test.split()[-1]))
    TRUE.append(int(true.split()[-1]))
    FALSE.append(int(false.split()[-1]))

START = deepcopy(ITEMS)

LCM = 1
for x in TEST:
    LCM *= (LCM * x)

for part in [1, 2]:
    COUNT = [0 for _ in range(len(ITEMS))]
    ITEMS = deepcopy(START)

    for _ in range(20 if part == 1 else 10_000):
        for i in range(len(ITEMS)):
            for item in ITEMS[i]:
                COUNT[i] += 1
                item = OP[i](item)

                if part == 2:
                    item %= LCM

                if part == 1:
                    item = (item // 3)

                if item % TEST[i] == 0:
                    ITEMS[TRUE[i]].append(item)

                else:
                    ITEMS[FALSE[i]].append(item)

            ITEMS[i] = []

    print(sorted(COUNT)[-1] * sorted(COUNT)[-2])
