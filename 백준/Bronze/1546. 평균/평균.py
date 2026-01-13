n = int(input())
a = [0] * n
result = 0
a = list(map(int, input().split()))
i = max(a)
for j in range(n):
    a[j] = a[j]/i*100
for values in range(n):
    result += a[values]
result = result/n
print(f'{result:.2f}')

