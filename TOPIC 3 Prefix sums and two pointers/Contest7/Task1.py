n = int(input())
data = input()
ans = 0
summ = 0
d = {0: 1}
for i in data:
    if i == 'a':
        summ += 1
    else:
        summ -= 1
    if summ in d:
        ans += d[summ]
        d[summ] += 1
    else:
        d[summ] = 1

print(ans)