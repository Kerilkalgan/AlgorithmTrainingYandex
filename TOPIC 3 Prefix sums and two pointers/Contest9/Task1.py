s = input()
uppercase_alphabet = [chr(code) for code in range(65, 91)]
d = {}
i = 26
for letter in uppercase_alphabet:
    d[letter] = i
    i -= 1
total = 0
sort_s = sorted(s)
for mark in s:
    total += d[mark]

last_key = sort_s[-1]
bad_rating = d[last_key]
avg_total = int(total / len(s) + 0.5)


def f_key(t):
    search_key = None
    for key, value in d.items():
        if value == t:
            search_key = key
            return search_key


if avg_total - bad_rating == 1 or avg_total - bad_rating == 0:
    print(f_key(avg_total))
else:
    print(f_key(bad_rating + 1))


