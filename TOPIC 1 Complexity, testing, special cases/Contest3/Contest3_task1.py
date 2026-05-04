s = input().split()
res = ''
for word in s:
   left = 0
   right = 0
   k = 0
   m = 0
   for el in word:
      if el == "'" and m == 0:
         k = 1
         left += 1
      if el != "'":
         m = 1
      if el == "'" and k == 1 and m == 1:
         right += 1
      k = 1
   res += word[2*left:len(word) - 2*right]

print(res)