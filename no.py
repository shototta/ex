n = 5
m = 5
a = [None] * n
for i in range(n):
    a[i] = [0] * m

b = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        b[i][j] = i + j
for i in range(5):
    for j in range(5):
        if i == j:
            b[i][j] = 1
print(*b, sep="\n")