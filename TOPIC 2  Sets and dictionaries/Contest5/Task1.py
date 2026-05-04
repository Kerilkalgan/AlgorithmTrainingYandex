def fun(n):
   x, d = map(int, input().split())
   l, r = x - d, x + d
   for _ in range(n-1):
      x, d = map(int, input().split())
      l, r = max(x - d, l), min(x + d, r)
      if l > r:
         return -1
   return r

n = int(input())
print(fun(n))