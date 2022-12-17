import re
from collections import defaultdict

GRAPH = {}
RATES = {}

for line in open('input').read().strip().split('\n'):
    front, back = re.split(r'; tunnels? leads? to valves? ', line)
    x = front.split(' ')[1]
    RATES[x] = int(front.split('=')[-1])
    GRAPH[x] = back.split(', ')

node_id = defaultdict(lambda: len(node_id))
[node_id[u] for u in RATES if RATES[u]]
ALL_MASK = (1 << len(node_id)) - 1

cache = defaultdict(
    lambda: [[-1 for mask in range(ALL_MASK + 1)] for t in range(31)])


def DP(pos, time_left, mask):
    if time_left == 0:
        return 0
    if cache[pos][time_left][mask] == -1:
        best = max(DP(v, time_left - 1, mask) for v in GRAPH[pos])
        bit = 1 << node_id[pos]
        if bit & mask:
            best = max(best, DP(pos, time_left - 1, mask - bit) +
                       RATES[pos] * (time_left - 1))
        cache[pos][time_left][mask] = best
    return cache[pos][time_left][mask]


print('Part1', DP('AA', 30, ALL_MASK))
print('Part2', max(DP('AA', 26, ALL_MASK - mask) + DP('AA', 26, mask)
      for mask in range(ALL_MASK + 1)))
