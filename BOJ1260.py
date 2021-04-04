'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 
1 2 4 3
1 2 3 4


'''

import sys
from queue import deque

N, M, V = map(int, sys.stdin.readline().split())

d = [ [] for i in range(N+1) ]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    d[a].append(b)
    d[b].append(a)

for i in range(len(d)):
    d[i] = sorted(d[i]) # 작은 수부터 오름 차순으로 탐색하려고 정렬해둠. <- 여기에서 중복을 미리 제거해두는 것도 괜찮긴 하겠다.

vis = [False]*(N+1)

dfs_list = []

def dfs(d, pos, vis):
    if vis[pos]:
        return
    vis[pos] = True
    dfs_list.append(pos)
    for i in range(len(d[pos])):
        dfs(d, d[pos][i], vis) # 위에서 sorted이므로 오름차순으로 출력됌


dfs(d, V, vis)




# BFS start
def queue_push(q, v):
    q.append(v)
def queue_pop(q):
    return q.popleft()

q = deque()

queue_push(q, V)

vis_q = [False]*(N+1)
bfs_list = []

vis_q[V] = True

while len(q) != 0:
    front = queue_pop(q)
    bfs_list.append(front)
    for i in range(len(d[front])):
        if vis_q[d[front][i]]:
            continue
        vis_q[d[front][i]] = True
        queue_push(q, d[front][i])


for i in range(len(dfs_list)):
    print(dfs_list[i], end=' ')
print()
for i in range(len(bfs_list)):
    print(bfs_list[i], end=' ')
# print('end') 
   
# print(str(dfs_list))
# print(str(bfs_list))


