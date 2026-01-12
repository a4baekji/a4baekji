c = [1, 1, 2, 2, 2, 8]
a = list(map(int, input().split()))
result = []
for i in range(6):
    result.append(c[i]-a[i])
print(*result)