n, x = map(int, input().split())
a_list = [] * n
result_list = []
a_list = list(map(int, input().split())) #map 은 리스트를 반환하지 않아서 오류 발생 list로 둘러싸줘야 한다.
for i in range(n):
    if a_list[i] < x:
        result_list.append(a_list[i])
    else:
        continue
for values in range(len(result_list)):
    print(result_list[values], end = ' ')