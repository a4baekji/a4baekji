a = []
b = []
for _ in range(5):
    a.append(list(input()))

for i in range(15):
    for j in range(5):
        if i < len(a[j]):
            b.append(a[j][i])

print(''.join(b))
