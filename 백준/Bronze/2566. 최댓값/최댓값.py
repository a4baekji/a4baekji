a = []
for _ in range(9):
    a.append(list(map(int, input().split())))

max_val = a[0][0]
idx1 = 0
idx2 = 0
for i in range(9):
    for j in range(9):
        if a[i][j] >= max_val:
            max_val = a[i][j]
            idx1 = i + 1
            idx2 = j + 1

print(max_val)
print(idx1, idx2)