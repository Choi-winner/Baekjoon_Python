'''
0	0, 1, 2
1	3, 7, 9, 11
2	4, 10, 14, 15
3	0, 4, 5, 6, 7
4	6, 7, 8, 10, 12
5	0, 2, 14, 15
6	3, 14, 15
7	4, 5, 7, 14, 15
8	1, 2, 3, 4, 5
9	3, 4, 5, 9, 13

예제
2
12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12 
12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6



'''
INF = float('inf')
# 입력 받는 부분
import sys
C = int(sys.stdin.readline())
clocks = []
for i in range(C):
    temp = list(map(int, sys.stdin.readline().split()))
    clocks.append(temp)

# 입력받은 것 확인하는 부분.
for i in range(C):
    print(i+1,'번째로 입력된 clock: ', clocks[i])

# 스위치 정의하는 부분.
switchs = [
[	0, 1, 2 ],
[	3, 7, 9, 11],
[	4, 10, 14, 15],
[	0, 4, 5, 6, 7],
[	6, 7, 8, 10, 12],
[	0, 2, 14, 15],
[	3, 14, 15],
[	4, 5, 7, 14, 15],
[	1, 2, 3, 4, 5],
[	3, 4, 5, 9, 13]
] # switch[0~9][0~2or3or4]

# 입력된 스위치의 종류에 따라 실제로 스위치를 누르는 함수.
def conductor(which_clock, which_switch):
    for i in switchs[which_switch]:
        temp = clocks[which_clock][i]
        if temp == 12:
            clocks[which_clock][i] = 3
        else:
            clocks[which_clock][i] += 3
# 이 함수에서 원래는 초기화를 위해서 reverse가 필요한데, 
# 지금 시계에서는 3번 움직인 다음에 1번 더 움직이면 자동으로 리셋되니깐 안만들어도 된다.

# 정렬되었는지의 여부 판단하는 함수.
def areAligned(which_switch):
    if clocks[which_switch].count(12) == 16:
        return True
    else:
        return False
        

# (재귀함수) 모든 경우에 대하여 스위치를 입력하는 함수.
def solve(which_clock, next_switch):
    if next_switch == 10: # 이건 모든 경우의 수를 다 탐색하고 0~9를 끝내고 10이 된 상황.
        if areAligned(which_clock):
            return 0 # 정렬되었다면 0을 반환해서 지금까지의 결과를 출력.
        else:
            return INF
    ret = INF

    for cnt in range(4):
        ret = min(ret, cnt + solve(which_clock, next_switch + 1)) # ret에 inf는 저장되지 않는다.
        conductor(which_clock, next_switch)
    return ret

for i in range(C):
    print(i+1, '번째 경우의 수:', solve(i, 0))