n, m, k = map(int, input().split())
stack = []
for _ in range(n):
    stack.append('')

def next(now_pos):
    return (now_pos + 1) % n
num_win = 0
tmp = ''
for _ in range(m):
    s = input()
    if s == 'Next':
        num_win = next(num_win)
        continue
    if s == 'Copy':
        tmp = stack[num_win][-k:]
        continue
    if s == 'Paste':
        stack[num_win] += tmp
        continue
    if s == 'Backspace':
       if stack[num_win]:
          stack[num_win] = stack[num_win][:-1]
       continue
    else:
       stack[num_win] += s
if stack[num_win][-k:]:
    print(stack[num_win][-k:])
else:
    print('Empty')
