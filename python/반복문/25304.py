total = int(input())
n = int(input())
result = 0
for _ in range(0, n):
    a, b = map(int, input().split())
    result += a * b
if result == total:
    print("Yes")
else:
    print("No")