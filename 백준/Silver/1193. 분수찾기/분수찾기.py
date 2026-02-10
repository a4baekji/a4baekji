n = int(input())
line = 0
end_num = 0

while(end_num < n):
    line += 1
    end_num += line

k = end_num - n

if(line % 2 == 0):
    a = line - k
    b = k + 1
else:
    a = k + 1
    b = line - k
print(str(a) + '/' + str(b))