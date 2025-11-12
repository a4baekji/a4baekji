a = []
for _ in range(10):
    n = int(input())
    a.append(n % 42)
unique = len(set(a)) #set함수를 이용하여 중복을 제거 후 남은 것들이 중복되지 않는 나머지 값들이기에 그 갯수는 리스트의 길이와 같다
print(unique)