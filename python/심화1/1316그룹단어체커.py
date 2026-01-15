n = int(input())
count = 0

for _ in range(n):
    seen = set()
    Group = True
    word = input()
    for i in range(len(word)):
        if word[i] in seen:
            if word[i] != word[i-1]:
                Group = False
                break
        seen.add(word[i])
    if Group:
        count += 1
print(count)