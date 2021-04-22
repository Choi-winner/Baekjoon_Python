'''
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 
합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
'''
'''
1. DP 식 정의
    2를 나타내는 방법: 2, 1+1
    3을 나타내는 방법: 3, 1+2, 2+1, 1+1+1
    4를 나타내는 방법: 1+3, 3+1, 2+2, 

2. DP 식 세우기
    dp(n) = dp(n-1) + dp(n-2) + dp(n-3)
    n >= 4
3. DP 식 초기화
    dp(1) = 1
    dp(2) = 2
    dp(3) = 4

'''
import sys
T = int(sys.stdin.readline())
d = [0 for _ in range(12)]
d[1] = 1
d[2] = 2
d[3] = 4
def dp(n):
    if d[n] != 0:
        return d[n]
    d[n-1] = dp(n-1)
    d[n-2] = dp(n-2)
    d[n-3] = dp(n-3)
    
    d[n] = d[n-1] + d[n-2] + d[n-3]
    return d[n]

n_list = []
for i in range(T):
    n_list.append(int(sys.stdin.readline()))

for n in n_list:
    num = dp(n)
    print(num)
