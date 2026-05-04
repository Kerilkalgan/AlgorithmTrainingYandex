n = int(input())
d = {}
for _ in range(n):
    d[input()] = 0
m = int(input())
c_left_past, c_right_past = 0, 0
for _ in range(m):
    data = input().split()
    a, b = int(data[0].split(':')[0]), int(data[0].split(':')[1])
    t = data[1]
    d[t] += (a - c_left_past) + (b - c_right_past)
    c_left_past = a
    c_right_past = b
print(max(d, key=d.get), d[max(d, key=d.get)])