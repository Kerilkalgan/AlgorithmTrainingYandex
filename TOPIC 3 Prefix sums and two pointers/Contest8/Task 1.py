command = input()
i = 0
j = 0
d = {(0, 0) : 1}
ans = 0
for comm in command:
   if comm == 'U':
      i -= 1
   if comm == 'D':
      i += 1
   if comm == 'R':
      j += 1
   if comm == 'L':
      j -= 1
   d[(i, j)] = d.get((i, j), 0) + 1
   if d[(i, j)] == 2:
      ans += 1
print(ans)