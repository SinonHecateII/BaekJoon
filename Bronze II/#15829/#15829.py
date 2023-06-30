L = int(input())
Hash = list(input())

sum = 0
for i in range(0, L):
    #ord() 문자를 유니코드에 맞는 정수로 출력
    sum = sum + ((ord(Hash[i]) - 96) * pow(31, i))        
print(sum % 1234567891)