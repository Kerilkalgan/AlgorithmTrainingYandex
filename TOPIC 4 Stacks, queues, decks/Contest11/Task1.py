from collections import deque

def is_braces_sequence_correct(data):
    d = {']' : '[', ')' : '(', '}' : '{'}
    open_brackets = ['[', '(', '{']
    stack = []
    for bracket in data:
        if bracket in open_brackets:
            stack.append(bracket)
            continue
        elif bracket in d and (not stack or d[bracket] != stack.pop()):
            stack.append(bracket)
    return len(stack) == 0

def cyclic_shift_correct(s):
    if len(s) == 0:
        return True
    dq_s = deque(s)
    n = len(s)
    for _ in range(n):
        dq_s.rotate(1)
        if is_braces_sequence_correct(list(dq_s)):
            return True
    return False

s_in = input()
print('YES' if cyclic_shift_correct(s_in) else 'NO')