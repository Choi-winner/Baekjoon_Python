'''
문제
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 
나누어져 있는 M*N 크기의 보드를 찾았다. 
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 
지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 
변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 
지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
당연히 8*8 크기는 아무데서나 골라도 된다. 
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

'''
n_m = input().split()
n = int(n_m[0]) # 세로 길이
m = int(n_m[1]) # 가로 길이

ch_in = []
for i in range(n):
    ch_in.append(list(input()))

# W -> 0 / B -> 1 로 변형시켜 보자.
for i in range(n):
    for j in range(m):
        if ch_in[i][j] == 'W':
            ch_in[i][j] = 0
        elif ch_in[i][j] == 'B':
            ch_in[i][j] = 1

# 2가지 형태의 체스판 만들기.
# W로 시작하는 것(0으로 시작) -> ch_W 
# B로 시작하는 것(1로 시작) -> ch_B
ch_W = []
for i in range(8):
    if i % 2 == 0:
        ch_W.append([0,1,0,1,0,1,0,1])
    else:
        ch_W.append([1,0,1,0,1,0,1,0])      


# 표준 체스판과 비교하기.
# n m 
# n-7 * m-7 개의 8*8 체스판 가능.

cnt = 64 # 바꿔야하는 것의 수.

for i in range(n-7):
    for j in range(m-7): # i,j는 test체스판의 왼쪽 위 시작 인덱스.
        cnt_W = 0
        cnt_B = 0
        for ii in range(8):
            for jj in range(8):
                if ch_W[ii][jj] != ch_in[i+ii][j+jj]:
                    cnt_W += 1
                else:
                    cnt_B += 1
        cnt = min(cnt_W, cnt_B, cnt)

print(cnt)