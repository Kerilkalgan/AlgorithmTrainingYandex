n = int(input())
data = list(map(int, input().split()))
ans = 0
l, r = 0, -1
d = {}
for l in range(n):
   while r < n and len(d) <= 2:
      if len(d) == 2:
         if r - l + 1 > ans:
            ans = r - l + 1
      r += 1
      if r == n:
         break
      d[data[r]] = d.get(data[r], 0) + 1
   d[data[l]] -= 1
   if d[data[l]] == 0:
      del d[data[l]]
print(ans)
