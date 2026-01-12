s = input().upper()
cnt = 0
result = "?"
for alpha in set(s):
    if s.count(alpha) > cnt:
        cnt = s.count(alpha)
        result = alpha
    elif s.count(alpha) == cnt:
        result = "?"
print(result)