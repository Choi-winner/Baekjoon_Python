# 유기농배추 문제 by dfs
'''
문제
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 
농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 
한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 
그 배추들 역시 해충으로부터 보호받을 수 있다.

(한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있다고 간주한다)

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다. 
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 
총 몇 마리의 지렁이가 필요한지 알 수 있다.

예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.

(0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.)

1	1	0	0	0	0	0	0	0	0
0	1	0	0	0	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	1	1	0	0	0	1	1	1
0	0	0	0	1	0	0	1	1	1
입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 
그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.

출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

입력
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''

import sys

def dfs(l, y, x):
    # 현재의 위치는 l[y][x]
    if l[y][x] == 1: # 1 을 만나면 계속 가본다! 
        l[y][x] = 0  # 0으로 바꾸고 간다!
    else: # 1 이 아닌 곳에 왔으면 다시 되돌아 가야지!
        return

    if x - 1 >= 0:
        dfs(l, y, x-1) # 좌 이동
    if y - 1 >= 0:
        dfs(l, y-1, x) # 위 이동
    if x + 1 <= len(l[0]) - 1:
        dfs(l, y, x+1) # 우 이동
    if y + 1 <= len(l) - 1:
        dfs(l, y+1, x) # 아래 이동

''' 상하좌우 탐색하는 알고리즘 간소화 방법.
dx = [0, 0, -1, +1 ] # delta_x
dy = [-1, +1, 0, 0 ] # delta_y
for i in range(4):
    nx = x + dx[i] # next_x = current_x + delta_x
    ny = y + dy[i] # next_y = current_y + delta_y
# 즉, i = 0 : top / i = 1 : bottom / i = 2 : left / i = 3 : right
'''


T = int(sys.stdin.readline())
out = []
for i in range(T):
    # print('------Test case ', i, '------')

    M, N, K = map(int, sys.stdin.readline().split())
    l = [ [ 0 for i in range(N) ] for j in range(M) ] # MxN 의 matrix 선언.

    for i in range(K):
        y, x = map(int, sys.stdin.readline().split())
        l[y][x] = 1 # 배추가 있는 곳은 1로 바꿔준다.
  
    cnt = 0
    for y in range(M):
        for x in range(N): # 2차원 순회!
            if l[y][x] == 1:
                cnt += 1
                dfs(l, y, x)
            
    # print('결과 출력')        
    # for a_line in l:
    #     print(a_line)
    out.append(cnt)

for i in range(T):
    print(out[i])
    

    # dfs idea: 2차원 순회를 하면서, 연결되어 있는 1을 모두 제거하는 방법을 쓰겠다. 
    #           (0, 0)부터 시작하여 1을 만나면 cnt += 1하고, 그와 연결되어 있는 1을 모두 찾아 0으로 만든다.