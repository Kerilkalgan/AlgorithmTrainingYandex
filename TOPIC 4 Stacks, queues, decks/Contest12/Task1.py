from collections import deque

a = list(map(int, input().split()))
dq_a = deque(a)


def fun(dq_a):
    i = 1
    count = 0
    while i < len(dq_a):
        if i + 1 < len(dq_a) and dq_a[i - 1] == dq_a[i] and dq_a[i - 1] == dq_a[i + 1]:
            del dq_a[i]
            count += 1
            k = i
            while k < len(dq_a) and dq_a[i - 1] == dq_a[k]:
                del dq_a[k]
                count += 1
            del dq_a[i - 1]
            count += 1
            i = 0
        i += 1
    return count


print(fun(dq_a))