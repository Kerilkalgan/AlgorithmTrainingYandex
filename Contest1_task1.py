n, m = map(int, input().split())
tabl = [str(input()) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if (j != m-1) and tabl[i][j] == '.' and tabl[i][j+1] == '.':
           count += 1
        if (i != n-1) and tabl[i][j] == '.' and tabl[i+1][j] == '.':
           count += 1
print(count)