def mem(n, s):
   res = []
   count = 0
   for i in range(len(s)):
      if s[i] in ('a', 'h'):
         if i >= 1:
            if s[i] == s[i-1]:
               res.append(count)
               count = 0
         count += 1
      else:
         res.append(count)
         count = 0
   return max(res)

n = int(input())
s = input() + '*'
print(mem(n, s))