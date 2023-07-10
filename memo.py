#input 여러개 받기
a, b = map(int, input().split())

#시간 초과 방지 빠른 input 
import sys
int(sys.stdin.readline())  #한줄 입력
a, b, c = map(int, sys.stdin.readlin().split())  

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

#알고리즘
#계수정렬 Bronze 1 #10989.py 

#재귀함수 Silver 1 #1675
    #> 재귀함수 사용시 재귀함수 깊이로 인해 Recurission Error 발생