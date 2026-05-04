cases = int(input())
for _ in range(cases):
    n, d = map(int, input().split())
    prefixsum = [0] * (n + 1)
    sufferance = []
    place = n + 1
    for i in range(n):
        t, k = map(int, input().split())
        sufferance.append(t)
        prefixsum[i+1] = prefixsum[i] + k
    for pos in range(n-1, -1, -1):
       if prefixsum[pos] + d > sufferance[pos]:
          break
       place -= 1
    print(place)
