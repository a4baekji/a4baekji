import sys
n = int(sys.stdin.readline())
result = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result.append(f"Case #{i+1}: {a} + {b} = {a+b}")
print("\n".join(result)) #join으로 리스트의 각 요소인 문자열 사이사이에 \n줄바꿈을 넣어 하나의 문자열로 만들어 출력
