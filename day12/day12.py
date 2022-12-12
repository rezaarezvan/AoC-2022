from collections import deque

DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
IN = open('input').read().strip()
LINES = [x for x in IN.split('\n')]

GRID = []
for line in LINES:
    GRID.append(line)

N_ROW = len(GRID)
N_COL = len(GRID[0])

E = [[0 for _ in range(N_COL)] for _ in range(N_ROW)]
for r in range(N_ROW):
    for c in range(N_COL):
        if GRID[r][c] == 'S':
            E[r][c] = 1
        elif GRID[r][c] == 'E':
            E[r][c] = 26
        else:
            E[r][c] = ord(GRID[r][c]) - ord('a') + 1


def BFS(part):
    Q = deque()

    for r in range(N_ROW):
        for c in range(N_COL):
            if (part == 1 and GRID[r][c] == 'S') or (part == 2 and E[r][c] == 1):
                Q.append(((r, c), 0))

    S = set()
    while Q:
        (r, c), d = Q.popleft()

        if (r, c) in S:
            continue
        S.add((r, c))

        if GRID[r][c] == 'E':
            return d

        for dr, dc in DIR:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < N_ROW and 0 <= cc < N_COL and E[rr][cc] <= 1 + E[r][c]:
                Q.append(((rr, cc), d+1))


print(BFS(1))
print(BFS(2))
