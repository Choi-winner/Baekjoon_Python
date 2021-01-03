'''
P1002
문제
조규현과 백승환은 터렛에 근무하는 직원이다. 
하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 
다음은 조규현과 백승환의 사진이다.

이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 
계산하라는 명령을 내렸다. 
조규현과 백승환은 각각 자신의 터렛 위치에서 
현재 적까지의 거리를 계산했다.

조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 
조규현이 계산한 류재명과의 거리 r1과 
백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 
류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스는 다음과 같이 이루어져 있다.

한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. 
x1, y1, x2, y2는 -10,000보다 크거나 같고, 
10,000보다 작거나 같은 정수이고, 
r1, r2는 10,000보다 작거나 같은 자연수이다.

출력
각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 
만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.
'''
from math import *
case_num = int(input())
cases = []

for i in range(0,case_num):
    cases.append(input().split())

result = []
for case in cases:
    d_x = (int(case[0]) - int(case[3]))
    d_y = (int(case[1]) - int(case[4]))
    r1 = int(case[2])
    r2 = int(case[5])
    d = sqrt(pow(d_x,2)+pow(d_y,2))
    
    if d == 0: # 두 원의 중심이 일치하는 경우
        if r1 == r2:
            result.append(-1)
            continue
        else:
            result.append(0)
            continue
    elif r1 < d and r2 < d: # 두 원이 멀리 떨어져 있는 경우.
        if r1 + r2 < d:
            result.append(0)
            continue
        elif r1 + r2 == d:
            result.append(1)
            continue
        elif r1 + r2 > d:
            result.append(2)
    elif r1 >= d or r2 >= d: # 두 원의 중심이 가까이 있는 경우.
        if abs(r1 - r2) < d:
            result.append(2)
            continue
        elif abs(r1 - r2) == d:
            result.append(1)
            continue
        elif abs(r1 - r2) > d: 
            result.append(0)
            continue

for i in result:
    print(i)