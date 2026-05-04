n = int(input())
true_ans = input()
m = int(input())
studens_right_ans = []
studens_wrong_ans = []
res = []
for i in range(m):
    right_ans = set()
    wrong_ans = set()
    marks = input()
    for j in range(len(marks)):
        if marks[j] == true_ans[j]:
            right_ans.add(j + 1)
        else:
            wrong_ans.add((marks[j], j + 1))
    studens_right_ans.append(right_ans)
    studens_wrong_ans.append(wrong_ans)

for i in range(m - 1):
    for j in range(i + 1, m):
        l_right1 = len(studens_right_ans[i])
        l_right2 = len(studens_right_ans[j])
        l_wrong1 = len(studens_wrong_ans[i])
        l_wrong2 = len(studens_wrong_ans[j])
        if len(studens_right_ans[i] & studens_right_ans[j]) > 0.5 * max(l_right1, l_right2) \
                and len(studens_wrong_ans[i] & studens_wrong_ans[j]) > 0.5 * max(l_wrong1, l_wrong2):
            res.append([i + 1, j + 1])

print(len(res))
for elem in res:
    print(*elem)