# queue를 이용하여 구현하는 BFS

'''
문제
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

-> output: 30
 
'''
import sys
from queue import deque

def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    return q.popleft()

n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

print(l)

ans = -1
q = deque() # queue 'q' 선언

''' BFS를 풀 때, queue 에 뭘 집어넣고 뭘 빼는 건가?
    queue에 push하는 것은 현재 노드에서 다음으로 갈 수 있는 모든 노드들의 정보!
'''

# 최초 입력. 맨 처음에는 y, x = 0, 0 위치를 탐색할 수 있으므로 [0, 0 s = 0]를 queue에 입력. 
queue_push(q, [0, 0, 0]) # [y, x, s]가 queue에 쌓인다.


while len(q) != 0:

    front = queue_pop(q) # y, x = 0, 0 
    if ans < front[2]:
        ans = front[2]

    if front[0] < n: # front의 y좌표가 n (=depth) 보다 작으므로 더 커져도 된다. (종료조건의 역할!)
        # left와 right는 현재 노드에서 갈 수 있는 다음 노드들!
        left = [ front[0] + 1, front[1], front[2] + l[front[0]][front[1]] ] # y, x = 1, 0
        right = [ front[0] + 1, front[1] + 1, front[2] + l[front[0]][front[1]] ] # y, x = 1, 1
        ''' 위에서, left와 right의 3번째 element에 업데이트하는 s의 값은 
            "현재 노드(front)의 s값" + "현재 노드가 가리키는 위치의 l에 있는 수" 를 업데이트.

            사실, s는 해당 노드의 값이 아니라, 해당 노드 이전까지의 경로에 있던 수를 다 더한 값!
        '''
        
        # q에 left와 right를 순서대로 입력한다. (왼쪽이 우선순위를 가진다고 가정했기 때문.)
        queue_push(q, left)
        queue_push(q, right)

print(ans)