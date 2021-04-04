'''
문제
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐
3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.



어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

예제 입력 1 
7
6
1 2
2 3
1 5
5 2
5 6
4 7
예제 출력 1 
4
'''

import sys
num_vertex = int(sys.stdin.readline())
num_edge = int(sys.stdin.readline())

d = [ [] for i in range(num_vertex+1) ] # d[0]은 사용하지 않는다.

for i in range(num_edge):
    a, b = map(int, sys.stdin.readline().split())
    d[a].append(b)
    d[b].append(a)

# 

# for i in range(num_vertex):
#     print(i, d[i])
    

# # DFS로 먼저 풀어보기
# # 
# # print('---------DFS---------')
# vis = [False]*(num_vertex+1)
# cnt = -1 # 첫 노드는 카운팅 안함.
# def dfs(d, pos, vis):
#     global cnt
#     if vis[pos]:
#         return
#     vis[pos] = True
#     # print('current visiting node: ', pos)
#     cnt += 1 # 1과 연결된 곳이 있어서 카운트를 1 증가시킴.

#     for i in range(len(d[pos])):
#         dfs(d, d[pos][i], vis)

# # vis[1] = True # starts at node 1
# dfs(d, 1, vis)
# print(cnt)


# BFS로 풀어보기.
from queue import deque

def queue_push(q, v):
    q.append(v)
def queue_pop(q):
    return q.popleft()


vis = [False]*(num_vertex+1)
cnt = -1 # 첫 노드는 카운팅 안함.

# queue 생성
q = deque()

queue_push(q, 1)
vis[1] = True

while len(q) != 0:
    front = queue_pop(q)
    cnt += 1
    for i in range(len(d[front])):
        if vis[d[front][i]]:
            continue
        vis[d[front][i]] = True
        queue_push(q, d[front][i])

print(cnt)