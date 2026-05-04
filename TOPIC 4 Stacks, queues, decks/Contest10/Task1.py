n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
count = 0
for i in range(n):
    side = 0
    for j in range(m):
        if grid[i][j] == '#':
            count += 1
            tmp_pos = j
            while j + side < m and grid[i][j + side] == '#':
                grid[i][j + side] = '.'
                side += 1

            for k in range(i + 1, i + side):
                for r in range(tmp_pos, tmp_pos + side):
                    grid[k][r] = '.'
            side = 0
print(count)