A = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
result = 0
for i in A: # 알파벳 리스트를 하나씩 분리
    for j in i: #분리한 알파벳 뭉치를 또 각각 분리
        for k in s: # 입력 받은 문자열 분리
            if j == k: # 알파벳 각각을 문자 하나하나와 비교
                result += A.index(i) + 3 #알파벳 뭉치의 인덱스에 초를 더 함
print(result)