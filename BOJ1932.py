'''
문제
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

예제 입력 1 
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
예제 출력 1 
30
'''
# 2가지 이동만 가능함. 아래 or 왼쪽 아래.
'''
1. DP식 정의
d[i][j] = i번째 행, j번째 열 까지 도달하는 데에 든 cost의 합의 최대.
 
2. 식 세우기
# (i, j)에 도달하라면, 직전 노드는 (i-1, j)나 (i-1,j-1)이어야 한다.
d[i][j] = max( d[i-1][j], d[i-1][j-1] ) + c[i][j]

3. 초기화
d[501][501] = -1 ? 0 ?
d[0][0] = c[0][0]

'''

import sys
n = int(sys.stdin.readline())
c = []
for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    c.append(l)

# print(c)

# initialization
d = [ [ -1 for _ in range(501)] for _1 in range(501) ] # init with 0 (because max function will be used)
d[0][0] = c[0][0]


for i in range(1, n):
    for j in range(i+1): 
        if j == 0: # j == 0, when doesn't have the left-up element 
            d[i][j] = d[i-1][j] + c[i][j] # when d[i][0], only could come from the left-end values.   
            print('case j == 0 d[{}][{}] = {}'.format(i,j,d[i][j]))     
        elif j == i: # right-end case
            d[i][j] = d[i-1][j-1] + c[i][j]
            print('case j == i d[{}][{}] = {}'.format(i,j,d[i][j]))     
        else:
            d[i][j] = max( d[i-1][j] , d[i-1][j-1] ) + c[i][j]
            print('case else d[{}][{}] = {}'.format(i,j,d[i][j]))     


ans = max(d[n-1])
print(ans)
for i in range(n):
    print(d[i][:i+1])

''' to test
3
2
1 2
3 4 1
-> 8

2 
1 
3 5
-> 6

2
1
5 3
-> 6
'''