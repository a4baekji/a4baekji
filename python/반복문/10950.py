n = int(input())
i = 0
k = 0
result = [0] * n #result = [n] 으로 할 경우 n칸의 리스트가 생기는게 아니라 그냥 n값을 가진 한 칸의 리스트 생성
while i < n:
    a, b = map(int,input().split())
    result[i] = a + b
    i += 1
while k < n:
    print(result[k])
    k += 1