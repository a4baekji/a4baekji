s = input()
result = []
for i in range(97, 123):
   result.append(str(s.find(chr(i)))) #find() 함수 자체가 그 문자가 나온 처음 인덱스를 반환해줌. 존재하지 않을 경우 -1 반환
print(" ".join(result))
       
# 나중에 다시 풀기
