n = int(input())
words = []
for _ in range(n):
    words.append(input())
m = len(words[0])
words.sort()
res = []
for i in range(0, n, 2):
   ind = 0
   while ind < m and words[i][ind] == words[i + 1][ind]:
      ind += 1
   res.append(ind)
print(min(res))