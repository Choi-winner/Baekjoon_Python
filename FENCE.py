'''


예제 입력
3
7
7 1 5 9 6 7 3
7
1 4 4 4 4 1 1 
4
1 8 2 2

출력
20
16
8 
'''

#입력 받는 부분
import sys
C = int(sys.stdin.readline())
L_list = []
H_list = []
for i in range(C):
    L_list.append(int(sys.stdin.readline()))
    temp = list(map(int, sys.stdin.readline().split()))
    H_list.append(temp)

# L_list[ 0 ~ C-1 ]
# i = o ~ C-1
# H_list[i][ 0 ~ L_list[i] ]

print('\n')
for i in range(C):
    print(L_list[i])
    print(H_list[i])

# 직사각형의 넓이는 (r-l+1)*min(h[i]) h[i]는 r과 l사이의 막대들의 넓이.
# 그 넓이 중 가장 짧은 것과 밑변의 길이를 곱한 값이 직사각형의 넓이.

# 높이 배열과 시작 인덱스와 끝 인덱스가 주어지면 넓이를 구하는 함수.
def area(which_case, start, end):
    return min(H_list[which_case][end:start+1])*(end - start + 1)

# 3가지 부분의 최대 직사각형의 넓이를 출력
# 기저 케이스: 1칸만 남는 경우.
def solve(which_case, left, right):
    if left == right:
        return H_list[which_case][left]
    # [left, mid]와 [mid+1, right]로 2개로 나눈다.
    mid = int((left + right)/2)
    ret = max(solve(which_case, left, mid), solve(which_case, mid+1, right))

    # 가운데 부분을 포함하는 사각형의 넓이를 계산.
    lo = mid
    hi = mid+1
    height = min(H_list[which_case][lo], H_list[which_case][hi])
    ret = max(ret, height*2) # height의 높이를 가지고 밑변이 2인 사각형과 앞서 구한 2개의 사각형 중 큰 것을 구한다.
    while( left < lo or hi < right ):
        # 높이가 더 높은 쪽으로 확장한다.
        if hi < right and ((lo == left) or (H_list[which_case][lo-1] < H_list[which_case][hi+1])):
            hi += 1 # 오른쪽이 더 놓은 경우라서 오른쪽으로 한 칸 이동한다.
            height = min(height, H_list[which_case][hi]) # 둘 중 큰 높이.
        else:
            lo -= 1
            height = min(height, H_list[which_case][lo])
        ret = max(ret, height * (hi - lo + 1))
    return ret

for i in range(C):
    print(i+1,'번째 입력에 대한 출력:',solve(i,0,L_list[i]-1))

