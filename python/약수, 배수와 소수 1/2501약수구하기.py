n, k = map(int, input().split())
k -= 1
result = []
for i in range(1, (n // 2) + 1):
    if(n % i == 0):
        result.append(i)
    else:
        continue
result.append(n)
set(result)
sorted_result = sorted(result)
if(k >= len(sorted_result)):
    print(0)
else:
    print(sorted_result[k])