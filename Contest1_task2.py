n, m = map(int, input().split())
L, R, X = [], [], []

for _ in range(n):
    l, r, x = map(int, input().split())
    L.append(l)
    R.append(r)
    X.append(x)
list_in = [int(input()) for _ in range(m)]
res = [0] * m
for k in range(n):
    i = 0
    for num in list_in:
        if L[k] <= num <= R[k]:
            a = 2 if ((num - L[k]) % 2 == 0) else 1
            res[i] += ((-1) ** a) * X[k]
        i += 1

for i in res:
    print(i)