x, y, w, h = map(int, input().split())

#오른쪽 경계선 거리
widthDistanceR = w - x
if(x > widthDistanceR):
    LowWidth = widthDistanceR
else:
    LowWidth = x

#아래 경계선 거리
heightDistanceL = h - y
if(y > heightDistanceL):
    LowHeight = heightDistanceL
else:
    LowHeight = y

if(LowWidth < LowHeight):
    print(LowWidth)
else:
    print(LowHeight)

#문제푼 후 추가사항
#min() 함수를 통해 최솟 값 찾기 가능