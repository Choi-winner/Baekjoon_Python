'''
문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 
따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. 
(색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. 
(빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.
'''
import sys

# sys.setrecursionlimit(10**7) 

N = int(sys.stdin.readline())
l = []
for i in range(N):
    ch_list = list(sys.stdin.readline())
    l.append(ch_list)

# l_RG = [ [ l[i][j] for j in range(N)] for i in range(N)]
l_RG = [ [None for _ in range(N)] for _ in range(N) ]
for i in range(N):
    for j in range(N):
        if l[i][j] == 'B': # B -> B
            l_RG[i][j] = 'B'
        else: # R, G -> R
            l_RG[i][j] = 'R'


# for i in range(N):
#     print(l[i])

# move
d_x = [+1, 0, -1, 0]
d_y = [0, +1, 0, -1]

# DFS 로 해결
def dfs(l, pos, current):
    y = pos[0]
    x = pos[1]
    
    for k in range(4):
        n_x = x + d_x[k]
        n_y = y + d_y[k]
        if 0 <= n_x < N and 0 <= n_y < N:
            if l[n_y][n_x] == current: # if not visited
                n_current = l[n_y][n_x]
                l[n_y][n_x] = 0 # visited marking
                dfs(l, [n_y, n_x], n_current)

cnt1 = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        if l[i][j] != 0: # 탐색한 곳은 모두 0으로 고칠 예정.
            cnt1 += 1 # cnt incresing
            current = l[i][j]
            l[i][j] = 0
            dfs(l, [i, j], current)


for i in range(N):
    for j in range(N):
        if l_RG[i][j] != 0: # 탐색한 곳은 모두 0으로 고칠 예정.
            cnt2 += 1 # cnt incresing
            current = l_RG[i][j]
            l_RG[i][j] = 0
            dfs(l_RG, [i, j], current)

print(cnt1, cnt2)
