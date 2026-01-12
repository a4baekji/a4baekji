n , m = map(int, input().split())
a = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for v in range((i-1),j):
        a[v] = k
    # == a[i-1:j] = [k] * (j-i+1) k값을 넣으려고 하면 오류발생 슬라이싱은 리스트처럼 반복값을 받아들이기에 넣으려는 구간 수 만큼 [k]를 만들어 넣어줘야됨
for r in range(len(a)):
    print(a[r], end = ' ') # == print(*a)
