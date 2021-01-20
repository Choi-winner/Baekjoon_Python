'''
1
3 7 
#.....# 
#.....# 
##..### 

입력
력의 첫 줄에는 테스트 케이스의 수 C (C <= 30) 가 주어집니다. 
각 테스트 케이스의 첫 줄에는 2개의 정수 H, W (1 <= H,W <= 20) 가 주어집니다. 
다음 H 줄에 각 W 글자로 게임판의 모양이 주어집니다. # 은 검은 칸, . 는 흰 칸을 나타냅니다. 
입력에 주어지는 게임판에 있는 흰 칸의 수는 50 을 넘지 않습니다.

출력
한 줄에 하나씩 흰 칸을 모두 덮는 방법의 수를 출력합니다.

3 
3 7 
#.....# 
#.....# 
##...## 
3 7 
#.....# 
#.....# 
##..### 
8 10 
########## 
#........# 
#........# 
#........# 
#........# 
#........# 
#........# 
########## 

'''

# 입력 받는 부분.
import sys
C = int(sys.stdin.readline())
H_list = []
W_list = []
board = []
for i in range(C):
    H, W = map(int, (sys.stdin.readline()).split())
    H_list.append(H) # H_list[0] = 첫번째 H
    W_list.append(W)
    board_each = []
    for j in range(H):
        a_line = sys.stdin.readline()
        board_each.append(list(a_line)) # board[0] = [#, ., ., ., ., #] 요런식.
    board.append(board_each)

# 입력 받은 것 확인.
print('\n\n입력 테스트: ')
for i in range(C):
    print('\n------------',i+1,'번째 입력에 대한 test ------------')
    print('H: ',H_list[i], ' / W: ',W_list[i])
    for j in range(H_list[i]):
        print(board[i][j]) # board[i][j]에는 i번째 케이스의 j번째 줄 보드의 list가 출력된다.

# 우선 흰색 칸의 수가 3의 배수가 아니면 바로 탈락이다.
# 3의 배수로 흰색 칸의 수를 나눈 것을 N이라고 하면, N은 내려놓은 ㄱ자 블럭의 개수이다.
# 한 조각: 한 블록을 내려놓는 것.
# 재귀로 N조각을 수행하면 된다.
# 흰색 부분을 하나씩 탐색한다.
# 흰색 하나를 기준으로 4가지 경우의 수가 존재한다.
# 중복을 제거하기 위해 빈칸 중에 가장 왼쪽 위부터 채운다.   

# 입력받은 블럭의 흰색 개수를 세는 코드
def canbeCovered(board_check):
    num_of_White = 0
    for a_row in board_check:
        # print('해당 행의 흰색 칸의 개수: ', a_row.count('.'))
        num_of_White += a_row.count('.')
    # num_of_White가 0, 1, 2이면 방법이 없으니깐 N = 0을 리턴.
    # 3의 배수이면 N을 리턴
    # 3의 배수가 아니어도 방법이 없으니깐 N = 0을 리턴.
    if  num_of_White == 0:
        return 0
    elif (num_of_White <= 2) or (num_of_White%3 != 0): # 흰 칸의 개수가 3의 배수이면 N을 리턴
        # print('num_of_White: ',num_of_White, '라서 return -1')
        return -1
    else:
        return int(num_of_White/3)


# 흰색 칸 하나를 선택했다면, 그 칸을 포함하여 놓을 수 있는 블럭의 개수는 8개이다.
# 선택된 칸을 중심으로 2번 이동한다고 생각하자. 
# 첫 이동 시에 오른쪽으로 이동했다면 두번째 이동 시에는 오른쪽의 직각 위치인 위와 아래로 이동이 가능하다.
move_direction = [ [ [1, 0], [0, 1] ], # 오른쪽 이동 -> 위 or 아래 이동
                   [ [1, 0], [0, -1] ],
                   [ [-1, 0], [0, 1]], # 왼쪽 이동 -> 위 or 아래 이동
                   [ [-1, 0], [0, -1] ],
                   [ [0, 1], [1, 0] ], # 위 이동 -> 오른쪽 or 왼쪽 이동
                   [ [0, 1], [-1, 0] ],
                   [ [0, -1], [1, 0] ],  # 아래 이동 -> 오른쪽 or 왼쪽 이동
                   [ [0, -1],[-1, 0] ]  ]
# move_direction[0 ~ 7][0 or 1][0 or 1] 

# covering함수 구현
# 입력: 현재 상태의 보드, 현재 남은 블럭의 개수(최초 N)
ret = 0
def covering(H_in, W_in, board_in):
    N = canbeCovered(board_in)
    if N == 0:
        #print('커버를 모두 끝냈습니다.')
        return 1 # 커버가 완료되어서 1 리턴.
    elif N == -1:
        #print('커버가 불가능한 보드입니다.')
        return 0
    
    ret = 0

    # 왼쪽 위의 흰색을 찾아서 거기를 기준으로 삼는다.
    # 기준으로부터 가능한 블럭을 찾는다.
    for i in range(H_in):
        for j in range(W_in):
            if board_in[i][j] == '.': # 가장 왼쪽 위에 있는 흰색.
                for k in range(8): # 8가지 경우의 수.
                    index_y = [i+move_direction[k][0][0] , i+move_direction[k][1][0]]
                    index_x = [j+move_direction[k][0][1], j+move_direction[k][1][1]]
                    if (0 <= index_y[0] < H_in) and (0 <= index_y[1] < H_in) and (0 <= index_x[0] < W_in)  and (0 <= index_x[1] < W_in): # 가능하다면, 
                        board_in[i][j] = '$'
                        board_in[index_y[0]][index_x[0]] = '$' # 색칠은 조금 다르게 함.
                        board_in[index_y[1]][index_x[1]] = '$'
                        N -= 1 # 한가지 경우 색칠했으므로 N -= 1
                        ret += covering(H_in, W_in, board_in)
                        board_in[i][j] = '.'
                        board_in[index_y[0]][index_x[0]] = '.' # 다시 흰색으로 바꿔놓기.
                        board_in[index_y[1]][index_x[1]] = '.'
    return ret

for i in range(C):
    print(i+1,'번째 보드를 커버하는 경우의 수:', covering(H_list[i], W_list[i], board[i] ) )