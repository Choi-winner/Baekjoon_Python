# 인접리스트로 BFS, DFS
n = 5
# 인접리스트 만들기.
l = [ [] for i in range(n) ] # number of vertex = n
l[0].append(1)
l[0].append(2)
l[0].append(3)

l[1].append(0)

l[2].append(0)
l[2].append(4)

l[3].append(0)
l[3].append(4)

l[4].append(2)
l[4].append(3)

for i in range(n):
    print(i, l[i])

''' 
<만들어진 인접리스트>
pos [adjacent list of pos] 
0 [1, 2, 3]
1 [0]
2 [0, 4]
3 [0, 4]
4 [2, 3]
'''


# dfs로 트리 탐색.
def dfs(l, pos, vis):
    # pos: 현재 탐색하고 있는 노드의 번호(위치)
    # 연결되어 있는 정점들
    # vis: 각 노드들에 대해 지금까지의 방문 여부.
    if vis[pos]:
        return
    vis[pos] = True # 방문했으니 True로 바꿔준다.
    print('current node: ', pos)
    for i in range(len(l[pos])): # l[pos]에 있는 것은 pos와 인접한 노드들의 리스트
        dfs(l, l[pos][i], vis) #  l[pos][i]는 다음으로 탐색할 노드의 위치.

vis = [False]*n
dfs(l, 0, vis) # 0 번 노드를 시작으로 탐색.
print('')
vis = [False]*n
dfs(l, 1, vis)


# BFS로 탐색.
from queue import deque

# Queue에서 사용할 push, pop 함수 만들기.
def queue_push(q, value):
    q.append(value) # 맨 뒤에 넣어준다.

def queue_pop(q):
    return q.popleft()

# 최초에 모두 방문하지 않았다고 visited 에 모두 False
visited = [False] * n

# queue 생성
q = deque()

visited[0] = True # 처음 방문할 곳이 0번 노드
queue_push(q, 0)

while len(q) != 0:
    front = queue_pop(q) # 만약에 queue에 뭐라도 있으면, pop
    print(front)
    for i in range(len(l[front])): # front와 연결되어 있는 곳을 모두 탐색!
        if visited[l[front][i]]:
            continue
        visited[l[front][i]] = True
        queue_push(q, l[front][i])


