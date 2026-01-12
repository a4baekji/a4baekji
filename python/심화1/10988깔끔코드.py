s = input()
center = int(len(s) // 2) #홀수짝수 구분 없이 중간 글자를 기준으로 양옆거만 같은면 된다.
result = 1
for i in range(center): 
    if s[i] != s[-i-1]:
        result = False
        break
if result:
    print(1)
else:
    print(0)