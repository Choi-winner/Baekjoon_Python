'''
문제
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다.
 w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
'''
import sys
end = False
ll = []
while end == False:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    l = [ None for _ in range(h) ]
    for i in range(h):
        l.append(list(map(int, sys.stdin.readline().split())))
    ll.append(l)
# ll[i] = l 각각
# l = map.
# 출력: 섬의 개수!

# l[0][0]에서부터 탐색하며, DFS로 이동할 수 있는 1을 모두 방문하고 방문한 곳은 0으로 고친다.
# DFS에서 만나는 1 말고, for 문에서 만나는 1에 대하여 count를 증가시키고, count = 섬의 개수. <- 출력

for i in range(len(ll)):
    l = ll[i]
    ll[i] = l[len(l)//2:]
    # for a in ll[i]:
    #     print(a)
    # print('---------------')

pos = [0, 0] # pos[0] = h, pos[1] = w
cnt = 0
d_x = [-1, -1, 0, +1, +1, +1, 0, -1 ] # 왼쪽부터 시계 반대 방향으로 회전
d_y = [0, -1, -1, -1, 0, +1, +1, +1] 

def dfs(l, pos):
    y = pos[0]
    x = pos[1]
    h = len(l)
    w = len(l[0])
    # base case: 지도의 마지막까지 탐색을 끝냈고, 마지막 인덱스에 섬이 없는 경우.
    if h == y and w == x and l[-1][-1] == 0:
        return
    if l[y][x] == 1:
        l[y][x] = 0 # visited mark
        for i in range(8):
            new_x = x + d_x[i]
            new_y = y + d_y[i]
            if 0 <= new_x <= w-1 and 0 <= new_y <= h-1:
                if l[new_y][new_x] == 1:
                    # l[new_y][new_x] = 0 # visited mark
                    dfs(l, [new_y, new_x]) 

        # if x - 1 >= 0 and l[y][x-1] == 1: # move left
        #     # next_pos = [y, x-1]
        #     l[y][x-1] = 0 # visited marking
        #     dfs(l, [y, x-1])
        # if y - 1 >= 0 and l[y-1][x] == 1: # move up
        #     l[y-1][x] = 0
        #     dfs(l, [y-1, x]) 
        # if x + 1 <= w and l[y][x+1] == 1: # move right
        #     l[y][x+1] = 0
        #     dfs(l, [y, x+1])
        # if y + 1 <= h and l[y+1][x] == 1: # move down
        #     l[y+1][x] = 0
        #     dfs(l, [y+1, x])
        # if x + 1 <= w and y-1 >= 0 and l[x+1][y-1] == 1: # move right up
        #     l[y-1][x+1] = 0
        #     dfs(l, [y-1, x+1])
        # if x + 1 <= w and l[x+1][y] == 1: # move right
        #     l[y][x+1] = 0
        #     dfs(l, [y, x+1])
    
def search(l):
    cnt = 0
    h = len(l)
    w = len(l[0])

    for i in range(h):
        for j in range(w):
            if l[i][j] == 1:
                cnt += 1
                dfs(l, [i, j]) # l에서 cnt 올린 섬의 1을 모두 0으로 만들고 온다. ( call-by-reference )
    return cnt


for l in ll:
    print( search(l) )

        

