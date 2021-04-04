'''
문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때,
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 
집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

입
3
26 40 83
49 60 57
13 89 99
출 
96

입력 분석
3개의 집이 있고,
1번 집은 빨, 초, 파로 칠할 때 각각 26, 40, 83 의 비용이 들고,
2번 집은 각각 49, 60, 57 
3번 집은 각각 13, 89, 99
-> 이웃하는 집의 색은 달라야 한다면, 어떻게 최소 비용으로 모두 색칠?

3개씩 독립적으로 볼 수 있나??

빨, 초 or 파, 

1. DP 식 정의
d[i][j] = i 번째 집을 j 색깔로 칠할 때 왼쪽부터 계산하여 드는 최소 비용. (오른쪽 집의 색은 생각하지 않음.)

2. DP 식 세우기
i = 2 ~ n
d[i][0] = min( d[i-1][1], d[i-1][2] ) + c[i-1][0] # c[i-1][0]은 i번째 집을 Red로 색칠하는 데에 드는 비용.
d[i][1] = min( d[i-1][0], d[i-1][2] ) + c[i-1][1]
d[i][2] = min( d[i-1][0], d[i-1][1] ) + c[i-1][2]

3. DP 식 초기화
# 첫번째 집은 d[1]에 해당.
d[1][0] = c[0][0]
d[1][1] = c[0][1]
d[1][2] = c[0][2]

d 는 집의 갯수 x 3 의 차원을 가지면 됌.
'''

import sys

n = int(sys.stdin.readline())
c = []
for i in range(n): # cost list 'c' beggins from the index of 0 to n-1
    l = list(map(int, sys.stdin.readline().split()))
    c.append(l)

# print(c)

d = [ [0, 0, 0] for _ in range(1002)] # cost를 일단 0, 0, 0으로 초기화

# initialization for the left end house
d[1][0] = c[0][0]
d[1][1] = c[0][1]
d[1][2] = c[0][2] # the index starts from '1' !

# from the left end to the right end, find the minimum cost of painting.
for i in range(2, n+1):
    # to paint i th house the 0(Red) color, the cost of "min( d[i-1][1], d[i-1][2] ) + c[i-1][0]" is needed.
    d[i][0] = min( d[i-1][1], d[i-1][2] ) + c[i-1][0] # c[i-1][0]은 i번째 집을 Red로 색칠하는 데에 드는 비용.
    d[i][1] = min( d[i-1][0], d[i-1][2] ) + c[i-1][1]
    d[i][2] = min( d[i-1][0], d[i-1][1] ) + c[i-1][2]

ans = min(d[n][0], d[n][1], d[n][2])
print(ans)


