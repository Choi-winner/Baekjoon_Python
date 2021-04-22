'''
문제
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 
토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 
 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다.
 M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다. 
 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 
 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 
 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다. 
 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 
 이러한 N개의 줄이 H번 반복하여 주어진다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지 최소 며칠이 걸리는지를 계산해서 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
'''
import sys
from queue import deque

M, N, H = map(int, sys.stdin.readline().split())
ll = []
for _ in range(H):
    l = []
    for _ in range(N):
        l.append(list(map(int, sys.stdin.readline().split())))
    ll.append(l)

# print()
# for l in ll:
#     for one_l in l:
#         print(one_l)
#     print('next line')
# l = ll[0] = 맨 아랫층
# l[0] = 맨 아랫층의 0번 줄 (0 ~ N-1)


# 1은 익은 토마토
# 0은 안익은 토마토
# -1은 빈 칸.
# 익은 토마토의 인접 토마토는 하루만에 익는다.

# 인접 지점으로 가자. BFS
d_y = [0, -1, 0, +1, 0, 0]
d_x = [-1, 0, +1, 0, 0, 0]
d_h = [0, 0, 0, 0, -1, +1]

def q_push(q, value):
    q.append(value)

def q_pop(q): # front pop
    return q.popleft()

q = deque()

for h in range(H):
    for y in range(N):
        for x in range(M):
            if ll[h][y][x] == 1:
                q.append([h, y, x])
                # q_push(q, [h, y, x]) # 익은 토마토를 모두 넣어둔다.

cnt = 0
works = len(q)
pop_num = len(q)
while_entered = False

while len(q) != 0:
    if pop_num == 0:
        cnt += 1
        pop_num = len(q)

    h, y, x = q.popleft() # 익은 토마토 하나의 위치를 꺼낸다.
    pop_num -= 1
    # h, y, x = pos
    for i in range(6): # 익은 토마토 주위 6군데에 안 익은 토마토가 있다면 익히고 1로 만들어 queue에 넣는다.
        n_h = h + d_h[i]
        n_y = y + d_y[i]
        n_x = x + d_x[i]
        if 0 <= n_h <= H-1 and 0 <= n_y <= N-1 and 0 <= n_x <= M-1:
            if ll[n_h][n_y][n_x] == 0:
                q.append([n_h, n_y, n_x])
                # q_push(q, [n_h, n_y, n_x])
                ll[n_h][n_y][n_x] = 1
    while_entered = True

# if while_entered:
#     cnt += 1

for h in range(H):
    for y in range(N):
        for x in range(M):
            if ll[h][y][x] == 0: # 하나라도 0 이 있으면 -1을 출력.
                cnt = -1 
                break  

print(cnt)


'''
4 3 2
0 0 0 0
0 0 1 0
0 0 0 0
-1 -1 0 0
0 0 0 0
0 0 0 0

-> 4


'''