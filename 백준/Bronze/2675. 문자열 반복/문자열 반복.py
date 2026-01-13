n = int(input())
result = []
for _ in range(n):
    s, r = input().split() #map으로 안 받고 뒤에서 형변환 시켜주면 된다. 기본 입력받는 값이 문자열이기 때문
    line = ""
    s = int(s)
    for ch in r:
        line += ch * s
    result.append(line)
print("\n".join(result))

