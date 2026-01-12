n = int(input())
result = []
for _ in range(n):
    s = input()
    result.append(s[0] + s[-1])
for res in result:
    print(res)
# == print("\n".join(result))