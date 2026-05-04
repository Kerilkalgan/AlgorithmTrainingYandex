def fun_rotate(l):
   return l[-1:] + l[:-1]

def fun(n, a):
   num = 0
   i = 0
   count = 0
   while i < len(a):
      if count == n:
         return -1
      num += 1
      if num == a[i]:
         a = fun_rotate(a)
         num = 0
         i = 0
         count += 1
         continue
      i += 1
   return count

n = int(input())
a = list(map(int, input().split()))