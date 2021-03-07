''' 유기농배추 문제
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

출력 
5
1
'''

# BFS로 풀어보자.
import sys
from queue import deque


# make function of 'push' and 'pop' of queue
def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    front = q.popleft()
    return front

# imputs: 
# T(# of test cases)
# M, N (matrix size is M x N)
# K (# of 유기농배추)
T = int(sys.stdin.readline())

out = []

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    l = [ [ 0 for i in range(N) ] for j in range(M) ] # M x N matrix 'l'
    
    for j in range(K):
        y, x = map(int, sys.stdin.readline().split())
        l[y][x] = 1
    print()
    for row in l:
        print(row)
    

    ''' < queue를 사용하는 방버에 대한 아이디어 >
    1이 발견되면 queue에 해당 위치정보( [y, x] )를 push 한다.
    queue에서 pop 한 front의 위치를 시작으로 다음으로 갈 수 있는 위치정보를 queue에 push한다.
    front의 정보에 있는 값이 1이 아니라 0일 경우, 다음으로 갈 수 없다.
    '''
    
    # make a queue 'q'
    q = deque()
    
    # delta x and y
    dx = [-1, 0, +1, 0 ]
    dy = [0, -1, 0, +1 ]
    
    # output = cnt
    cnt = 0

    for y in range(M):
        for x in range(N):
            # 만약 q 가 비어있다면, 2차원 순회를 진행하며 1을 찾는다.
            # 만약 q 가 비어있지 않다면, 순회하지 않고, queue에 있는 것들을 먼저 처리한다. 
            
            if len(q) > 0: # q에 무언가 있다면 BFS를 돌려 인접한 1을 모두 없앤다.
                front = queue_pop(q)
                y, x = front # 이러면 들어가나?
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny >= 0 and ny < M and nx >= 0 and nx < N:
                        if l[ny][nx] == 1: 
                            l[ny][nx] = 0 # q에 push할 때에는 항상 1을 0으로 바꾸면서 넣는다.
                            queue_push(q, [ny, nx])
            else: # q에 아무것도 없다면, 2차원 순회를 통해 새로운 1을 찾는다.
                if l[y][x] == 1:
                    cnt += 1
                    l[y][x] = 0 # q에 push할 때에는 항상 1을 0으로 바꾸면서 넣는다.
                    queue_push(q, [y, x])
    
    out.append(cnt)

for i in range(T):
    print(out[i])            
