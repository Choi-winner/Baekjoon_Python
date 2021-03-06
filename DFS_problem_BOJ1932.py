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

ans = -1 
# global변수로 ans를 쓰는 이유?
'''
아마도, 이번 프로그램에서 dfs의 전체 영역에서 ans가 딱 1개 나오기 때문인 것 같다.
각 탐색에서 상태는 유지가 되어야 하는데, 그 역할은 parameter 's'가 잘 수행해준다.
즉, 앞으로 DFS에서는 주로 global변수로 output을 쓰면 될 듯!
'''

def dfs(l, y, x, s): # 배열이 l이고, 현재 위치가 y, x이다.
    global ans # global 선언해주어야 이 함수 안에서 수정할 수 있다.
    if y == len(l): # 끝까지 도착하고 한 칸 더 갈려고 하는 상황! 예를 들어 y = 0, 1, 2, 3, 4(<-끝), 5(<-return)
        if ans < s: # (s의 최댓값을 구하는 문제이므로)ans가 더 커졌다면 업데이트
            ans = s
        return # ans를 return하지는 않는다. ans는 global이므로 나중에 참조하면 된다.

    # (y, x) 위치에서 갈 수 있는 곳은 바로 아래 혹은 바로 아래 오른쪽.
    dfs(l, y+1, x, s + l[y][x])
    dfs(l, y+1, x+1, s + l[y][x]) 


n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

print(l)

dfs(l, 0, 0, 0)
print(ans)