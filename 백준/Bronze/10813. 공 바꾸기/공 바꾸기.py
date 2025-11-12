n, m = map(int, input().split())
a_list = [0] * n 
for i in range(n):
    a_list[i] = i + 1 # 빈 리스트에 인덱스를 지정해서 값을 입력하려 했을 때 오류가 발생했다 따라서 윗 줄 코드에서 0 값으로 채워줬다.
for _ in range(m):
    i, j = map(int, input().split())
    a = a_list[i-1]
    a_list[i-1] = a_list[j-1]
    a_list[j-1] = a
print(*a_list)
