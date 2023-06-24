
check = 0
while check == 0: 
    n = int(input('입력'))  #n 입력, ip의 길이 설정
    if(n >= 1 and n <= 255):
        check = 1

#0열 = 할당횟수, 1열 = 사용중인 컴퓨터
ip_array = [[0 for col in range(2)] for row in range(n)]  

queries = []
computer_data = []

#쿼리 컴퓨터 이름이랑 요청 정보 분할
for i in range(0, len(queries)):
    split_queries = queries[i].split()
    name = split_queries[0]
    
    is_connected = 0
    for j in range(0, len(computer_data)):
        if(computer_data[j][0] == name):
            is_connected = 1
            ip_request(name, j)
    if(is_connected == 0):
        computer_data.append([name, 0])

    request = split_queries[1]
    if(request == "request"):

def ip_request(name, row):
    if(computer_data[row][1] == 0):
        
    computer_data[row][1] = computer_data[row][1] + 1

