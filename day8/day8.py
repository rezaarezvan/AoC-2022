DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def part1(grid):
    result = 0

    M = len(grid)
    N = len(grid[0])

    def is_visible(i, j):
        for di, dj in DIRECTIONS:
            ni, nj = i + di, j + dj

            while 0 <= ni < M and 0 <= nj < N and grid[ni][nj] < grid[i][j]:
                ni += di
                nj += dj

            if not (0 <= ni < M and 0 <= nj < N):
                return True

        return False

    for i in range(M):
        for j in range(N):
            if is_visible(i, j):
                result += 1

    return result

def part2(grid):
    result = 0

    M = len(grid)
    N = len(grid[0])

    def score(i, j):
        score = 1

        for di, dj in DIRECTIONS:
            vision = 0
            ni, nj = i + di, j + dj

            while 0 <= ni < M and 0 <= nj < N:
                vision += 1
                if grid[ni][nj] >= grid[i][j]:
                    break

                ni += di
                nj += dj

            score *= vision

        return score

    for i in range(M):
        for j in range(N):
            result = max(result, score(i, j))

    return result

with open('input') as f:
    grid = []
    for line in f.readlines():
        grid.append(list(map(int, line.strip())))

print(part1(grid))
print(part2(grid))
