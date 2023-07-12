#input 여러개 받기
a, b = map(int, input().split())

#시간 초과 방지 빠른 input 
import sys
int(sys.stdin.readline())  #한줄 입력
a, b, c = map(int, sys.stdin.readline().split())  

#리스트로 여러개 받기
NumList = []
NumList = list(map(int, input().split()))

#ord() 문자를 유니코드에 맞는 정수로 출력
print((ord('a') - 96))

import math
math.ceil()  #반올림

NumList = []
NumList.sort()  #오름차순으로 정렬하고 값 변경
NumList.sorted()  #오름차순으로 정렬하지만 NumList의 값은 변경 X

NumList.count()  #리스트안 특정 원소 개수 구할 때

#문자안에 값이 있는지 확인
num = 6
if('6' in str(num)):
    print("num에 6이 있습니다.")

#스택 알고리즘
from collections import deque  #deque
dq = deque([1, 2, 3])
dq.popleft()  #가장 왼쪽값 pop
dq.append(5)  #오른쪽 끝에 append

#알고리즘
#계수정렬 Bronze 1 #10989.py 

#재귀함수 Silver 5 #1675
    #> 재귀함수 사용시 재귀함수 깊이로 인해 Recurission Error 발생

#이진 탐색 Silver 4 #1920